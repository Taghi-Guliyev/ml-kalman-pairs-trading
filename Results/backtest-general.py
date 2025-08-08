import pandas as pd
import quantstats as qs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import warnings
import os
import glob

warnings.filterwarnings("ignore")

# --- DATA LOADING FUNCTIONS ---

def combine_price_files(path=".", start_date=None, end_date=None):
    """Finds and merges all 'sp500_prices_*.csv' files."""
    csv_files = glob.glob(os.path.join(path, "sp500_prices_*.csv"))
    if not csv_files:
        print("Error: No 'sp500_prices_*.csv' files found.")
        return None
    
    df_list = [pd.read_csv(f, index_col='datetime', parse_dates=True) for f in sorted(csv_files)]
    
    combined_df = pd.concat(df_list, axis=1)
    combined_df.index = pd.to_datetime(combined_df.index).tz_localize(None).normalize()
    
    combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]
    
    if start_date and end_date:
        combined_df = combined_df.loc[start_date:end_date]
        
    print(f"Successfully combined local price data. Shape: {combined_df.shape}")
    return combined_df

def load_and_process_tradelog(filename):
    """Loads the trade log and prepares it for analysis."""
    try:
        df = pd.read_csv(filename)
        print(f"Successfully loaded '{filename}' with {len(df)} trades.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

    df.dropna(subset=['entry_date', 'exit_date'], inplace=True)
    df['entry_date'] = pd.to_datetime(df['entry_date'])
    df['exit_date'] = pd.to_datetime(df['exit_date'])
    df['pnlcomm'] = pd.to_numeric(df['pnlcomm'])
    return df

# --- CALCULATION FUNCTIONS ---

def calculate_daily_returns(tradelog_df, initial_capital=1_000_000):
    """Converts a trade log into a daily returns series."""
    if tradelog_df.empty:
        return pd.Series(dtype=float), pd.Series(dtype=float)

    start_date = tradelog_df['entry_date'].min()
    end_date = tradelog_df['exit_date'].max()
    
    if pd.isna(start_date) or pd.isna(end_date):
        return pd.Series(dtype=float), pd.Series(dtype=float)

    date_range = pd.date_range(start=start_date, end=end_date, freq='B')
    daily_pnl = pd.Series(0.0, index=date_range)
    
    pnl_by_date = tradelog_df.groupby('exit_date')['pnlcomm'].sum()
    daily_pnl.update(pnl_by_date)
    
    cumulative_pnl = daily_pnl.cumsum()
    equity_curve = initial_capital + cumulative_pnl
    daily_returns = equity_curve.pct_change().fillna(0)
    
    return daily_returns, equity_curve

def calculate_benchmark_return(tradelog_df, all_prices_df, start_date, end_date):
    """Calculates the best performing stock's Buy & Hold return from local data."""
    tickers = set()
    for pair in tradelog_df['pair'].unique():
        if isinstance(pair, str) and '-' in pair:
            tickers.update(pair.split('-'))
        else:
            tickers.add(pair)
            
    valid_tickers = [t for t in tickers if t in all_prices_df.columns]
    if not valid_tickers:
        print("Could not calculate benchmark return; no valid tickers found in price data.")
        return "N/A", 0.0
        
    prices = all_prices_df.loc[start_date:end_date, valid_tickers]
    
    prices = prices.dropna(axis=1, how='any', subset=[prices.index[0], prices.index[-1]])
    if prices.empty:
        print("Could not calculate benchmark return; no valid price data for the period.")
        return "N/A", 0.0
        
    performance = (prices.iloc[-1] / prices.iloc[0]) - 1
    
    best_performer = performance.idxmax()
    best_return = performance.max()
    
    print(f"\nBenchmark: Best performing stock was {best_performer} with a return of {best_return:.2%}")
    return best_performer, best_return

# --- REPORTING FUNCTION ---

def generate_pdf_report(strategy_name, daily_returns, equity_curve, tradelog_df, benchmark_return_info):
    """Generates a multi-page PDF report with metrics and charts."""
    best_performer_name, benchmark_return = benchmark_return_info
    output_filename = f"{strategy_name.lower().replace(' ', '_')}_performance_report.pdf"
    
    def safe_float(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0

    metrics = qs.reports.metrics(daily_returns, mode='full', display=False)
    
    win_rate = (tradelog_df['pnlcomm'] > 0).mean() if not tradelog_df.empty else 0
    avg_win = tradelog_df[tradelog_df['pnlcomm'] > 0]['pnlcomm'].mean() if not tradelog_df.empty else 0
    avg_loss = tradelog_df[tradelog_df['pnlcomm'] < 0]['pnlcomm'].mean() if not tradelog_df.empty else 0
    expected_value = (win_rate * avg_win) + ((1 - win_rate) * avg_loss) if not tradelog_df.empty else 0
    
    report_df = pd.DataFrame(index=[
        'Start Period', 'End Period', 'Risk-Free Rate (%)',
        'Compounded Return (%)', 'Annualized Return (%)', 'Best Stock B&H Return (%)',
        'Sharpe Ratio (4% RF)', 'Sortino Ratio (4% RF)',
        'Max Drawdown (%)', 'Avg. Drawdown (%)',
        'Win Rate (%)', 'Avg. Win ($)', 'Avg. Loss ($)', 'Expected Value ($)'
    ], columns=['Value'])
    
    report_df.loc['Start Period'] = daily_returns.index.min().strftime('%Y-%m-%d')
    report_df.loc['End Period'] = daily_returns.index.max().strftime('%Y-%m-%d')
    report_df.loc['Risk-Free Rate (%)'] = "4.00"
    report_df.loc['Compounded Return (%)'] = f"{safe_float(qs.stats.comp(daily_returns)) * 100:.2f}"
    report_df.loc['Annualized Return (%)'] = f"{safe_float(qs.stats.cagr(daily_returns)) * 100:.2f}"
    report_df.loc['Best Stock B&H Return (%)'] = f"{safe_float(benchmark_return) * 100:.2f} ({best_performer_name})"
    report_df.loc['Sharpe Ratio (4% RF)'] = f"{safe_float(qs.stats.sharpe(daily_returns, rf=0.04)):.2f}"
    report_df.loc['Sortino Ratio (4% RF)'] = f"{safe_float(qs.stats.sortino(daily_returns, rf=0.04)):.2f}"
    
    # --- FIX: Check if the metric exists in the report before trying to access it ---
    max_drawdown = metrics.loc['Max Drawdown'] if 'Max Drawdown' in metrics.index else 0.0
    avg_drawdown = metrics.loc['Avg. Drawdown'] if 'Avg. Drawdown' in metrics.index else 0.0
    
    report_df.loc['Max Drawdown (%)'] = f"{safe_float(max_drawdown):.2f}"
    report_df.loc['Avg. Drawdown (%)'] = f"{safe_float(avg_drawdown):.2f}"
    
    report_df.loc['Win Rate (%)'] = f"{safe_float(win_rate) * 100:.2f}"
    report_df.loc['Avg. Win ($)'] = f"{avg_win:,.2f}"
    report_df.loc['Avg. Loss ($)'] = f"{avg_loss:,.2f}"
    report_df.loc['Expected Value ($)'] = f"{expected_value:,.2f}"
    
    with PdfPages(output_filename) as pdf:
        fig, ax = plt.subplots(figsize=(8, 8)); ax.axis('tight'); ax.axis('off')
        table = ax.table(cellText=report_df.values, rowLabels=report_df.index, colLabels=report_df.columns, loc='center', cellLoc='left')
        table.auto_set_font_size(False); table.set_fontsize(12); table.scale(1.2, 1.2)
        ax.set_title(f"Performance Metrics: {strategy_name}", fontsize=16, pad=20)
        pdf.savefig(fig, bbox_inches='tight'); plt.close()
        
        if not equity_curve.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            equity_curve.plot(ax=ax, grid=True, title=f"Equity Curve: {strategy_name}", lw=2)
            ax.set_ylabel("Portfolio Value ($)"); ax.set_xlabel("Date")
            ax.yaxis.set_major_formatter('{x:,.0f}')
            pdf.savefig(fig, bbox_inches='tight'); plt.close()
        
    print(f"\nSuccessfully generated PDF report: '{output_filename}'")


def main():
    """Main execution function."""
    STRATEGY_NAME = 'ML+Kalman Strategy'
    TRADE_LOG_FILE = 'ml_forward_test_results.csv'
    INITIAL_CAPITAL = 1_000_000
    
    tradelog_df = load_and_process_tradelog(TRADE_LOG_FILE)
    if tradelog_df is None or tradelog_df.empty:
        print("Trade log is empty or could not be loaded. Exiting.")
        return
        
    daily_returns, equity_curve = calculate_daily_returns(tradelog_df, INITIAL_CAPITAL)
    if daily_returns.empty or equity_curve.empty:
        print("Could not calculate daily returns, possibly due to data issues. Exiting analysis.")
        return
    
    print(f"\nAnalyzing trade period from {daily_returns.index.min().date()} to {daily_returns.index.max().date()}")
    
    all_prices_df = combine_price_files()
    if all_prices_df is None:
        print("Could not load price data for benchmark. Exiting.")
        return
        
    bench_info = calculate_benchmark_return(tradelog_df, all_prices_df, daily_returns.index.min(), daily_returns.index.max())
    
    generate_pdf_report(STRATEGY_NAME, daily_returns, equity_curve, tradelog_df, bench_info)

if __name__ == "__main__":
    main()
