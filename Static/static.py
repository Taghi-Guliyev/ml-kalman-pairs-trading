import pandas as pd
import numpy as np
import glob
import os
import statsmodels.api as sm
from tqdm import tqdm

def combine_price_files(path="."):
    """
    Finds all 'sp500_prices_*.csv' files and merges them.
    """
    csv_files = glob.glob(os.path.join(path, "sp500_prices_*.csv"))
    if not csv_files:
        print("Error: No 'sp500_prices_*.csv' files found.")
        return None
    
    df_list = [pd.read_csv(f, index_col='datetime', parse_dates=True) for f in sorted(csv_files)]
    
    combined_df = pd.concat(df_list, axis=1)
    combined_df.index = pd.to_datetime(combined_df.index).tz_localize(None).normalize()
    
    print(f"Successfully combined all price data. DataFrame shape: {combined_df.shape}")
    return combined_df

def prepare_data_for_backtrader(price_data, candidate_pairs_file='final_candidate_pairs.csv'):
    """
    Prepares and saves the data for each pair in a format ready for Backtrader.
    """
    try:
        pairs_df = pd.read_csv(candidate_pairs_file)
        print(f"\nLoaded {len(pairs_df)} candidate pairs to prepare for backtesting.")
    except FileNotFoundError:
        print(f"Error: The file '{candidate_pairs_file}' was not found.")
        return

    output_dir = 'static_backtest_data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"Data for backtesting will be saved in the '{output_dir}/' directory.")

    train_start_date = '2023-07-31'
    train_end_date = '2024-07-31'
    test_start_date = '2024-07-31'
    test_end_date = '2025-07-31' 

    for index, row in tqdm(pairs_df.iterrows(), total=pairs_df.shape[0], desc="Preparing Data for Backtrader"):
        pair_name = row['Pair']
        
        try:
            stock1_ticker, stock2_ticker = pair_name.split('-')
            pair_prices = price_data[[stock1_ticker, stock2_ticker]].dropna()
            
            train_data = pair_prices.loc[train_start_date:train_end_date]
            test_data = pair_prices.loc[test_start_date:test_end_date]

            if train_data.empty or test_data.empty or len(train_data) < 200:
                continue

            model = sm.OLS(train_data[stock1_ticker], sm.add_constant(train_data[stock2_ticker]))
            result = model.fit()
            static_beta = result.params.iloc[1]

            spread = test_data[stock1_ticker] - static_beta * test_data[stock2_ticker]
            train_spread = train_data[stock1_ticker] - static_beta * train_data[stock2_ticker]
            spread_mean_train = train_spread.mean()
            spread_std_train = train_spread.std()
            
            z_score = (spread - spread_mean_train) / spread_std_train
            
            backtrader_df = test_data.copy()
            backtrader_df.rename(columns={stock1_ticker: 'stock1_close', stock2_ticker: 'stock2_close'}, inplace=True)
            backtrader_df['z_score'] = z_score
            backtrader_df['hedge_ratio'] = static_beta
            
            
            # We can just use one of the stock's prices; its value doesn't matter, its presence does.
            backtrader_df['close'] = backtrader_df['stock1_close']
            
            output_filename = os.path.join(output_dir, f"{pair_name}.csv")
            backtrader_df.to_csv(output_filename)

        except Exception:
            continue
            
    print(f"\nData preparation complete. All files saved in '{output_dir}/'.")

# --- Main Execution ---
if __name__ == "__main__":
    all_prices_df = combine_price_files()
    
    if all_prices_df is not None:
        prepare_data_for_backtrader(all_prices_df)
