import pandas as pd
import numpy as np
import glob
import os
from statsmodels.tsa.stattools import coint
from tqdm import tqdm

def combine_price_files(path="."):
    """
    Finds all 'sp500_prices_*.csv' files in the specified path,
    loads them, and merges them into a single DataFrame.

    Returns:
        pd.DataFrame: A single DataFrame with all stock price data,
                      or None if no files are found.
    """
    # Use glob to find all files matching the pattern
    csv_files = glob.glob(os.path.join(path, "sp500_prices_*.csv"))
    
    if not csv_files:
        print("Error: No 'sp500_prices_*.csv' files found in the current directory.")
        print("Please make sure the script is in the same folder as your CSV files.")
        return None

    print(f"Found {len(csv_files)} data files to merge.")
    
    # List to hold all the individual DataFrames
    df_list = []
    
    for filename in sorted(csv_files):
        try:
            # Read each CSV, setting the first column ('datetime') as the index
            # and parsing it as a date. This is crucial for proper alignment.
            df = pd.read_csv(filename, index_col='datetime', parse_dates=True)
            df_list.append(df)
            print(f"Successfully loaded: {filename}")
        except Exception as e:
            print(f"Could not read {filename}. Error: {e}")
            
    if not df_list:
        print("No dataframes were loaded. Exiting.")
        return None

    # Concatenate all DataFrames in the list.
    # axis=1 merges them horizontally, aligning on the datetime index.
    combined_df = pd.concat(df_list, axis=1)
    
    # Ensure the index is a standard DatetimeIndex without timezone for consistency
    combined_df.index = pd.to_datetime(combined_df.index)
    combined_df.index = combined_df.index.tz_localize(None).normalize()
    
    print(f"\nSuccessfully combined all files into a single DataFrame.")
    print(f"Shape of the final DataFrame: {combined_df.shape}")
    
    return combined_df

def find_highly_correlated_pairs(df, threshold=0.8):
    """
    Calculates the correlation matrix for the given DataFrame and
    finds pairs with an absolute correlation above the threshold.

    Args:
        df (pd.DataFrame): DataFrame of stock prices.
        threshold (float): The absolute correlation threshold.

    Returns:
        pd.DataFrame: A DataFrame with one column 'Highly Correlated Pairs'.
    """
    if df is None:
        return None
        
    print(f"\nCalculating correlation matrix for {df.shape[1]} stocks...")
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    print("Filtering for pairs with absolute correlation >", threshold)
    
    # --- THIS IS THE CORRECTED LINE ---
    # Get the upper triangle using np directly and cast to bool
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    
    # Find pairs that meet the threshold
    highly_correlated_pairs = upper_triangle[abs(upper_triangle) > threshold].stack().reset_index()
    highly_correlated_pairs.columns = ['Stock 1', 'Stock 2', 'Correlation']
    
    if highly_correlated_pairs.empty:
        print("No pairs found above the correlation threshold.")
        return pd.DataFrame({'Highly Correlated Pairs': []})

    # Format the output as requested: 'STOCKA-STOCKB'
    formatted_pairs = highly_correlated_pairs.apply(lambda row: f"{row['Stock 1']}-{row['Stock 2']}", axis=1)
    
    print(f"Found {len(formatted_pairs)} highly correlated pairs.")
    
    return pd.DataFrame(formatted_pairs, columns=['Highly Correlated Pairs'])

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Combine all the CSV files
    all_prices_df = combine_price_files()
    
    if all_prices_df is not None:
        # 2. Find the highly correlated pairs
        correlated_pairs_df = find_highly_correlated_pairs(all_prices_df, threshold=0.8)
        
        if correlated_pairs_df is not None:
            # 3. Export the results to a new CSV file
            output_filename = 'highly_correlated_pairs.csv'
            # We don't need the DataFrame index in the output file
            correlated_pairs_df.to_csv(output_filename, index=False)
            print(f"\nSuccessfully exported the list of pairs to '{output_filename}'.")



def find_cointegrated_pairs(price_data, correlated_pairs_file='highly_correlated_pairs.csv'):
    """
    Loads a list of correlated pairs and performs a cointegration test on each one.

    Args:
        price_data (pd.DataFrame): DataFrame containing price history for all stocks.
        correlated_pairs_file (str): The path to the CSV file with correlated pairs.

    Returns:
        pd.DataFrame: A DataFrame of pairs that passed the cointegration test.
    """
    try:
        # Load the list of highly correlated pairs
        pairs_df = pd.read_csv(correlated_pairs_file)
        # Ensure the column is treated as a list of strings
        pairs_to_test = pairs_df['Highly Correlated Pairs'].tolist()
        print(f"\nLoaded {len(pairs_to_test)} correlated pairs to test for cointegration.")
    except FileNotFoundError:
        print(f"Error: The file '{correlated_pairs_file}' was not found.")
        return None

    cointegrated_results = []
    
    # Use tqdm to create a progress bar for the loop
    print("Running Engle-Granger cointegration tests...")
    for pair in tqdm(pairs_to_test, desc="Testing Pairs"):
        try:
            stock1_ticker, stock2_ticker = pair.split('-')
            
            # Get the price series for both stocks
            stock1_prices = price_data[stock1_ticker]
            stock2_prices = price_data[stock2_ticker]
            
            # IMPORTANT: Drop NaN values to align the time series.
            # This handles cases where one stock started trading later than the other.
            combined_prices = pd.concat([stock1_prices, stock2_prices], axis=1).dropna()
            
            # Ensure there's enough overlapping data to run the test
            if len(combined_prices) > 100: # A reasonable minimum period
                series1 = combined_prices[stock1_ticker]
                series2 = combined_prices[stock2_ticker]
                
                # Perform the Engle-Granger cointegration test
                score, p_value, _ = coint(series1, series2)
                
                # Check if the p-value is below our significance threshold
                if p_value < 0.05:
                    cointegrated_results.append({
                        'Pair': pair,
                        'p-value': p_value
                    })
        except KeyError as e:
            # This might happen if a ticker name has an issue
            # print(f"Warning: Could not find ticker {e} in price data. Skipping pair '{pair}'.")
            pass
        except Exception as e:
            # Catch any other potential errors during the test
            # print(f"An error occurred with pair '{pair}': {e}")
            pass
            
    if not cointegrated_results:
        print("\nNo cointegrated pairs found with a p-value < 0.05.")
        return pd.DataFrame(columns=['Pair', 'p-value'])

    print(f"\nFound {len(cointegrated_results)} cointegrated pairs!")
    return pd.DataFrame(cointegrated_results)

# --- Main Execution ---
if __name__ == "__main__":
    if all_prices_df is not None:
        # 2. Run the cointegration tests on the correlated pairs
        cointegrated_pairs_df = find_cointegrated_pairs(all_prices_df)
        
        if cointegrated_pairs_df is not None and not cointegrated_pairs_df.empty:
            # 3. Sort by p-value to see the most statistically significant pairs first
            cointegrated_pairs_df.sort_values('p-value', inplace=True)
            
            # 4. Export the final list to a new CSV file
            output_filename = 'cointegrated_pairs.csv'
            cointegrated_pairs_df.to_csv(output_filename, index=False)
            print(f"Successfully exported the list of cointegrated pairs to '{output_filename}'.")

