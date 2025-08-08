import pandas as pd
import numpy as np
import os
import glob
from tqdm import tqdm
import joblib

# --- 1. CONFIGURATION ---

# File and Directory Paths
DATA_DIR = 'ml_forward'
VIX_FILE = 'vix_data.csv'
MODEL_FILE = 'rf_profitability_model.joblib'
IMPUTER_FILE = 'feature_imputer.joblib'
OUTPUT_FILENAME = 'ml_forward_test_results.csv'

# Forward Test Period
FORWARD_TEST_START = '2024-07-31'
FORWARD_TEST_END = '2025-07-31'

# Portfolio and Strategy Parameters
INITIAL_CAPITAL = 1_000_000.00
COMMISSION_RATE = 0.001
ENTRY_Z_SCORE = 3.0
EXIT_Z_SCORE = 0.5
MAX_CONCURRENT_PAIRS = 10
MAX_HOLD_DAYS = 150
ML_CONFIDENCE_THRESHOLD = 0.5 # Only enter if model predicts > 50% chance of profit

# --- EXACT Features the model was trained on, in the correct order ---
MODEL_FEATURES = [
    'spread_volatility', 'hedge_ratio', 'spread_ma_ratio', 'spread_momentum',
    'rsi1', 'atr1_norm', 'macd1', 'rsi2', 'atr2_norm',
    'is_high_vix', 'is_low_vix', 'z_score_slope', 'z_score_abs'
]

def load_vix_data(filepath):
    """Loads and preprocesses the VIX data to create VIX-based features."""
    try:
        vix_df = pd.read_csv(filepath, index_col='datetime', parse_dates=True)
        vix_df.index = vix_df.index.normalize()
        vix_df = vix_df[['close']].rename(columns={'close': 'vix'})
        
        vix_mean = vix_df['vix'].rolling(window=60).mean()
        vix_std = vix_df['vix'].rolling(window=60).std()
        vix_df['vix_zscore'] = (vix_df['vix'] - vix_mean) / vix_std
        vix_df['is_high_vix'] = (vix_df['vix_zscore'] > 1).astype(int)
        vix_df['is_low_vix'] = (vix_df['vix_zscore'] < -1).astype(int)
        print("VIX data loaded and processed successfully.")
        return vix_df[['is_high_vix', 'is_low_vix']]
    except FileNotFoundError:
        print(f"Warning: VIX file '{filepath}' not found. VIX features will be disabled.")
        return None

