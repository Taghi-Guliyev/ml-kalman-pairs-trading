import pandas as pd
import numpy as np
import os
import glob
from tqdm import tqdm

def run_kalman_backtest():
    """
    Runs a portfolio-level Kalman Filter pairs trading backtest from pre-processed CSV files
    with proper capital, leverage, and risk management.
    """
    # --- 1. CONFIGURATION ---
    DATA_DIR = 'kalman_signal_data'  # Use the Kalman data directory
    OUTPUT_FILENAME = 'detailed_trades_kalman.csv'
    INITIAL_CAPITAL = 1_000_000.00
    COMMISSION_RATE = 0.001
    
    # Strategy Parameters
    ENTRY_Z_SCORE = 3  # Use a slightly higher threshold for entry to filter noise
    EXIT_Z_SCORE = 0.5   # Use hysteresis to prevent exiting on minor flickers
    MAX_CONCURRENT_PAIRS = 10
    MAX_HOLD_DAYS = 150 # Time-based stop loss: exit any trade held longer than 60 days

    # --- 2. DATA LOADING ---
    all_pairs_data = {}
    data_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    if not data_files:
        print(f"FATAL: No data files found in the '{DATA_DIR}' directory. Exiting.")
        return

    print(f"Loading {len(data_files)} pair data files...")
    for file_path in data_files:
        pair_name = os.path.basename(file_path).replace('.csv', '')
        df = pd.read_csv(file_path, index_col='datetime', parse_dates=True)
        all_pairs_data[pair_name] = df

    # --- 3. SETUP PORTFOLIO & TIMELINE ---
    portfolio = {
        'cash': INITIAL_CAPITAL,
        'total_value': INITIAL_CAPITAL,
        'positions': {pair: {} for pair in all_pairs_data.keys()}
    }
    closed_trades = []
    master_timeline = sorted(list(set.union(*[set(df.index) for df in all_pairs_data.values()])))
    print(f"Backtest will run from {master_timeline[0].date()} to {master_timeline[-1].date()}.")

    # --- 4. MAIN BACKTESTING LOOP ---
    for current_date in tqdm(master_timeline, desc="Running Kalman Backtest"):
        
        # Mark-to-Market: Update portfolio value and count open positions
        current_portfolio_value = portfolio['cash']
        open_positions_count = 0
        for pair_name, position in portfolio['positions'].items():
            if position:
                open_positions_count += 1
                try:
                    latest_price_s1 = all_pairs_data[pair_name].loc[current_date, 'stock1_close']
                    latest_price_s2 = all_pairs_data[pair_name].loc[current_date, 'stock2_close']
                    value_s1 = position['size_s1'] * latest_price_s1
                    value_s2 = position['size_s2'] * latest_price_s2
                    current_portfolio_value += (value_s1 + value_s2)
                except KeyError:
                    current_portfolio_value += position.get('entry_value', 0)
        portfolio['total_value'] = current_portfolio_value

        capital_per_trade = portfolio['total_value'] / MAX_CONCURRENT_PAIRS

        for pair_name, pair_df in all_pairs_data.items():
            if current_date not in pair_df.index:
                continue

            # Get daily data, including the dynamic hedge_ratio
            z_score = pair_df.loc[current_date, 'z_score']
            price_s1 = pair_df.loc[current_date, 'stock1_close']
            price_s2 = pair_df.loc[current_date, 'stock2_close']
            hedge_ratio = pair_df.loc[current_date, 'hedge_ratio']
            position = portfolio['positions'][pair_name]

            # Skip day if Z-score is NaN (due to rolling window at the start)
            if np.isnan(z_score):
                continue

            # --- EXIT LOGIC ---
            if position:
                exit_signal = False
                exit_reason = ""
                
                # Reason 1: Z-score reversion
                if position['type'] == 'LONG' and z_score >= -EXIT_Z_SCORE:
                    exit_signal, exit_reason = True, "Z-Score Reversion"
                elif position['type'] == 'SHORT' and z_score <= EXIT_Z_SCORE:
                    exit_signal, exit_reason = True, "Z-Score Reversion"
                
                # Reason 2: Time-based stop loss
                days_held = (current_date.date() - position['entry_date']).days
                if days_held > MAX_HOLD_DAYS:
                    exit_signal, exit_reason = True, "Time Stop Loss"

                if exit_signal:
                    exit_value_s1 = position['size_s1'] * price_s1
                    exit_value_s2 = position['size_s2'] * price_s2
                    exit_commission = (abs(exit_value_s1) + abs(exit_value_s2)) * COMMISSION_RATE
                    portfolio['cash'] += (exit_value_s1 + exit_value_s2 - exit_commission)
                    pnl = (exit_value_s1 + exit_value_s2) - position['entry_value']
                    pnl_comm = pnl - position['entry_commission'] - exit_commission
                    closed_trades.append({
                        'pair': pair_name, 'entry_date': position['entry_date'],
                        'exit_date': current_date.date(), 'days_held': days_held, 'exit_reason': exit_reason,
                        'pnl': pnl, 'pnlcomm': pnl_comm, 'size_s1': position['size_s1'],
                        'entry_price_s1': position['entry_price_s1'], 'exit_price_s1': price_s1,
                        'size_s2': position['size_s2'], 'entry_price_s2': position['entry_price_s2'],
                        'exit_price_s2': price_s2,
                    })
                    portfolio['positions'][pair_name] = {}
            
            # --- ENTRY LOGIC ---
            else:
                if open_positions_count < MAX_CONCURRENT_PAIRS:
                    trade_opened = False
                    # Long entry: Buy S1, Sell S2
                    if z_score < -ENTRY_Z_SCORE:
                        # Use Beta-hedging for position size
                        size_s1 = (capital_per_trade * 0.5) / price_s1
                        size_s2 = -size_s1 * hedge_ratio
                        trade_type = 'LONG'
                        trade_opened = True
                    # Short entry: Sell S1, Buy S2
                    elif z_score > ENTRY_Z_SCORE:
                        # Use Beta-hedging for position size
                        size_s1 = -(capital_per_trade * 0.5) / price_s1
                        size_s2 = -size_s1 * hedge_ratio
                        trade_type = 'SHORT'
                        trade_opened = True
                    
                    if trade_opened:
                        entry_value_s1 = size_s1 * price_s1
                        entry_value_s2 = size_s2 * price_s2
                        entry_commission = (abs(entry_value_s1) + abs(entry_value_s2)) * COMMISSION_RATE
                        portfolio['cash'] -= (entry_value_s1 + entry_value_s2 + entry_commission)
                        portfolio['positions'][pair_name] = {
                            'type': trade_type, 'entry_date': current_date.date(),
                            'size_s1': size_s1, 'entry_price_s1': price_s1,
                            'size_s2': size_s2, 'entry_price_s2': price_s2,
                            'entry_value': entry_value_s1 + entry_value_s2,
                            'entry_commission': entry_commission
                        }
                        open_positions_count += 1

    # --- 5. FINALIZE & SAVE RESULTS ---
    print("Closing any remaining open positions...")
    for pair_name, position in portfolio['positions'].items():
        if position:
            pair_df = all_pairs_data[pair_name]
            if not pair_df.empty:
                final_pair_date = pair_df.index[-1]
                try:
                    price_s1 = pair_df.loc[final_pair_date, 'stock1_close']
                    price_s2 = pair_df.loc[final_pair_date, 'stock2_close']
                    exit_value_s1 = position['size_s1'] * price_s1
                    exit_value_s2 = position['size_s2'] * price_s2
                    exit_commission = (abs(exit_value_s1) + abs(exit_value_s2)) * COMMISSION_RATE
                    portfolio['cash'] += (exit_value_s1 + exit_value_s2 - exit_commission)
                    pnl = (exit_value_s1 + exit_value_s2) - position['entry_value']
                    pnl_comm = pnl - position['entry_commission'] - exit_commission
                    closed_trades.append({
                        'pair': pair_name, 'entry_date': position['entry_date'], 'exit_date': final_pair_date.date(),
                        'days_held': (final_pair_date.date() - position['entry_date']).days, 'exit_reason': 'End of Backtest',
                        'pnl': pnl, 'pnlcomm': pnl_comm,
                        'size_s1': position['size_s1'], 'entry_price_s1': position['entry_price_s1'], 'exit_price_s1': price_s1,
                        'size_s2': position['size_s2'], 'entry_price_s2': position['entry_price_s2'], 'exit_price_s2': price_s2,
                    })
                except KeyError:
                    print(f"Warning: Could not find final price for {pair_name} on {final_pair_date}.")

    # --- 6. DISPLAY SUMMARY ---
    trades_df = pd.DataFrame(closed_trades)
    trades_df.to_csv(OUTPUT_FILENAME, index=False)
    
    final_value = portfolio['cash']
    total_return = (final_value - INITIAL_CAPITAL) / INITIAL_CAPITAL * 100
    print("\n" + "="*50)
    print("KALMAN BACKTEST COMPLETE")
    print(f"Final Portfolio Value: ${final_value:,.2f}")
    print(f"Total Return: {total_return:.2f}%")
    print(f"Total Trades Closed: {len(trades_df)}")
    print(f"Trade log saved to '{OUTPUT_FILENAME}'")
    print("="*50)

if __name__ == '__main__':
    run_kalman_backtest()
