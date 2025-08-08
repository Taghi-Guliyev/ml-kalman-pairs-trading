import pandas as pd
import numpy as np
import os
import glob
from tqdm import tqdm

def generate_ml_training_data():
    """
    This code synchronizes the final portfolio
    value calculation and position sizing to be identical to the Kalman backtester,
    ensuring perfectly matched results.
    """
    # --- 1. CONFIGURATION ---
    DATA_DIR = 'kalman_signal_features'
    OUTPUT_FILENAME = 'detailed_trades_features.csv' 
    INITIAL_CAPITAL = 1_000_000.00
    COMMISSION_RATE = 0.001
    
    # Strategy Parameters
    ENTRY_Z_SCORE = 3.0
    EXIT_Z_SCORE = 0.5
    MAX_CONCURRENT_PAIRS = 10
    MAX_HOLD_DAYS = 150
    
    # Feature columns (not used in logic, but good for analysis)
    FEATURE_COLUMNS = [
        'z_score', 'spread_volatility', 'hedge_ratio', 
        'spread_ma_ratio', 'spread_momentum', 'corr_30d',
        'rsi1', 'atr1_norm', 'ema_dist1', 'macd1',
        'rsi2', 'atr2_norm', 'ema_dist2', 'macd2'
    ]
    
    # --- 2. DATA LOADING ---
    all_pairs_data = {}
    data_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    if not data_files:
        print(f"Error: No data files found in '{DATA_DIR}'")
        return
        
    print(f"Loading {len(data_files)} pair data files...")
    for file_path in data_files:
        pair_name = os.path.basename(file_path).replace('.csv', '')
        try:
            df = pd.read_csv(file_path, index_col='datetime', parse_dates=True)
            all_pairs_data[pair_name] = df
        except Exception as e:
            print(f"Error loading {pair_name}: {str(e)}")
            continue

    # --- 3. PORTFOLIO SETUP ---
    portfolio = {
        'cash': INITIAL_CAPITAL,
        'total_value': INITIAL_CAPITAL,
        'positions': {pair: {} for pair in all_pairs_data.keys()}
    }
    closed_trades = []
    
    master_timeline = sorted(list(set.union(*[set(df.index) for df in all_pairs_data.values()])))
    print(f"\nBacktest running from {master_timeline[0].date()} to {master_timeline[-1].date()}")

    # --- 4. MAIN BACKTEST LOOP ---
    for current_date in tqdm(master_timeline, desc="Processing Dates"):
        # A. Mark-to-Market and count open positions
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

            if pd.isna(daily_data['z_score']) or pd.isna(daily_data['hedge_ratio']):
                continue

            # --- C. EXIT LOGIC ---
            if position:
                exit_signal, exit_reason = False, ""
                days_held = (current_date.date() - position['entry_date']).days
                
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
                    pnl = (exit_s1 + exit_s2) - position['entry_value']
                    pnl_comm = pnl - position['entry_commission'] - exit_comm
                    
                    trade_details = {
                        'pair': pair_name, 'entry_date': position['entry_date'],
                        'exit_date': current_date.date(), 'days_held': days_held,
                        'exit_reason': exit_reason, 'pnl': pnl, 'pnlcomm': pnl_comm,
                    }
                    entry_features = {col: position['entry_features'].get(col, np.nan) for col in FEATURE_COLUMNS}
                    trade_details.update(entry_features)
                    closed_trades.append(trade_details)
                    
                    portfolio['positions'][pair_name] = {}

            # --- D. ENTRY LOGIC ---
            elif open_positions < MAX_CONCURRENT_PAIRS:
                trade_type = None
                if daily_data['z_score'] < -ENTRY_Z_SCORE: trade_type = "LONG"
                elif daily_data['z_score'] > ENTRY_Z_SCORE: trade_type = "SHORT"
                
                if trade_type:
                    try:
                        # ** SYNCHRONIZED SIZING LOGIC **
                        size_s1 = (capital_per_trade * 0.5) / daily_data['stock1_close']
                        if trade_type == 'SHORT': size_s1 *= -1
                        
                        size_s2 = -size_s1 * daily_data['hedge_ratio']
                        entry_s1 = size_s1 * daily_data['stock1_close']
                        entry_s2 = size_s2 * daily_data['stock2_close']
                        entry_comm = (abs(entry_s1) + abs(entry_s2)) * COMMISSION_RATE
                        
                        portfolio['cash'] -= (entry_s1 + entry_s2 + entry_comm)
                        
                        portfolio['positions'][pair_name] = {
                            'type': trade_type, 'entry_date': current_date.date(),
                            'size_s1': size_s1, 'size_s2': size_s2,
                            'entry_value': entry_s1 + entry_s2,
                            'entry_commission': entry_comm,
                            'entry_features': {col: daily_data.get(col, np.nan) for col in FEATURE_COLUMNS}
                        }
                        open_positions += 1
                    except Exception as e:
                        print(f"Entry error for {pair_name} on {current_date.date()}: {str(e)}")

    # --- 5. FINAL CLEANUP & RESULTS ---
    print("Closing any remaining open positions...")
    last_day = master_timeline[-1]
    for pair_name, position in portfolio['positions'].items():
        if position:
            try:
                last_data = all_pairs_data[pair_name].iloc[-1]
                exit_s1 = position['size_s1'] * last_data['stock1_close']
                exit_s2 = position['size_s2'] * last_data['stock2_close']
                exit_comm = (abs(exit_s1) + abs(exit_s2)) * COMMISSION_RATE
                
                # ** SYNCHRONIZED FINAL CASH UPDATE **
                portfolio['cash'] += (exit_s1 + exit_s2 - exit_comm)

                pnl = (exit_s1 + exit_s2) - position['entry_value']
                pnl_comm = pnl - position['entry_commission'] - exit_comm
                
                trade_details = {
                    'pair': pair_name, 'entry_date': position['entry_date'],
                    'exit_date': last_day.date(), 'days_held': (last_day.date() - position['entry_date']).days,
                    'exit_reason': "End of Backtest", 'pnl': pnl, 'pnlcomm': pnl_comm,
                }
                entry_features = {col: position['entry_features'].get(col, np.nan) for col in FEATURE_COLUMNS}
                trade_details.update(entry_features)
                closed_trades.append(trade_details)
            except Exception as e:
                print(f"Final exit error for {pair_name}: {str(e)}")

    if closed_trades:
        trades_df = pd.DataFrame(closed_trades)
        trades_df.to_csv(OUTPUT_FILENAME, index=False)
        
        # ** SYNCHRONIZED FINAL VALUE CALCULATION **
        final_value = portfolio['cash']
        total_return = (final_value - INITIAL_CAPITAL) / INITIAL_CAPITAL * 100
        win_rate = (trades_df['pnlcomm'] > 0).mean() if not trades_df.empty else 0
        
        print("\n" + "="*50)
        print("ML BACKTEST RESULTS (FULLY SYNCHRONIZED)")
        print(f"Final Portfolio Value: ${final_value:,.2f}")
        print(f"Total Return: {total_return:.2f}%")
        print(f"Total Trades: {len(trades_df)}")
        print(f"Win Rate: {win_rate:.2%}")
        print(f"Results saved to {OUTPUT_FILENAME}")
        print("="*50)
    else:
        print("\nNo trades were executed during the backtest.")

if __name__ == '__main__':
    generate_ml_training_data()