def run_ml_forward_test():
    """
    Runs a forward test of the pairs trading strategy, using a trained ML model
    to filter entry signals on unseen data.
    """
    # --- 2. LOAD ARTIFACTS AND DATA ---
    print("Loading ML model and imputer...")
    try:
        model = joblib.load(MODEL_FILE)
        imputer = joblib.load(IMPUTER_FILE)
    except FileNotFoundError:
        print(f"Error: Could not find model ('{MODEL_FILE}') or imputer ('{IMPUTER_FILE}'). Aborting.")
        return

    vix_features = load_vix_data(VIX_FILE)

    print(f"Loading and preprocessing {len(glob.glob(os.path.join(DATA_DIR, '*.csv')))} pair data files...")
    all_pairs_data = {}
    for file_path in tqdm(glob.glob(os.path.join(DATA_DIR, "*.csv")), desc="Preprocessing Pairs"):
        pair_name = os.path.basename(file_path).replace('.csv', '')
        try:
            df = pd.read_csv(file_path, index_col='datetime', parse_dates=True)
            df.index = df.index.normalize()

            # --- On-the-fly Feature Engineering to match training ---
            if vix_features is not None:
                df = pd.merge(df, vix_features, left_index=True, right_index=True, how='left')
                df[['is_high_vix', 'is_low_vix']] = df[['is_high_vix', 'is_low_vix']].fillna(0)
            else:
                df['is_high_vix'] = 0
                df['is_low_vix'] = 0

            df['z_score_abs'] = np.abs(df['z_score'])
            df['z_score_slope'] = df['z_score'].diff(3) # Using a 3-day difference as in training

            all_pairs_data[pair_name] = df
        except Exception as e:
            print(f"Could not process {pair_name}: {e}")

    # --- 3. PORTFOLIO SETUP FOR FORWARD TEST ---
    portfolio = {
        'cash': INITIAL_CAPITAL, 'total_value': INITIAL_CAPITAL,
        'positions': {pair: {} for pair in all_pairs_data.keys()}
    }
    closed_trades = []
    
    master_timeline = sorted(list(set.union(*[set(df.index) for df in all_pairs_data.values()])))
    forward_test_timeline = [d for d in master_timeline if pd.to_datetime(FORWARD_TEST_START) <= d <= pd.to_datetime(FORWARD_TEST_END)]
    
    if not forward_test_timeline:
        print("Error: No data available for the specified forward test period.")
        return
        
    print(f"\nForward test running from {forward_test_timeline[0].date()} to {forward_test_timeline[-1].date()}")

    # --- 4. MAIN FORWARD TEST LOOP ---
    for current_date in tqdm(forward_test_timeline, desc="Processing Dates"):
        # A. Mark-to-Market
        current_value = portfolio['cash']
        open_positions = 0
        for pair, position in portfolio['positions'].items():
            if position:
                open_positions += 1
                try:
                    data = all_pairs_data[pair].loc[current_date]
                    current_value += (position['size_s1'] * data['stock1_close'] + 
                                      position['size_s2'] * data['stock2_close'])
                except KeyError:
                    current_value += position.get('entry_value', 0)
        
        portfolio['total_value'] = current_value
        capital_per_trade = portfolio['total_value'] / MAX_CONCURRENT_PAIRS

        # B. Process signals for each pair
        for pair_name, pair_data in all_pairs_data.items():
            if current_date not in pair_data.index:
                continue
            
            daily_data = pair_data.loc[current_date]
            position = portfolio['positions'][pair_name]

            # --- C. EXIT LOGIC (Unchanged) ---
            if position:
                exit_signal, exit_reason = False, ""
                days_held = (current_date - position['entry_date']).days
                
                if ((position['type'] == 'LONG' and daily_data['z_score'] >= -EXIT_Z_SCORE) or
                    (position['type'] == 'SHORT' and daily_data['z_score'] <= EXIT_Z_SCORE)):
                    exit_signal, exit_reason = True, "Z-Score Reversion"
                elif days_held > MAX_HOLD_DAYS:
                    exit_signal, exit_reason = True, "Time Stop Loss"
                
                if exit_signal:
                    exit_s1 = position['size_s1'] * daily_data['stock1_close']
                    exit_s2 = position['size_s2'] * daily_data['stock2_close']
                    exit_comm = (abs(exit_s1) + abs(exit_s2)) * COMMISSION_RATE
                    portfolio['cash'] += (exit_s1 + exit_s2 - exit_comm)
                    pnl_comm = (exit_s1 + exit_s2) - position['entry_value'] - position['entry_commission'] - exit_comm
                    
                    closed_trades.append({
                        'pair': pair_name, 'entry_date': position['entry_date'].date(),
                        'exit_date': current_date.date(), 'days_held': days_held,
                        'exit_reason': exit_reason, 'pnlcomm': pnl_comm,
                        'model_approved': position['model_approved']
                    })
                    portfolio['positions'][pair_name] = {}

            # --- D. ML-POWERED ENTRY LOGIC ---
            elif open_positions < MAX_CONCURRENT_PAIRS:
                trade_type = None
                if daily_data['z_score'] < -ENTRY_Z_SCORE: trade_type = "LONG"
                elif daily_data['z_score'] > ENTRY_Z_SCORE: trade_type = "SHORT"
                
                if trade_type:
                    # A trade is triggered by Z-score, now ask the model for approval
                    try:
                        # 1. Prepare feature vector as a DataFrame with correct column names
                        features_for_model_df = pd.DataFrame([daily_data[MODEL_FEATURES]])
                        
                        # 2. Impute missing values using the DataFrame
                        #    This fixes the SimpleImputer warning.
                        features_imputed = imputer.transform(features_for_model_df)
                        
                        # 2a. Re-create a DataFrame for the model prediction
                        #    This fixes the RandomForestClassifier warning.
                        features_ready_for_model = pd.DataFrame(features_imputed, columns=MODEL_FEATURES)
                        
                        # 3. Get probability prediction from the model
                        profit_probability = model.predict_proba(features_ready_for_model)[0, 1]
                        
                        # 4. Check if probability exceeds our confidence threshold
                        if profit_probability > ML_CONFIDENCE_THRESHOLD:
                            # ** MODEL APPROVES TRADE **
                            size_s1 = (capital_per_trade * 0.5) / daily_data['stock1_close']
                            if trade_type == 'SHORT': size_s1 *= -1
                            
                            size_s2 = -size_s1 * daily_data['hedge_ratio']
                            entry_s1 = size_s1 * daily_data['stock1_close']
                            entry_s2 = size_s2 * daily_data['stock2_close']
                            entry_comm = (abs(entry_s1) + abs(entry_s2)) * COMMISSION_RATE
                            
                            portfolio['cash'] -= (entry_s1 + entry_s2 + entry_comm)
                            
                            portfolio['positions'][pair_name] = {
                                'type': trade_type, 'entry_date': current_date,
                                'size_s1': size_s1, 'size_s2': size_s2,
                                'entry_value': entry_s1 + entry_s2,
                                'entry_commission': entry_comm,
                                'model_approved': True
                            }
                            open_positions += 1
                            
                    except Exception as e:
                        # This can happen if data for a feature is NaN (e.g., at the start of the period)
                        # print(f"Could not get model prediction for {pair_name} on {current_date.date()}: {e}")
                        pass

    # --- 5. FINAL CLEANUP & RESULTS ---
    print("\nClosing any remaining open positions at the end of the test...")
    
    for pair_name, position in portfolio['positions'].items():
        if position:
            try:
                
                # Use the last available row for the specific pair, not a global last_day
                last_data = all_pairs_data[pair_name].iloc[-1]
                last_known_date = last_data.name # Get the actual date of the last row
                
                exit_s1 = position['size_s1'] * last_data['stock1_close']
                exit_s2 = position['size_s2'] * last_data['stock2_close']
                exit_comm = (abs(exit_s1) + abs(exit_s2)) * COMMISSION_RATE
                portfolio['cash'] += (exit_s1 + exit_s2 - exit_comm)
                pnl_comm = (exit_s1 + exit_s2) - position['entry_value'] - position['entry_commission'] - exit_comm
                
                closed_trades.append({
                    'pair': pair_name, 
                    'entry_date': position['entry_date'].date(),
                    'exit_date': last_known_date.date(), 
                    'days_held': (last_known_date - position['entry_date']).days,
                    'exit_reason': "End of Backtest", 
                    'pnlcomm': pnl_comm, 
                    'model_approved': position['model_approved']
                })
            except IndexError:
                # This could happen if a pair's DataFrame is unexpectedly empty.
                print(f"Warning: Could not close position for {pair_name} as its data is empty.")
            except Exception as e:
                print(f"Warning: An error occurred closing position for {pair_name}: {e}")

    if closed_trades:
        trades_df = pd.DataFrame(closed_trades)
        trades_df.to_csv(OUTPUT_FILENAME, index=False)
        
        final_value = portfolio['cash']
        total_return = (final_value - INITIAL_CAPITAL) / INITIAL_CAPITAL * 100
        win_rate = (trades_df['pnlcomm'] > 0).mean() * 100
        
        print("\n" + "="*50)
        print("ML-POWERED FORWARD TEST RESULTS")
        print(f"Period: {FORWARD_TEST_START} to {FORWARD_TEST_END}")
        print("="*50)
        print(f"Final Portfolio Value: ${final_value:,.2f}")
        print(f"Total Return: {total_return:.2f}%")
        print(f"Total Trades: {len(trades_df)}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"Average PnL per Trade: ${trades_df['pnlcomm'].mean():,.2f}")
        print(f"\nResults saved to {OUTPUT_FILENAME}")
        print("="*50)
    else:
        print("\nNo trades were executed during the forward test period.")

if __name__ == '__main__':
    run_ml_forward_test()