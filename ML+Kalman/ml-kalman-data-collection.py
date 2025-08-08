import pandas as pd
import numpy as np
import glob
import os
from pykalman import KalmanFilter
from tqdm import tqdm
import talib
import warnings

# Configuration
warnings.filterwarnings("ignore")
CALC_START = '2019-09-01'
TEST_START = '2020-01-01' 
TEST_END = '2025-07-31'
MIN_DATA_POINTS = 100
Z_SCORE_WINDOW = 60

def load_and_clean_prices(path="."):
    """Load and merge price files with strict quality control"""
    files = glob.glob(os.path.join(path, "sp500_prices_*.csv"))
    if not files:
        raise FileNotFoundError("No price files found")
    
    # Read with consistent datetime handling
    dfs = []
    for f in sorted(files):
        df = pd.read_csv(f, index_col='datetime', parse_dates=True)
        df.index = pd.to_datetime(df.index).tz_localize(None).normalize()
        dfs.append(df)
    
    # Concatenate with duplicate protection
    prices = pd.concat(dfs, axis=1)
    prices = prices.loc[~prices.index.duplicated(keep='first')]
    prices = prices.loc[:, ~prices.columns.duplicated()]
    return prices

def calculate_kalman_signals(prices, ticker1, ticker2):
    """Pure Kalman implementation without any feature additions"""
    # Get clean price data
    pair_data = prices.loc[CALC_START:TEST_END, [ticker1, ticker2]].dropna()
    if len(pair_data) < MIN_DATA_POINTS:
        return None
    
    # Kalman Filter Setup
    kf = KalmanFilter(
        n_dim_state=2,
        n_dim_obs=1,
        initial_state_mean=np.zeros(2),
        initial_state_covariance=np.ones((2, 2)),
        transition_matrices=np.eye(2),
        observation_matrices=np.vstack([
            pair_data[ticker2].values, 
            np.ones(len(pair_data))
        ]).T[:, np.newaxis, :],
        observation_covariance=0.1,
        transition_covariance=1e-11 * np.eye(2)
    )
    
    # Run Filter
    state_means, _ = kf.filter(pair_data[ticker1].values)
    
    # Calculate Spread and Z-Score
    spread = pair_data[ticker1] - (state_means[:, 0] * pair_data[ticker2])
    z_score = (spread - spread.rolling(Z_SCORE_WINDOW).mean()) / spread.rolling(Z_SCORE_WINDOW).std()
    
    # Create output DataFrame
    signals = pd.DataFrame({
        'stock1_close': pair_data[ticker1],
        'stock2_close': pair_data[ticker2],
        'z_score': z_score,
        'hedge_ratio': state_means[:, 0]
    }, index=pair_data.index)
    
    return signals.loc[TEST_START:TEST_END]

def add_ml_features(signals, prices, ticker1, ticker2):
    """Add technical indicators without modifying core signals"""
    if signals is None or len(signals) == 0:
        return None
    
    features = signals.copy()
    spread = features['stock1_close'] - (features['hedge_ratio'] * features['stock2_close'])
    
    # Technical Indicators - Stock 1
    features['rsi1'] = talib.RSI(features['stock1_close'])
    features['atr1_norm'] = talib.ATR(
        features['stock1_close'], features['stock1_close'], features['stock1_close'], 14
    ) / features['stock1_close']
    features['ema_dist1'] = (features['stock1_close'] / talib.EMA(features['stock1_close'], 20)) - 1
    macd1, macdsignal1, _ = talib.MACD(features['stock1_close'])
    features['macd1'] = macd1 - macdsignal1
    
    # Technical Indicators - Stock 2
    features['rsi2'] = talib.RSI(features['stock2_close'])
    features['atr2_norm'] = talib.ATR(
        features['stock2_close'], features['stock2_close'], features['stock2_close'], 14
    ) / features['stock2_close']
    features['ema_dist2'] = (features['stock2_close'] / talib.EMA(features['stock2_close'], 20)) - 1
    macd2, macdsignal2, _ = talib.MACD(features['stock2_close'])
    features['macd2'] = macd2 - macdsignal2
    
    # Spread Features
    features['spread_volatility'] = spread.diff().abs().rolling(30).std().shift(1)
    features['spread_ma_ratio'] = spread / spread.rolling(60).mean().shift(1)
    features['spread_momentum'] = spread - spread.shift(5)
    
    # Correlation
    full_prices = prices.loc[CALC_START:TEST_END, [ticker1, ticker2]].dropna()
    features['corr_30d'] = full_prices[ticker1].rolling(30).corr(full_prices[ticker2]).shift(1)
    
    return features

def generate_signals(price_path=".", pairs_file='final_candidate_pairs.csv'):
    """Complete signal generation pipeline"""
    # Load data
    prices = load_and_clean_prices(price_path)
    pairs = pd.read_csv(pairs_file)
    
    # Create output directories
    os.makedirs("kalman_signal_features", exist_ok=True)
    
    # Process each pair
    for _, row in tqdm(pairs.iterrows(), total=len(pairs)):
        t1, t2 = row['Pair'].split('-')
        
        try:
            # 1. Calculate core Kalman signals
            kalman = calculate_kalman_signals(prices, t1, t2)
            if kalman is None:
                continue
                
            # 2. Add ML features
            ml = add_ml_features(kalman.copy(), prices, t1, t2)
            if ml is not None:
                ml.to_csv(f"kalman_signal_features/{row['Pair']}.csv")
                
        except Exception as e:
            print(f"Skipping {row['Pair']}: {str(e)}")
            continue

if __name__ == "__main__":
    generate_signals()