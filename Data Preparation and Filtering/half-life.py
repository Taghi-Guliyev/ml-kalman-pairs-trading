import pandas as pd
import numpy as np
import glob
import os
from statsmodels.tsa.stattools import coint
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
    
    print(f"Found {len(csv_files)} data files to merge for the analysis.")
    df_list = [pd.read_csv(f, index_col='datetime', parse_dates=True) for f in sorted(csv_files)]
    
    combined_df = pd.concat(df_list, axis=1)
    combined_df.index = pd.to_datetime(combined_df.index).tz_localize(None).normalize()
    
    print(f"Successfully combined all price data. DataFrame shape: {combined_df.shape}")
    return combined_df

def calculate_half_life(spread_series):
    """
    Calculates the half-life of mean reversion for a given time series.
    This is done by modeling the spread as an Ornstein-Uhlenbeck process.
    """
    # Create a lagged version of the spread
    lagged_spread = spread_series.shift(1).dropna()
    
    # Calculate the change in the spread
    delta_spread = spread_series.diff().dropna()
    
    # The regression requires the series to be aligned, so we take the intersection of indices
    aligned_lagged = lagged_spread[delta_spread.index]
    
    # Run the regression: delta_spread = lambda * lagged_spread
    # We add a constant (intercept) to the regression
    model = sm.OLS(delta_spread, sm.add_constant(aligned_lagged))
    result = model.fit()
    
    # The mean-reversion speed is the coefficient 'lambda'
    lambda_coeff = result.params.iloc[1]
    
    # The half-life is calculated as -log(2) / lambda
    # We only care about mean-reverting pairs, so lambda must be negative
    if lambda_coeff < 0:
        half_life = -np.log(2) / lambda_coeff
        return half_life
    else:
        # If lambda is positive, the series is momentum-driven, not mean-reverting
        return np.inf


def filter_pairs_by_half_life(price_data, cointegrated_pairs_file='cointegrated_pairs.csv', max_half_life=63):
    """
    Loads cointegrated pairs and filters them based on their mean-reversion half-life.
    
    Args:
        price_data (pd.DataFrame): DataFrame of all stock prices.
        cointegrated_pairs_file (str): Path to the cointegrated pairs CSV.
        max_half_life (int): Maximum half-life in days to be considered a good pair.

    Returns:
        pd.DataFrame: A filtered DataFrame of pairs with their p-value and half-life.
    """
    try:
        pairs_df = pd.read_csv(cointegrated_pairs_file)
        print(f"\nLoaded {len(pairs_df)} cointegrated pairs to filter by half-life.")
    except FileNotFoundError:
        print(f"Error: The file '{cointegrated_pairs_file}' was not found.")
        return None

    final_candidates = []

    print(f"Calculating half-life for each pair and filtering for < {max_half_life} days...")
    for index, row in tqdm(pairs_df.iterrows(), total=pairs_df.shape[0], desc="Calculating Half-Life"):
        pair = row['Pair']
        p_value = row['p-value']
        
        try:
            stock1_ticker, stock2_ticker = pair.split('-')
            
            # Get price series and align them by dropping NaNs
            combined_prices = price_data[[stock1_ticker, stock2_ticker]].dropna()
            
            if len(combined_prices) > 100:
                series1 = combined_prices[stock1_ticker]
                series2 = combined_prices[stock2_ticker]
                
                # Calculate the spread using a simple linear regression (OLS)
                # This gives us the hedge ratio (beta)
                model = sm.OLS(series1, sm.add_constant(series2))
                result = model.fit()
                beta = result.params.iloc[1]
                spread = series1 - beta * series2
                
                # Calculate the half-life of this spread
                half_life = calculate_half_life(spread)
                
                # Keep the pair if it has a reasonable half-life
                if 1 < half_life < max_half_life:
                    final_candidates.append({
                        'Pair': pair,
                        'p-value': p_value,
                        'Half-Life (days)': half_life
                    })
        except Exception:
            # Silently ignore pairs that cause errors (e.g., missing data)
            pass

    if not final_candidates:
        print("\nNo pairs met the half-life criteria.")
        return pd.DataFrame(columns=['Pair', 'p-value', 'Half-Life (days)'])

    print(f"\nFound {len(final_candidates)} final candidate pairs with a reasonable half-life!")
    return pd.DataFrame(final_candidates)

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Load and combine all price data
    all_prices_df = combine_price_files()
    
    if all_prices_df is not None:
        # 2. Filter the cointegrated pairs by their half-life
        final_pairs_df = filter_pairs_by_half_life(all_prices_df)
        
        if final_pairs_df is not None and not final_pairs_df.empty:
            # 3. Sort by Half-Life to see the fastest-reverting pairs first
            final_pairs_df.sort_values('Half-Life (days)', inplace=True)
            
            # 4. Export the final list to a new CSV
            output_filename = 'final_candidate_pairs.csv'
            final_pairs_df.to_csv(output_filename, index=False)
            print(f"Successfully exported the final list of candidate pairs to '{output_filename}'.")
