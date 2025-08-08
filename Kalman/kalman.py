import pandas as pd
import numpy as np
import glob
import os
from pykalman import KalmanFilter
from tqdm import tqdm

def combine_price_files(path="."):
    """
    Finds all 'sp500_prices_*.csv' files, merges them, and cleans the data.
    """
    csv_files = glob.glob(os.path.join(path, "sp500_prices_*.csv"))
    if not csv_files:
        print("Error: No 'sp500_prices_*.csv' files found in the current directory.")
        return None
    
    df_list = [pd.read_csv(f, index_col='datetime', parse_dates=True) for f in sorted(csv_files)]
    
    combined_df = pd.concat(df_list, axis=1)
    
    combined_df.index = pd.to_datetime(combined_df.index).tz_localize(None).normalize()
    
    combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]
    
    print(f"Successfully combined all price data. DataFrame shape: {combined_df.shape}")
    return combined_df

def generate_kalman_signals(price_data, candidate_pairs_file='final_candidate_pairs.csv'):
    """
    Runs the Kalman Filter for all candidate pairs, using a defined warm-up period
    to speed up calculations and save signals for the specified backtest period.
    """
    try:
        pairs_df = pd.read_csv(candidate_pairs_file)
        print(f"\nLoaded {len(pairs_df)} candidate pairs to process.")
    except FileNotFoundError:
        print(f"Error: The file '{candidate_pairs_file}' was not found.")
        return

    output_dir = "kalman_signal_data"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Daily signal files for the backtest will be saved in the '{output_dir}/' directory.")
    
    # Define the date ranges
    calculation_start_date = '2023-07-31' # Start of the warm-up period
    test_start_date = '2024-07-31'        # Start of the actual backtest
    test_end_date = '2025-07-31'          # End of the backtest

    # Kalman Filter parameters (using the previously optimized settings)
    transition_covariance = 1e-11 * np.eye(2)
    observation_covariance = 0.1

    for index, row in tqdm(pairs_df.iterrows(), total=pairs_df.shape[0], desc="Generating Kalman Signals"):
        pair_name = row['Pair']
        
        try:
            stock1_ticker, stock2_ticker = pair_name.split('-')
            
            if not all(ticker in price_data.columns for ticker in [stock1_ticker, stock2_ticker]):
                continue
            
            pair_prices = price_data.loc[calculation_start_date:test_end_date, [stock1_ticker, stock2_ticker]].dropna()
            
            if len(pair_prices) < 100:
                continue

            # --- Kalman Filter and Signal Calculation (now runs on a smaller dataset) ---
            observations = pair_prices[stock1_ticker].values
            observation_matrix = np.vstack([
                pair_prices[stock2_ticker].values, 
                np.ones(len(pair_prices))
            ]).T[:, np.newaxis, :]

            kf = KalmanFilter(
                n_dim_state=2, n_dim_obs=1,
                initial_state_mean=np.zeros(2),
                initial_state_covariance=np.ones((2, 2)),
                transition_matrices=np.eye(2),
                observation_matrices=observation_matrix,
                observation_covariance=observation_covariance,
                transition_covariance=transition_covariance
            )
            
            state_means, _ = kf.filter(observations)
            
            dynamic_estimates = pd.DataFrame({
                'beta': state_means[:, 0],
                'alpha': state_means[:, 1]
            }, index=pair_prices.index)

            dynamic_spread = pair_prices[stock1_ticker] - (dynamic_estimates['beta'] * pair_prices[stock2_ticker])
            rolling_z_score = (dynamic_spread - dynamic_spread.rolling(window=60).mean()) / dynamic_spread.rolling(window=60).std()
            
            # Create the full signal DataFrame
            signal_df = pd.DataFrame(index=pair_prices.index)
            signal_df['stock1_close'] = pair_prices[stock1_ticker]
            signal_df['stock2_close'] = pair_prices[stock2_ticker]
            signal_df['z_score'] = rolling_z_score
            signal_df['hedge_ratio'] = dynamic_estimates['beta']
            
            final_signal_df = signal_df.loc[test_start_date:test_end_date]
            
            if not final_signal_df.empty:
                final_signal_df.to_csv(os.path.join(output_dir, f"{pair_name}.csv"))

        except Exception:
            continue

    print(f"\nDaily signal generation complete. All files saved in '{output_dir}/'.")


if __name__ == "__main__":
    # 1. Combine all available price files into one large DataFrame
    all_prices_df = combine_price_files()
    
    # 2. If prices are loaded, generate the Kalman signal files for backtesting
    if all_prices_df is not None:
        generate_kalman_signals(all_prices_df)