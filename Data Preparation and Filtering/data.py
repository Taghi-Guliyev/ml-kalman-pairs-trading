from tvDatafeed import TvDatafeed, Interval
import pandas as pd

# --- Configuration ---
# Initialize the TvDatafeed client
tv = TvDatafeed()

# Data parameters
INTERVAL = Interval.in_daily
N_BARS = 7000

# --- Data Storage ---
# Dictionary to hold the closing prices for each ticker
all_data = {}
failed_tickers = []

# --- Data Download (One Call Per Ticker) ---
# The following section makes an individual API call for each of the 503 tickers.

print("Starting data download... This will take a significant amount of time.")

# Ticker 1: NVDA
try:
    data_nvda = tv.get_hist(symbol='NVDA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_nvda is not None and not data_nvda.empty:
        all_data['NVDA'] = data_nvda['close']
        print("(1/503) Successfully fetched data for NVDA")
    else:
        print("(1/503) No data returned for NVDA. Skipping.")
        failed_tickers.append('NVDA')
except Exception as e:
    print(f"(1/503) Failed to fetch data for NVDA: {e}")
    failed_tickers.append('NVDA')

# Ticker 2: MSFT
try:
    data_msft = tv.get_hist(symbol='MSFT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_msft is not None and not data_msft.empty:
        all_data['MSFT'] = data_msft['close']
        print("(2/503) Successfully fetched data for MSFT")
    else:
        print("(2/503) No data returned for MSFT. Skipping.")
        failed_tickers.append('MSFT')
except Exception as e:
    print(f"(2/503) Failed to fetch data for MSFT: {e}")
    failed_tickers.append('MSFT')

# Ticker 3: AAPL
try:
    data_aapl = tv.get_hist(symbol='AAPL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_aapl is not None and not data_aapl.empty:
        all_data['AAPL'] = data_aapl['close']
        print("(3/503) Successfully fetched data for AAPL")
    else:
        print("(3/503) No data returned for AAPL. Skipping.")
        failed_tickers.append('AAPL')
except Exception as e:
    print(f"(3/503) Failed to fetch data for AAPL: {e}")
    failed_tickers.append('AAPL')

# Ticker 4: AMZN
try:
    data_amzn = tv.get_hist(symbol='AMZN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_amzn is not None and not data_amzn.empty:
        all_data['AMZN'] = data_amzn['close']
        print("(4/503) Successfully fetched data for AMZN")
    else:
        print("(4/503) No data returned for AMZN. Skipping.")
        failed_tickers.append('AMZN')
except Exception as e:
    print(f"(4/503) Failed to fetch data for AMZN: {e}")
    failed_tickers.append('AMZN')

# Ticker 5: META
try:
    data_meta = tv.get_hist(symbol='META', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_meta is not None and not data_meta.empty:
        all_data['META'] = data_meta['close']
        print("(5/503) Successfully fetched data for META")
    else:
        print("(5/503) No data returned for META. Skipping.")
        failed_tickers.append('META')
except Exception as e:
    print(f"(5/503) Failed to fetch data for META: {e}")
    failed_tickers.append('META')

# Ticker 6: AVGO
try:
    data_avgo = tv.get_hist(symbol='AVGO', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_avgo is not None and not data_avgo.empty:
        all_data['AVGO'] = data_avgo['close']
        print("(6/503) Successfully fetched data for AVGO")
    else:
        print("(6/503) No data returned for AVGO. Skipping.")
        failed_tickers.append('AVGO')
except Exception as e:
    print(f"(6/503) Failed to fetch data for AVGO: {e}")
    failed_tickers.append('AVGO')

# Ticker 7: GOOGL
try:
    data_googl = tv.get_hist(symbol='GOOGL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_googl is not None and not data_googl.empty:
        all_data['GOOGL'] = data_googl['close']
        print("(7/503) Successfully fetched data for GOOGL")
    else:
        print("(7/503) No data returned for GOOGL. Skipping.")
        failed_tickers.append('GOOGL')
except Exception as e:
    print(f"(7/503) Failed to fetch data for GOOGL: {e}")
    failed_tickers.append('GOOGL')

# Ticker 8: GOOG
try:
    data_goog = tv.get_hist(symbol='GOOG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_goog is not None and not data_goog.empty:
        all_data['GOOG'] = data_goog['close']
        print("(8/503) Successfully fetched data for GOOG")
    else:
        print("(8/503) No data returned for GOOG. Skipping.")
        failed_tickers.append('GOOG')
except Exception as e:
    print(f"(8/503) Failed to fetch data for GOOG: {e}")
    failed_tickers.append('GOOG')

# Ticker 9: BRK.B
try:
    data_brk_b = tv.get_hist(symbol='BRK.B', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_brk_b is not None and not data_brk_b.empty:
        all_data['BRK.B'] = data_brk_b['close']
        print("(9/503) Successfully fetched data for BRK.B")
    else:
        print("(9/503) No data returned for BRK.B. Skipping.")
        failed_tickers.append('BRK.B')
except Exception as e:
    print(f"(9/503) Failed to fetch data for BRK.B: {e}")
    failed_tickers.append('BRK.B')

# Ticker 10: TSLA
try:
    data_tsla = tv.get_hist(symbol='TSLA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_tsla is not None and not data_tsla.empty:
        all_data['TSLA'] = data_tsla['close']
        print("(10/503) Successfully fetched data for TSLA")
    else:
        print("(10/503) No data returned for TSLA. Skipping.")
        failed_tickers.append('TSLA')
except Exception as e:
    print(f"(10/503) Failed to fetch data for TSLA: {e}")
    failed_tickers.append('TSLA')

# Ticker 11: JPM
try:
    data_jpm = tv.get_hist(symbol='JPM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_jpm is not None and not data_jpm.empty:
        all_data['JPM'] = data_jpm['close']
        print("(11/503) Successfully fetched data for JPM")
    else:
        print("(11/503) No data returned for JPM. Skipping.")
        failed_tickers.append('JPM')
except Exception as e:
    print(f"(11/503) Failed to fetch data for JPM: {e}")
    failed_tickers.append('JPM')

# Ticker 12: WMT
try:
    data_wmt = tv.get_hist(symbol='WMT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wmt is not None and not data_wmt.empty:
        all_data['WMT'] = data_wmt['close']
        print("(12/503) Successfully fetched data for WMT")
    else:
        print("(12/503) No data returned for WMT. Skipping.")
        failed_tickers.append('WMT')
except Exception as e:
    print(f"(12/503) Failed to fetch data for WMT: {e}")
    failed_tickers.append('WMT')

# Ticker 13: ORCL
try:
    data_orcl = tv.get_hist(symbol='ORCL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_orcl is not None and not data_orcl.empty:
        all_data['ORCL'] = data_orcl['close']
        print("(13/503) Successfully fetched data for ORCL")
    else:
        print("(13/503) No data returned for ORCL. Skipping.")
        failed_tickers.append('ORCL')
except Exception as e:
    print(f"(13/503) Failed to fetch data for ORCL: {e}")
    failed_tickers.append('ORCL')

# Ticker 14: V
try:
    data_v = tv.get_hist(symbol='V', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_v is not None and not data_v.empty:
        all_data['V'] = data_v['close']
        print("(14/503) Successfully fetched data for V")
    else:
        print("(14/503) No data returned for V. Skipping.")
        failed_tickers.append('V')
except Exception as e:
    print(f"(14/503) Failed to fetch data for V: {e}")
    failed_tickers.append('V')

# Ticker 15: LLY
try:
    data_lly = tv.get_hist(symbol='LLY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lly is not None and not data_lly.empty:
        all_data['LLY'] = data_lly['close']
        print("(15/503) Successfully fetched data for LLY")
    else:
        print("(15/503) No data returned for LLY. Skipping.")
        failed_tickers.append('LLY')
except Exception as e:
    print(f"(15/503) Failed to fetch data for LLY: {e}")
    failed_tickers.append('LLY')

# Ticker 16: MA
try:
    data_ma = tv.get_hist(symbol='MA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ma is not None and not data_ma.empty:
        all_data['MA'] = data_ma['close']
        print("(16/503) Successfully fetched data for MA")
    else:
        print("(16/503) No data returned for MA. Skipping.")
        failed_tickers.append('MA')
except Exception as e:
    print(f"(16/503) Failed to fetch data for MA: {e}")
    failed_tickers.append('MA')

# Ticker 17: NFLX
try:
    data_nflx = tv.get_hist(symbol='NFLX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_nflx is not None and not data_nflx.empty:
        all_data['NFLX'] = data_nflx['close']
        print("(17/503) Successfully fetched data for NFLX")
    else:
        print("(17/503) No data returned for NFLX. Skipping.")
        failed_tickers.append('NFLX')
except Exception as e:
    print(f"(17/503) Failed to fetch data for NFLX: {e}")
    failed_tickers.append('NFLX')

# Ticker 18: XOM
try:
    data_xom = tv.get_hist(symbol='XOM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_xom is not None and not data_xom.empty:
        all_data['XOM'] = data_xom['close']
        print("(18/503) Successfully fetched data for XOM")
    else:
        print("(18/503) No data returned for XOM. Skipping.")
        failed_tickers.append('XOM')
except Exception as e:
    print(f"(18/503) Failed to fetch data for XOM: {e}")
    failed_tickers.append('XOM')

# Ticker 19: COST
try:
    data_cost = tv.get_hist(symbol='COST', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cost is not None and not data_cost.empty:
        all_data['COST'] = data_cost['close']
        print("(19/503) Successfully fetched data for COST")
    else:
        print("(19/503) No data returned for COST. Skipping.")
        failed_tickers.append('COST')
except Exception as e:
    print(f"(19/503) Failed to fetch data for COST: {e}")
    failed_tickers.append('COST')

# Ticker 20: JNJ
try:
    data_jnj = tv.get_hist(symbol='JNJ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_jnj is not None and not data_jnj.empty:
        all_data['JNJ'] = data_jnj['close']
        print("(20/503) Successfully fetched data for JNJ")
    else:
        print("(20/503) No data returned for JNJ. Skipping.")
        failed_tickers.append('JNJ')
except Exception as e:
    print(f"(20/503) Failed to fetch data for JNJ: {e}")
    failed_tickers.append('JNJ')

# Ticker 21: HD
try:
    data_hd = tv.get_hist(symbol='HD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hd is not None and not data_hd.empty:
        all_data['HD'] = data_hd['close']
        print("(21/503) Successfully fetched data for HD")
    else:
        print("(21/503) No data returned for HD. Skipping.")
        failed_tickers.append('HD')
except Exception as e:
    print(f"(21/503) Failed to fetch data for HD: {e}")
    failed_tickers.append('HD')

# Ticker 22: PG
try:
    data_pg = tv.get_hist(symbol='PG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pg is not None and not data_pg.empty:
        all_data['PG'] = data_pg['close']
        print("(22/503) Successfully fetched data for PG")
    else:
        print("(22/503) No data returned for PG. Skipping.")
        failed_tickers.append('PG')
except Exception as e:
    print(f"(22/503) Failed to fetch data for PG: {e}")
    failed_tickers.append('PG')

# Ticker 23: PLTR
try:
    data_pltr = tv.get_hist(symbol='PLTR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pltr is not None and not data_pltr.empty:
        all_data['PLTR'] = data_pltr['close']
        print("(23/503) Successfully fetched data for PLTR")
    else:
        print("(23/503) No data returned for PLTR. Skipping.")
        failed_tickers.append('PLTR')
except Exception as e:
    print(f"(23/503) Failed to fetch data for PLTR: {e}")
    failed_tickers.append('PLTR')

# Ticker 24: BAC
try:
    data_bac = tv.get_hist(symbol='BAC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bac is not None and not data_bac.empty:
        all_data['BAC'] = data_bac['close']
        print("(24/503) Successfully fetched data for BAC")
    else:
        print("(24/503) No data returned for BAC. Skipping.")
        failed_tickers.append('BAC')
except Exception as e:
    print(f"(24/503) Failed to fetch data for BAC: {e}")
    failed_tickers.append('BAC')

# Ticker 25: ABBV
try:
    data_abbv = tv.get_hist(symbol='ABBV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_abbv is not None and not data_abbv.empty:
        all_data['ABBV'] = data_abbv['close']
        print("(25/503) Successfully fetched data for ABBV")
    else:
        print("(25/503) No data returned for ABBV. Skipping.")
        failed_tickers.append('ABBV')
except Exception as e:
    print(f"(25/503) Failed to fetch data for ABBV: {e}")
    failed_tickers.append('ABBV')


# --- EXPORT CHUNK 1 (TICKERS 1-25) ---
print("\n--- Merging and exporting data for companies 1-25 ---")
chunk_1_data = {}
tickers_1_25 = {
    'NVDA': 'data_nvda', 'MSFT': 'data_msft', 'AAPL': 'data_aapl', 'AMZN': 'data_amzn', 
    'META': 'data_meta', 'AVGO': 'data_avgo', 'GOOGL': 'data_googl', 'GOOG': 'data_goog', 
    'BRK.B': 'data_brk_b', 'TSLA': 'data_tsla', 'JPM': 'data_jpm', 'WMT': 'data_wmt', 
    'ORCL': 'data_orcl', 'V': 'data_v', 'LLY': 'data_lly', 'MA': 'data_ma', 
    'NFLX': 'data_nflx', 'XOM': 'data_xom', 'COST': 'data_cost', 'JNJ': 'data_jnj', 
    'HD': 'data_hd', 'PG': 'data_pg', 'PLTR': 'data_pltr', 'BAC': 'data_bac', 
    'ABBV': 'data_abbv'
}

for ticker, data_var_name in tickers_1_25.items():
    # Check if the variable exists and has data
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        # Get the 'close' price Series
        close_series = locals()[data_var_name]['close']
        
        # *** THE FIX: Standardize the index ***
        # Remove timezone and set time to midnight for consistent alignment
        close_series.index = close_series.index.tz_localize(None).normalize()
        
        # Add the standardized series to our dictionary
        chunk_1_data[ticker] = close_series

if chunk_1_data:
    price_df_1 = pd.DataFrame(chunk_1_data)
    price_df_1.sort_index(inplace=True)
    price_df_1.ffill(inplace=True)
    price_df_1.to_csv('sp500_prices_1-25.csv')
    print("--- Successfully exported sp500_prices_1-25.csv ---\n")
else:
    print("--- No data collected for chunk 1, skipping export. ---\n")


# Ticker 26: CVX
try:
    data_cvx = tv.get_hist(symbol='CVX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cvx is not None and not data_cvx.empty:
        all_data['CVX'] = data_cvx['close']
        print("(26/503) Successfully fetched data for CVX")
    else:
        print("(26/503) No data returned for CVX. Skipping.")
        failed_tickers.append('CVX')
except Exception as e:
    print(f"(26/503) Failed to fetch data for CVX: {e}")
    failed_tickers.append('CVX')

# Ticker 27: KO
try:
    data_ko = tv.get_hist(symbol='KO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ko is not None and not data_ko.empty:
        all_data['KO'] = data_ko['close']
        print("(27/503) Successfully fetched data for KO")
    else:
        print("(27/503) No data returned for KO. Skipping.")
        failed_tickers.append('KO')
except Exception as e:
    print(f"(27/503) Failed to fetch data for KO: {e}")
    failed_tickers.append('KO')

# Ticker 28: AMD
try:
    data_amd = tv.get_hist(symbol='AMD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_amd is not None and not data_amd.empty:
        all_data['AMD'] = data_amd['close']
        print("(28/503) Successfully fetched data for AMD")
    else:
        print("(28/503) No data returned for AMD. Skipping.")
        failed_tickers.append('AMD')
except Exception as e:
    print(f"(28/503) Failed to fetch data for AMD: {e}")
    failed_tickers.append('AMD')

# Ticker 29: GE
try:
    data_ge = tv.get_hist(symbol='GE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ge is not None and not data_ge.empty:
        all_data['GE'] = data_ge['close']
        print("(29/503) Successfully fetched data for GE")
    else:
        print("(29/503) No data returned for GE. Skipping.")
        failed_tickers.append('GE')
except Exception as e:
    print(f"(29/503) Failed to fetch data for GE: {e}")
    failed_tickers.append('GE')

# Ticker 30: TMUS
try:
    data_tmus = tv.get_hist(symbol='TMUS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_tmus is not None and not data_tmus.empty:
        all_data['TMUS'] = data_tmus['close']
        print("(30/503) Successfully fetched data for TMUS")
    else:
        print("(30/503) No data returned for TMUS. Skipping.")
        failed_tickers.append('TMUS')
except Exception as e:
    print(f"(30/503) Failed to fetch data for TMUS: {e}")
    failed_tickers.append('TMUS')

# Ticker 31: CSCO
try:
    data_csco = tv.get_hist(symbol='CSCO', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_csco is not None and not data_csco.empty:
        all_data['CSCO'] = data_csco['close']
        print("(31/503) Successfully fetched data for CSCO")
    else:
        print("(31/503) No data returned for CSCO. Skipping.")
        failed_tickers.append('CSCO')
except Exception as e:
    print(f"(31/503) Failed to fetch data for CSCO: {e}")
    failed_tickers.append('CSCO')

# Ticker 32: WFC
try:
    data_wfc = tv.get_hist(symbol='WFC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wfc is not None and not data_wfc.empty:
        all_data['WFC'] = data_wfc['close']
        print("(32/503) Successfully fetched data for WFC")
    else:
        print("(32/503) No data returned for WFC. Skipping.")
        failed_tickers.append('WFC')
except Exception as e:
    print(f"(32/503) Failed to fetch data for WFC: {e}")
    failed_tickers.append('WFC')

# Ticker 33: CRM
try:
    data_crm = tv.get_hist(symbol='CRM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_crm is not None and not data_crm.empty:
        all_data['CRM'] = data_crm['close']
        print("(33/503) Successfully fetched data for CRM")
    else:
        print("(33/503) No data returned for CRM. Skipping.")
        failed_tickers.append('CRM')
except Exception as e:
    print(f"(33/503) Failed to fetch data for CRM: {e}")
    failed_tickers.append('CRM')

# Ticker 34: PM
try:
    data_pm = tv.get_hist(symbol='PM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pm is not None and not data_pm.empty:
        all_data['PM'] = data_pm['close']
        print("(34/503) Successfully fetched data for PM")
    else:
        print("(34/503) No data returned for PM. Skipping.")
        failed_tickers.append('PM')
except Exception as e:
    print(f"(34/503) Failed to fetch data for PM: {e}")
    failed_tickers.append('PM')

# Ticker 35: IBM
try:
    data_ibm = tv.get_hist(symbol='IBM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ibm is not None and not data_ibm.empty:
        all_data['IBM'] = data_ibm['close']
        print("(35/503) Successfully fetched data for IBM")
    else:
        print("(35/503) No data returned for IBM. Skipping.")
        failed_tickers.append('IBM')
except Exception as e:
    print(f"(35/503) Failed to fetch data for IBM: {e}")
    failed_tickers.append('IBM')

# Ticker 36: UNH
try:
    data_unh = tv.get_hist(symbol='UNH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_unh is not None and not data_unh.empty:
        all_data['UNH'] = data_unh['close']
        print("(36/503) Successfully fetched data for UNH")
    else:
        print("(36/503) No data returned for UNH. Skipping.")
        failed_tickers.append('UNH')
except Exception as e:
    print(f"(36/503) Failed to fetch data for UNH: {e}")
    failed_tickers.append('UNH')

# Ticker 37: MS
try:
    data_ms = tv.get_hist(symbol='MS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ms is not None and not data_ms.empty:
        all_data['MS'] = data_ms['close']
        print("(37/503) Successfully fetched data for MS")
    else:
        print("(37/503) No data returned for MS. Skipping.")
        failed_tickers.append('MS')
except Exception as e:
    print(f"(37/503) Failed to fetch data for MS: {e}")
    failed_tickers.append('MS')

# Ticker 38: INTU
try:
    data_intu = tv.get_hist(symbol='INTU', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_intu is not None and not data_intu.empty:
        all_data['INTU'] = data_intu['close']
        print("(38/503) Successfully fetched data for INTU")
    else:
        print("(38/503) No data returned for INTU. Skipping.")
        failed_tickers.append('INTU')
except Exception as e:
    print(f"(38/503) Failed to fetch data for INTU: {e}")
    failed_tickers.append('INTU')

# Ticker 39: GS
try:
    data_gs = tv.get_hist(symbol='GS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gs is not None and not data_gs.empty:
        all_data['GS'] = data_gs['close']
        print("(39/503) Successfully fetched data for GS")
    else:
        print("(39/503) No data returned for GS. Skipping.")
        failed_tickers.append('GS')
except Exception as e:
    print(f"(39/503) Failed to fetch data for GS: {e}")
    failed_tickers.append('GS')

# Ticker 40: LIN
try:
    data_lin = tv.get_hist(symbol='LIN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_lin is not None and not data_lin.empty:
        all_data['LIN'] = data_lin['close']
        print("(40/503) Successfully fetched data for LIN")
    else:
        print("(40/503) No data returned for LIN. Skipping.")
        failed_tickers.append('LIN')
except Exception as e:
    print(f"(40/503) Failed to fetch data for LIN: {e}")
    failed_tickers.append('LIN')

# Ticker 41: ABT
try:
    data_abt = tv.get_hist(symbol='ABT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_abt is not None and not data_abt.empty:
        all_data['ABT'] = data_abt['close']
        print("(41/503) Successfully fetched data for ABT")
    else:
        print("(41/503) No data returned for ABT. Skipping.")
        failed_tickers.append('ABT')
except Exception as e:
    print(f"(41/503) Failed to fetch data for ABT: {e}")
    failed_tickers.append('ABT')

# Ticker 42: MCD
try:
    data_mcd = tv.get_hist(symbol='MCD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mcd is not None and not data_mcd.empty:
        all_data['MCD'] = data_mcd['close']
        print("(42/503) Successfully fetched data for MCD")
    else:
        print("(42/503) No data returned for MCD. Skipping.")
        failed_tickers.append('MCD')
except Exception as e:
    print(f"(42/503) Failed to fetch data for MCD: {e}")
    failed_tickers.append('MCD')

# Ticker 43: AXP
try:
    data_axp = tv.get_hist(symbol='AXP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_axp is not None and not data_axp.empty:
        all_data['AXP'] = data_axp['close']
        print("(43/503) Successfully fetched data for AXP")
    else:
        print("(43/503) No data returned for AXP. Skipping.")
        failed_tickers.append('AXP')
except Exception as e:
    print(f"(43/503) Failed to fetch data for AXP: {e}")
    failed_tickers.append('AXP')

# Ticker 44: DIS
try:
    data_dis = tv.get_hist(symbol='DIS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dis is not None and not data_dis.empty:
        all_data['DIS'] = data_dis['close']
        print("(44/503) Successfully fetched data for DIS")
    else:
        print("(44/503) No data returned for DIS. Skipping.")
        failed_tickers.append('DIS')
except Exception as e:
    print(f"(44/503) Failed to fetch data for DIS: {e}")
    failed_tickers.append('DIS')

# Ticker 45: RTX
try:
    data_rtx = tv.get_hist(symbol='RTX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rtx is not None and not data_rtx.empty:
        all_data['RTX'] = data_rtx['close']
        print("(45/503) Successfully fetched data for RTX")
    else:
        print("(45/503) No data returned for RTX. Skipping.")
        failed_tickers.append('RTX')
except Exception as e:
    print(f"(45/503) Failed to fetch data for RTX: {e}")
    failed_tickers.append('RTX')

# Ticker 46: NOW
try:
    data_now = tv.get_hist(symbol='NOW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_now is not None and not data_now.empty:
        all_data['NOW'] = data_now['close']
        print("(46/503) Successfully fetched data for NOW")
    else:
        print("(46/503) No data returned for NOW. Skipping.")
        failed_tickers.append('NOW')
except Exception as e:
    print(f"(46/503) Failed to fetch data for NOW: {e}")
    failed_tickers.append('NOW')

# Ticker 47: MRK
try:
    data_mrk = tv.get_hist(symbol='MRK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mrk is not None and not data_mrk.empty:
        all_data['MRK'] = data_mrk['close']
        print("(47/503) Successfully fetched data for MRK")
    else:
        print("(47/503) No data returned for MRK. Skipping.")
        failed_tickers.append('MRK')
except Exception as e:
    print(f"(47/503) Failed to fetch data for MRK: {e}")
    failed_tickers.append('MRK')

# Ticker 48: CAT
try:
    data_cat = tv.get_hist(symbol='CAT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cat is not None and not data_cat.empty:
        all_data['CAT'] = data_cat['close']
        print("(48/503) Successfully fetched data for CAT")
    else:
        print("(48/503) No data returned for CAT. Skipping.")
        failed_tickers.append('CAT')
except Exception as e:
    print(f"(48/503) Failed to fetch data for CAT: {e}")
    failed_tickers.append('CAT')

# Ticker 49: T
try:
    data_t = tv.get_hist(symbol='T', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_t is not None and not data_t.empty:
        all_data['T'] = data_t['close']
        print("(49/503) Successfully fetched data for T")
    else:
        print("(49/503) No data returned for T. Skipping.")
        failed_tickers.append('T')
except Exception as e:
    print(f"(49/503) Failed to fetch data for T: {e}")
    failed_tickers.append('T')

# Ticker 50: PEP
try:
    data_pep = tv.get_hist(symbol='PEP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pep is not None and not data_pep.empty:
        all_data['PEP'] = data_pep['close']
        print("(50/503) Successfully fetched data for PEP")
    else:
        print("(50/503) No data returned for PEP. Skipping.")
        failed_tickers.append('PEP')
except Exception as e:
    print(f"(50/503) Failed to fetch data for PEP: {e}")
    failed_tickers.append('PEP')


# --- EXPORT CHUNK 2 (TICKERS 26-50) ---
print("\n--- Merging and exporting data for companies 26-50 ---")
chunk_2_data = {}
tickers_26_50 = {
    'CVX': 'data_cvx', 'KO': 'data_ko', 'AMD': 'data_amd', 'GE': 'data_ge', 'TMUS': 'data_tmus',
    'CSCO': 'data_csco', 'WFC': 'data_wfc', 'CRM': 'data_crm', 'PM': 'data_pm', 'IBM': 'data_ibm',
    'UNH': 'data_unh', 'MS': 'data_ms', 'INTU': 'data_intu', 'GS': 'data_gs', 'LIN': 'data_lin',
    'ABT': 'data_abt', 'MCD': 'data_mcd', 'AXP': 'data_axp', 'DIS': 'data_dis', 'RTX': 'data_rtx',
    'NOW': 'data_now', 'MRK': 'data_mrk', 'CAT': 'data_cat', 'T': 'data_t', 'PEP': 'data_pep'
}

for ticker, data_var_name in tickers_26_50.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        chunk_2_data[ticker] = locals()[data_var_name]['close']

if chunk_2_data:
    price_df_2 = pd.DataFrame(chunk_2_data)
    price_df_2.sort_index(inplace=True)
    price_df_2.ffill(inplace=True)
    price_df_2.to_csv('sp500_prices_26-50.csv')
    print("--- Successfully exported sp500_prices_26-50.csv ---\n")
else:
    print("--- No data collected for chunk 2, skipping export. ---\n")


# Ticker 51: TMO
try:
    data_tmo = tv.get_hist(symbol='TMO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tmo is not None and not data_tmo.empty:
        all_data['TMO'] = data_tmo['close']
        print("(51/503) Successfully fetched data for TMO")
    else:
        print("(51/503) No data returned for TMO. Skipping.")
        failed_tickers.append('TMO')
except Exception as e:
    print(f"(51/503) Failed to fetch data for TMO: {e}")
    failed_tickers.append('TMO')

# Ticker 52: UBER
try:
    data_uber = tv.get_hist(symbol='UBER', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_uber is not None and not data_uber.empty:
        all_data['UBER'] = data_uber['close']
        print("(52/503) Successfully fetched data for UBER")
    else:
        print("(52/503) No data returned for UBER. Skipping.")
        failed_tickers.append('UBER')
except Exception as e:
    print(f"(52/503) Failed to fetch data for UBER: {e}")
    failed_tickers.append('UBER')

# Ticker 53: BKNG
try:
    data_bkng = tv.get_hist(symbol='BKNG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_bkng is not None and not data_bkng.empty:
        all_data['BKNG'] = data_bkng['close']
        print("(53/503) Successfully fetched data for BKNG")
    else:
        print("(53/503) No data returned for BKNG. Skipping.")
        failed_tickers.append('BKNG')
except Exception as e:
    print(f"(53/503) Failed to fetch data for BKNG: {e}")
    failed_tickers.append('BKNG')

# Ticker 54: VZ
try:
    data_vz = tv.get_hist(symbol='VZ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vz is not None and not data_vz.empty:
        all_data['VZ'] = data_vz['close']
        print("(54/503) Successfully fetched data for VZ")
    else:
        print("(54/503) No data returned for VZ. Skipping.")
        failed_tickers.append('VZ')
except Exception as e:
    print(f"(54/503) Failed to fetch data for VZ: {e}")
    failed_tickers.append('VZ')

# Ticker 55: SCHW
try:
    data_schw = tv.get_hist(symbol='SCHW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_schw is not None and not data_schw.empty:
        all_data['SCHW'] = data_schw['close']
        print("(55/503) Successfully fetched data for SCHW")
    else:
        print("(55/503) No data returned for SCHW. Skipping.")
        failed_tickers.append('SCHW')
except Exception as e:
    print(f"(55/503) Failed to fetch data for SCHW: {e}")
    failed_tickers.append('SCHW')

# Ticker 56: ISRG
try:
    data_isrg = tv.get_hist(symbol='ISRG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_isrg is not None and not data_isrg.empty:
        all_data['ISRG'] = data_isrg['close']
        print("(56/503) Successfully fetched data for ISRG")
    else:
        print("(56/503) No data returned for ISRG. Skipping.")
        failed_tickers.append('ISRG')
except Exception as e:
    print(f"(56/503) Failed to fetch data for ISRG: {e}")
    failed_tickers.append('ISRG')

# Ticker 57: QCOM
try:
    data_qcom = tv.get_hist(symbol='QCOM', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_qcom is not None and not data_qcom.empty:
        all_data['QCOM'] = data_qcom['close']
        print("(57/503) Successfully fetched data for QCOM")
    else:
        print("(57/503) No data returned for QCOM. Skipping.")
        failed_tickers.append('QCOM')
except Exception as e:
    print(f"(57/503) Failed to fetch data for QCOM: {e}")
    failed_tickers.append('QCOM')

# Ticker 58: C
try:
    data_c = tv.get_hist(symbol='C', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_c is not None and not data_c.empty:
        all_data['C'] = data_c['close']
        print("(58/503) Successfully fetched data for C")
    else:
        print("(58/503) No data returned for C. Skipping.")
        failed_tickers.append('C')
except Exception as e:
    print(f"(58/503) Failed to fetch data for C: {e}")
    failed_tickers.append('C')

# Ticker 59: TXN
try:
    data_txn = tv.get_hist(symbol='TXN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_txn is not None and not data_txn.empty:
        all_data['TXN'] = data_txn['close']
        print("(59/503) Successfully fetched data for TXN")
    else:
        print("(59/503) No data returned for TXN. Skipping.")
        failed_tickers.append('TXN')
except Exception as e:
    print(f"(59/503) Failed to fetch data for TXN: {e}")
    failed_tickers.append('TXN')

# Ticker 60: BA
try:
    data_ba = tv.get_hist(symbol='BA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ba is not None and not data_ba.empty:
        all_data['BA'] = data_ba['close']
        print("(60/503) Successfully fetched data for BA")
    else:
        print("(60/503) No data returned for BA. Skipping.")
        failed_tickers.append('BA')
except Exception as e:
    print(f"(60/503) Failed to fetch data for BA: {e}")
    failed_tickers.append('BA')

# Ticker 61: BLK
try:
    data_blk = tv.get_hist(symbol='BLK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_blk is not None and not data_blk.empty:
        all_data['BLK'] = data_blk['close']
        print("(61/503) Successfully fetched data for BLK")
    else:
        print("(61/503) No data returned for BLK. Skipping.")
        failed_tickers.append('BLK')
except Exception as e:
    print(f"(61/503) Failed to fetch data for BLK: {e}")
    failed_tickers.append('BLK')

# Ticker 62: ACN
try:
    data_acn = tv.get_hist(symbol='ACN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_acn is not None and not data_acn.empty:
        all_data['ACN'] = data_acn['close']
        print("(62/503) Successfully fetched data for ACN")
    else:
        print("(62/503) No data returned for ACN. Skipping.")
        failed_tickers.append('ACN')
except Exception as e:
    print(f"(62/503) Failed to fetch data for ACN: {e}")
    failed_tickers.append('ACN')

# Ticker 63: GEV
try:
    data_gev = tv.get_hist(symbol='GEV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gev is not None and not data_gev.empty:
        all_data['GEV'] = data_gev['close']
        print("(63/503) Successfully fetched data for GEV")
    else:
        print("(63/503) No data returned for GEV. Skipping.")
        failed_tickers.append('GEV')
except Exception as e:
    print(f"(63/503) Failed to fetch data for GEV: {e}")
    failed_tickers.append('GEV')

# Ticker 64: AMGN
try:
    data_amgn = tv.get_hist(symbol='AMGN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_amgn is not None and not data_amgn.empty:
        all_data['AMGN'] = data_amgn['close']
        print("(64/503) Successfully fetched data for AMGN")
    else:
        print("(64/503) No data returned for AMGN. Skipping.")
        failed_tickers.append('AMGN')
except Exception as e:
    print(f"(64/503) Failed to fetch data for AMGN: {e}")
    failed_tickers.append('AMGN')

# Ticker 65: SPGI
try:
    data_spgi = tv.get_hist(symbol='SPGI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_spgi is not None and not data_spgi.empty:
        all_data['SPGI'] = data_spgi['close']
        print("(65/503) Successfully fetched data for SPGI")
    else:
        print("(65/503) No data returned for SPGI. Skipping.")
        failed_tickers.append('SPGI')
except Exception as e:
    print(f"(65/503) Failed to fetch data for SPGI: {e}")
    failed_tickers.append('SPGI')

# Ticker 66: ADBE
try:
    data_adbe = tv.get_hist(symbol='ADBE', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_adbe is not None and not data_adbe.empty:
        all_data['ADBE'] = data_adbe['close']
        print("(66/503) Successfully fetched data for ADBE")
    else:
        print("(66/503) No data returned for ADBE. Skipping.")
        failed_tickers.append('ADBE')
except Exception as e:
    print(f"(66/503) Failed to fetch data for ADBE: {e}")
    failed_tickers.append('ADBE')

# Ticker 67: BSX
try:
    data_bsx = tv.get_hist(symbol='BSX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bsx is not None and not data_bsx.empty:
        all_data['BSX'] = data_bsx['close']
        print("(67/503) Successfully fetched data for BSX")
    else:
        print("(67/503) No data returned for BSX. Skipping.")
        failed_tickers.append('BSX')
except Exception as e:
    print(f"(67/503) Failed to fetch data for BSX: {e}")
    failed_tickers.append('BSX')

# Ticker 68: SYK
try:
    data_syk = tv.get_hist(symbol='SYK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_syk is not None and not data_syk.empty:
        all_data['SYK'] = data_syk['close']
        print("(68/503) Successfully fetched data for SYK")
    else:
        print("(68/503) No data returned for SYK. Skipping.")
        failed_tickers.append('SYK')
except Exception as e:
    print(f"(68/503) Failed to fetch data for SYK: {e}")
    failed_tickers.append('SYK')

# Ticker 69: ETN
try:
    data_etn = tv.get_hist(symbol='ETN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_etn is not None and not data_etn.empty:
        all_data['ETN'] = data_etn['close']
        print("(69/503) Successfully fetched data for ETN")
    else:
        print("(69/503) No data returned for ETN. Skipping.")
        failed_tickers.append('ETN')
except Exception as e:
    print(f"(69/503) Failed to fetch data for ETN: {e}")
    failed_tickers.append('ETN')

# Ticker 70: AMAT
try:
    data_amat = tv.get_hist(symbol='AMAT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_amat is not None and not data_amat.empty:
        all_data['AMAT'] = data_amat['close']
        print("(70/503) Successfully fetched data for AMAT")
    else:
        print("(70/503) No data returned for AMAT. Skipping.")
        failed_tickers.append('AMAT')
except Exception as e:
    print(f"(70/503) Failed to fetch data for AMAT: {e}")
    failed_tickers.append('AMAT')

# Ticker 71: NEE
try:
    data_nee = tv.get_hist(symbol='NEE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nee is not None and not data_nee.empty:
        all_data['NEE'] = data_nee['close']
        print("(71/503) Successfully fetched data for NEE")
    else:
        print("(71/503) No data returned for NEE. Skipping.")
        failed_tickers.append('NEE')
except Exception as e:
    print(f"(71/503) Failed to fetch data for NEE: {e}")
    failed_tickers.append('NEE')

# Ticker 72: ANET
try:
    data_anet = tv.get_hist(symbol='ANET', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_anet is not None and not data_anet.empty:
        all_data['ANET'] = data_anet['close']
        print("(72/503) Successfully fetched data for ANET")
    else:
        print("(72/503) No data returned for ANET. Skipping.")
        failed_tickers.append('ANET')
except Exception as e:
    print(f"(72/503) Failed to fetch data for ANET: {e}")
    failed_tickers.append('ANET')

# Ticker 73: DHR
try:
    data_dhr = tv.get_hist(symbol='DHR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dhr is not None and not data_dhr.empty:
        all_data['DHR'] = data_dhr['close']
        print("(73/503) Successfully fetched data for DHR")
    else:
        print("(73/503) No data returned for DHR. Skipping.")
        failed_tickers.append('DHR')
except Exception as e:
    print(f"(73/503) Failed to fetch data for DHR: {e}")
    failed_tickers.append('DHR')

# Ticker 74: PGR
try:
    data_pgr = tv.get_hist(symbol='PGR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pgr is not None and not data_pgr.empty:
        all_data['PGR'] = data_pgr['close']
        print("(74/503) Successfully fetched data for PGR")
    else:
        print("(74/503) No data returned for PGR. Skipping.")
        failed_tickers.append('PGR')
except Exception as e:
    print(f"(74/503) Failed to fetch data for PGR: {e}")
    failed_tickers.append('PGR')

# Ticker 75: HON
try:
    data_hon = tv.get_hist(symbol='HON', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_hon is not None and not data_hon.empty:
        all_data['HON'] = data_hon['close']
        print("(75/503) Successfully fetched data for HON")
    else:
        print("(75/503) No data returned for HON. Skipping.")
        failed_tickers.append('HON')
except Exception as e:
    print(f"(75/503) Failed to fetch data for HON: {e}")
    failed_tickers.append('HON')


# --- EXPORT CHUNK 3 (TICKERS 51-75) ---
print("\n--- Merging and exporting data for companies 51-75 ---")
chunk_3_data = {}
tickers_51_75 = {
    'TMO': 'data_tmo', 'UBER': 'data_uber', 'BKNG': 'data_bkng', 'VZ': 'data_vz', 'SCHW': 'data_schw', 'ISRG': 'data_isrg', 'QCOM': 'data_qcom', 'C': 'data_c', 'TXN': 'data_txn', 'BA': 'data_ba', 'BLK': 'data_blk', 'ACN': 'data_acn', 'GEV': 'data_gev', 'AMGN': 'data_amgn', 'SPGI': 'data_spgi', 'ADBE': 'data_adbe', 'BSX': 'data_bsx', 'SYK': 'data_syk', 'ETN': 'data_etn', 'AMAT': 'data_amat', 'NEE': 'data_nee', 'ANET': 'data_anet', 'DHR': 'data_dhr', 'PGR': 'data_pgr', 'HON': 'data_hon'
}
for ticker, data_var_name in tickers_51_75.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_3_data[ticker] = close_series
if chunk_3_data:
    price_df_3 = pd.DataFrame(chunk_3_data)
    price_df_3.sort_index(inplace=True)
    price_df_3.ffill(inplace=True)
    price_df_3.to_csv('sp500_prices_51-75.csv')
    print("--- Successfully exported sp500_prices_51-75.csv ---\n")
else:
    print("--- No data collected for chunk 3, skipping export. ---\n")


# Ticker 76: TJX
try:
    data_tjx = tv.get_hist(symbol='TJX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tjx is not None and not data_tjx.empty:
        all_data['TJX'] = data_tjx['close']
        print("(76/503) Successfully fetched data for TJX")
    else:
        print("(76/503) No data returned for TJX. Skipping.")
        failed_tickers.append('TJX')
except Exception as e:
    print(f"(76/503) Failed to fetch data for TJX: {e}")
    failed_tickers.append('TJX')

# Ticker 77: GILD
try:
    data_gild = tv.get_hist(symbol='GILD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_gild is not None and not data_gild.empty:
        all_data['GILD'] = data_gild['close']
        print("(77/503) Successfully fetched data for GILD")
    else:
        print("(77/503) No data returned for GILD. Skipping.")
        failed_tickers.append('GILD')
except Exception as e:
    print(f"(77/503) Failed to fetch data for GILD: {e}")
    failed_tickers.append('GILD')

# Ticker 78: BX
try:
    data_bx = tv.get_hist(symbol='BX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bx is not None and not data_bx.empty:
        all_data['BX'] = data_bx['close']
        print("(78/503) Successfully fetched data for BX")
    else:
        print("(78/503) No data returned for BX. Skipping.")
        failed_tickers.append('BX')
except Exception as e:
    print(f"(78/503) Failed to fetch data for BX: {e}")
    failed_tickers.append('BX')

# Ticker 79: PFE
try:
    data_pfe = tv.get_hist(symbol='PFE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pfe is not None and not data_pfe.empty:
        all_data['PFE'] = data_pfe['close']
        print("(79/503) Successfully fetched data for PFE")
    else:
        print("(79/503) No data returned for PFE. Skipping.")
        failed_tickers.append('PFE')
except Exception as e:
    print(f"(79/503) Failed to fetch data for PFE: {e}")
    failed_tickers.append('PFE')

# Ticker 80: DE
try:
    data_de = tv.get_hist(symbol='DE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_de is not None and not data_de.empty:
        all_data['DE'] = data_de['close']
        print("(80/503) Successfully fetched data for DE")
    else:
        print("(80/503) No data returned for DE. Skipping.")
        failed_tickers.append('DE')
except Exception as e:
    print(f"(80/503) Failed to fetch data for DE: {e}")
    failed_tickers.append('DE')

# Ticker 81: COF
try:
    data_cof = tv.get_hist(symbol='COF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cof is not None and not data_cof.empty:
        all_data['COF'] = data_cof['close']
        print("(81/503) Successfully fetched data for COF")
    else:
        print("(81/503) No data returned for COF. Skipping.")
        failed_tickers.append('COF')
except Exception as e:
    print(f"(81/503) Failed to fetch data for COF: {e}")
    failed_tickers.append('COF')

# Ticker 82: KKR
try:
    data_kkr = tv.get_hist(symbol='KKR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kkr is not None and not data_kkr.empty:
        all_data['KKR'] = data_kkr['close']
        print("(82/503) Successfully fetched data for KKR")
    else:
        print("(82/503) No data returned for KKR. Skipping.")
        failed_tickers.append('KKR')
except Exception as e:
    print(f"(82/503) Failed to fetch data for KKR: {e}")
    failed_tickers.append('KKR')

# Ticker 83: PANW
try:
    data_panw = tv.get_hist(symbol='PANW', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_panw is not None and not data_panw.empty:
        all_data['PANW'] = data_panw['close']
        print("(83/503) Successfully fetched data for PANW")
    else:
        print("(83/503) No data returned for PANW. Skipping.")
        failed_tickers.append('PANW')
except Exception as e:
    print(f"(83/503) Failed to fetch data for PANW: {e}")
    failed_tickers.append('PANW')

# Ticker 84: UNP
try:
    data_unp = tv.get_hist(symbol='UNP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_unp is not None and not data_unp.empty:
        all_data['UNP'] = data_unp['close']
        print("(84/503) Successfully fetched data for UNP")
    else:
        print("(84/503) No data returned for UNP. Skipping.")
        failed_tickers.append('UNP')
except Exception as e:
    print(f"(84/503) Failed to fetch data for UNP: {e}")
    failed_tickers.append('UNP')

# Ticker 85: LOW
try:
    data_low = tv.get_hist(symbol='LOW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_low is not None and not data_low.empty:
        all_data['LOW'] = data_low['close']
        print("(85/503) Successfully fetched data for LOW")
    else:
        print("(85/503) No data returned for LOW. Skipping.")
        failed_tickers.append('LOW')
except Exception as e:
    print(f"(85/503) Failed to fetch data for LOW: {e}")
    failed_tickers.append('LOW')

# Ticker 86: APH
try:
    data_aph = tv.get_hist(symbol='APH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aph is not None and not data_aph.empty:
        all_data['APH'] = data_aph['close']
        print("(86/503) Successfully fetched data for APH")
    else:
        print("(86/503) No data returned for APH. Skipping.")
        failed_tickers.append('APH')
except Exception as e:
    print(f"(86/503) Failed to fetch data for APH: {e}")
    failed_tickers.append('APH')

# Ticker 87: LRCX
try:
    data_lrcx = tv.get_hist(symbol='LRCX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_lrcx is not None and not data_lrcx.empty:
        all_data['LRCX'] = data_lrcx['close']
        print("(87/503) Successfully fetched data for LRCX")
    else:
        print("(87/503) No data returned for LRCX. Skipping.")
        failed_tickers.append('LRCX')
except Exception as e:
    print(f"(87/503) Failed to fetch data for LRCX: {e}")
    failed_tickers.append('LRCX')

# Ticker 88: ADP
try:
    data_adp = tv.get_hist(symbol='ADP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_adp is not None and not data_adp.empty:
        all_data['ADP'] = data_adp['close']
        print("(88/503) Successfully fetched data for ADP")
    else:
        print("(88/503) No data returned for ADP. Skipping.")
        failed_tickers.append('ADP')
except Exception as e:
    print(f"(88/503) Failed to fetch data for ADP: {e}")
    failed_tickers.append('ADP')

# Ticker 89: MU
try:
    data_mu = tv.get_hist(symbol='MU', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mu is not None and not data_mu.empty:
        all_data['MU'] = data_mu['close']
        print("(89/503) Successfully fetched data for MU")
    else:
        print("(89/503) No data returned for MU. Skipping.")
        failed_tickers.append('MU')
except Exception as e:
    print(f"(89/503) Failed to fetch data for MU: {e}")
    failed_tickers.append('MU')

# Ticker 90: CMCSA
try:
    data_cmcsa = tv.get_hist(symbol='CMCSA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cmcsa is not None and not data_cmcsa.empty:
        all_data['CMCSA'] = data_cmcsa['close']
        print("(90/503) Successfully fetched data for CMCSA")
    else:
        print("(90/503) No data returned for CMCSA. Skipping.")
        failed_tickers.append('CMCSA')
except Exception as e:
    print(f"(90/503) Failed to fetch data for CMCSA: {e}")
    failed_tickers.append('CMCSA')

# Ticker 91: COP
try:
    data_cop = tv.get_hist(symbol='COP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cop is not None and not data_cop.empty:
        all_data['COP'] = data_cop['close']
        print("(91/503) Successfully fetched data for COP")
    else:
        print("(91/503) No data returned for COP. Skipping.")
        failed_tickers.append('COP')
except Exception as e:
    print(f"(91/503) Failed to fetch data for COP: {e}")
    failed_tickers.append('COP')

# Ticker 92: KLAC
try:
    data_klac = tv.get_hist(symbol='KLAC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_klac is not None and not data_klac.empty:
        all_data['KLAC'] = data_klac['close']
        print("(92/503) Successfully fetched data for KLAC")
    else:
        print("(92/503) No data returned for KLAC. Skipping.")
        failed_tickers.append('KLAC')
except Exception as e:
    print(f"(92/503) Failed to fetch data for KLAC: {e}")
    failed_tickers.append('KLAC')

# Ticker 93: VRTX
try:
    data_vrtx = tv.get_hist(symbol='VRTX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_vrtx is not None and not data_vrtx.empty:
        all_data['VRTX'] = data_vrtx['close']
        print("(93/503) Successfully fetched data for VRTX")
    else:
        print("(93/503) No data returned for VRTX. Skipping.")
        failed_tickers.append('VRTX')
except Exception as e:
    print(f"(93/503) Failed to fetch data for VRTX: {e}")
    failed_tickers.append('VRTX')

# Ticker 94: MDT
try:
    data_mdt = tv.get_hist(symbol='MDT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mdt is not None and not data_mdt.empty:
        all_data['MDT'] = data_mdt['close']
        print("(94/503) Successfully fetched data for MDT")
    else:
        print("(94/503) No data returned for MDT. Skipping.")
        failed_tickers.append('MDT')
except Exception as e:
    print(f"(94/503) Failed to fetch data for MDT: {e}")
    failed_tickers.append('MDT')

# Ticker 95: SNPS
try:
    data_snps = tv.get_hist(symbol='SNPS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_snps is not None and not data_snps.empty:
        all_data['SNPS'] = data_snps['close']
        print("(95/503) Successfully fetched data for SNPS")
    else:
        print("(95/503) No data returned for SNPS. Skipping.")
        failed_tickers.append('SNPS')
except Exception as e:
    print(f"(95/503) Failed to fetch data for SNPS: {e}")
    failed_tickers.append('SNPS')

# Ticker 96: CRWD
try:
    data_crwd = tv.get_hist(symbol='CRWD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_crwd is not None and not data_crwd.empty:
        all_data['CRWD'] = data_crwd['close']
        print("(96/503) Successfully fetched data for CRWD")
    else:
        print("(96/503) No data returned for CRWD. Skipping.")
        failed_tickers.append('CRWD')
except Exception as e:
    print(f"(96/503) Failed to fetch data for CRWD: {e}")
    failed_tickers.append('CRWD')

# Ticker 97: NKE
try:
    data_nke = tv.get_hist(symbol='NKE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nke is not None and not data_nke.empty:
        all_data['NKE'] = data_nke['close']
        print("(97/503) Successfully fetched data for NKE")
    else:
        print("(97/503) No data returned for NKE. Skipping.")
        failed_tickers.append('NKE')
except Exception as e:
    print(f"(97/503) Failed to fetch data for NKE: {e}")
    failed_tickers.append('NKE')

# Ticker 98: ADI
try:
    data_adi = tv.get_hist(symbol='ADI', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_adi is not None and not data_adi.empty:
        all_data['ADI'] = data_adi['close']
        print("(98/503) Successfully fetched data for ADI")
    else:
        print("(98/503) No data returned for ADI. Skipping.")
        failed_tickers.append('ADI')
except Exception as e:
    print(f"(98/503) Failed to fetch data for ADI: {e}")
    failed_tickers.append('ADI')

# Ticker 99: WELL
try:
    data_well = tv.get_hist(symbol='WELL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_well is not None and not data_well.empty:
        all_data['WELL'] = data_well['close']
        print("(99/503) Successfully fetched data for WELL")
    else:
        print("(99/503) No data returned for WELL. Skipping.")
        failed_tickers.append('WELL')
except Exception as e:
    print(f"(99/503) Failed to fetch data for WELL: {e}")
    failed_tickers.append('WELL')

# Ticker 100: CB
try:
    data_cb = tv.get_hist(symbol='CB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cb is not None and not data_cb.empty:
        all_data['CB'] = data_cb['close']
        print("(100/503) Successfully fetched data for CB")
    else:
        print("(100/503) No data returned for CB. Skipping.")
        failed_tickers.append('CB')
except Exception as e:
    print(f"(100/503) Failed to fetch data for CB: {e}")
    failed_tickers.append('CB')


# --- EXPORT CHUNK 4 (TICKERS 76-100) ---
print("\n--- Merging and exporting data for companies 76-100 ---")
chunk_4_data = {}
tickers_76_100 = {
    'TJX': 'data_tjx', 'GILD': 'data_gild', 'BX': 'data_bx', 'PFE': 'data_pfe', 'DE': 'data_de', 'COF': 'data_cof', 'KKR': 'data_kkr', 'PANW': 'data_panw', 'UNP': 'data_unp', 'LOW': 'data_low', 'APH': 'data_aph', 'LRCX': 'data_lrcx', 'ADP': 'data_adp', 'MU': 'data_mu', 'CMCSA': 'data_cmcsa', 'COP': 'data_cop', 'KLAC': 'data_klac', 'VRTX': 'data_vrtx', 'MDT': 'data_mdt', 'SNPS': 'data_snps', 'CRWD': 'data_crwd', 'NKE': 'data_nke', 'ADI': 'data_adi', 'WELL': 'data_well', 'CB': 'data_cb'
}
for ticker, data_var_name in tickers_76_100.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_4_data[ticker] = close_series
if chunk_4_data:
    price_df_4 = pd.DataFrame(chunk_4_data)
    price_df_4.sort_index(inplace=True)
    price_df_4.ffill(inplace=True)
    price_df_4.to_csv('sp500_prices_76-100.csv')
    print("--- Successfully exported sp500_prices_76-100.csv ---\n")
else:
    print("--- No data collected for chunk 4, skipping export. ---\n")


# Ticker 101: ICE
try:
    data_ice = tv.get_hist(symbol='ICE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ice is not None and not data_ice.empty:
        all_data['ICE'] = data_ice['close']
        print("(101/503) Successfully fetched data for ICE")
    else:
        print("(101/503) No data returned for ICE. Skipping.")
        failed_tickers.append('ICE')
except Exception as e:
    print(f"(101/503) Failed to fetch data for ICE: {e}")
    failed_tickers.append('ICE')

# Ticker 102: SBUX
try:
    data_sbux = tv.get_hist(symbol='SBUX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_sbux is not None and not data_sbux.empty:
        all_data['SBUX'] = data_sbux['close']
        print("(102/503) Successfully fetched data for SBUX")
    else:
        print("(102/503) No data returned for SBUX. Skipping.")
        failed_tickers.append('SBUX')
except Exception as e:
    print(f"(102/503) Failed to fetch data for SBUX: {e}")
    failed_tickers.append('SBUX')

# Ticker 103: SO
try:
    data_so = tv.get_hist(symbol='SO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_so is not None and not data_so.empty:
        all_data['SO'] = data_so['close']
        print("(103/503) Successfully fetched data for SO")
    else:
        print("(103/503) No data returned for SO. Skipping.")
        failed_tickers.append('SO')
except Exception as e:
    print(f"(103/503) Failed to fetch data for SO: {e}")
    failed_tickers.append('SO')

# Ticker 104: TT
try:
    data_tt = tv.get_hist(symbol='TT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tt is not None and not data_tt.empty:
        all_data['TT'] = data_tt['close']
        print("(104/503) Successfully fetched data for TT")
    else:
        print("(104/503) No data returned for TT. Skipping.")
        failed_tickers.append('TT')
except Exception as e:
    print(f"(104/503) Failed to fetch data for TT: {e}")
    failed_tickers.append('TT')

# Ticker 105: CEG
try:
    data_ceg = tv.get_hist(symbol='CEG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ceg is not None and not data_ceg.empty:
        all_data['CEG'] = data_ceg['close']
        print("(105/503) Successfully fetched data for CEG")
    else:
        print("(105/503) No data returned for CEG. Skipping.")
        failed_tickers.append('CEG')
except Exception as e:
    print(f"(105/503) Failed to fetch data for CEG: {e}")
    failed_tickers.append('CEG')

# Ticker 106: DASH
try:
    data_dash = tv.get_hist(symbol='DASH', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_dash is not None and not data_dash.empty:
        all_data['DASH'] = data_dash['close']
        print("(106/503) Successfully fetched data for DASH")
    else:
        print("(106/503) No data returned for DASH. Skipping.")
        failed_tickers.append('DASH')
except Exception as e:
    print(f"(106/503) Failed to fetch data for DASH: {e}")
    failed_tickers.append('DASH')

# Ticker 107: AMT
try:
    data_amt = tv.get_hist(symbol='AMT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_amt is not None and not data_amt.empty:
        all_data['AMT'] = data_amt['close']
        print("(107/503) Successfully fetched data for AMT")
    else:
        print("(107/503) No data returned for AMT. Skipping.")
        failed_tickers.append('AMT')
except Exception as e:
    print(f"(107/503) Failed to fetch data for AMT: {e}")
    failed_tickers.append('AMT')

# Ticker 108: PLD
try:
    data_pld = tv.get_hist(symbol='PLD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pld is not None and not data_pld.empty:
        all_data['PLD'] = data_pld['close']
        print("(108/503) Successfully fetched data for PLD")
    else:
        print("(108/503) No data returned for PLD. Skipping.")
        failed_tickers.append('PLD')
except Exception as e:
    print(f"(108/503) Failed to fetch data for PLD: {e}")
    failed_tickers.append('PLD')

# Ticker 109: MO
try:
    data_mo = tv.get_hist(symbol='MO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mo is not None and not data_mo.empty:
        all_data['MO'] = data_mo['close']
        print("(109/503) Successfully fetched data for MO")
    else:
        print("(109/503) No data returned for MO. Skipping.")
        failed_tickers.append('MO')
except Exception as e:
    print(f"(109/503) Failed to fetch data for MO: {e}")
    failed_tickers.append('MO')

# Ticker 110: MMC
try:
    data_mmc = tv.get_hist(symbol='MMC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mmc is not None and not data_mmc.empty:
        all_data['MMC'] = data_mmc['close']
        print("(110/503) Successfully fetched data for MMC")
    else:
        print("(110/503) No data returned for MMC. Skipping.")
        failed_tickers.append('MMC')
except Exception as e:
    print(f"(110/503) Failed to fetch data for MMC: {e}")
    failed_tickers.append('MMC')

# Ticker 111: CME
try:
    data_cme = tv.get_hist(symbol='CME', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cme is not None and not data_cme.empty:
        all_data['CME'] = data_cme['close']
        print("(111/503) Successfully fetched data for CME")
    else:
        print("(111/503) No data returned for CME. Skipping.")
        failed_tickers.append('CME')
except Exception as e:
    print(f"(111/503) Failed to fetch data for CME: {e}")
    failed_tickers.append('CME')

# Ticker 112: CDNS
try:
    data_cdns = tv.get_hist(symbol='CDNS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cdns is not None and not data_cdns.empty:
        all_data['CDNS'] = data_cdns['close']
        print("(112/503) Successfully fetched data for CDNS")
    else:
        print("(112/503) No data returned for CDNS. Skipping.")
        failed_tickers.append('CDNS')
except Exception as e:
    print(f"(112/503) Failed to fetch data for CDNS: {e}")
    failed_tickers.append('CDNS')

# Ticker 113: LMT
try:
    data_lmt = tv.get_hist(symbol='LMT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lmt is not None and not data_lmt.empty:
        all_data['LMT'] = data_lmt['close']
        print("(113/503) Successfully fetched data for LMT")
    else:
        print("(113/503) No data returned for LMT. Skipping.")
        failed_tickers.append('LMT')
except Exception as e:
    print(f"(113/503) Failed to fetch data for LMT: {e}")
    failed_tickers.append('LMT')

# Ticker 114: BMY
try:
    data_bmy = tv.get_hist(symbol='BMY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bmy is not None and not data_bmy.empty:
        all_data['BMY'] = data_bmy['close']
        print("(114/503) Successfully fetched data for BMY")
    else:
        print("(114/503) No data returned for BMY. Skipping.")
        failed_tickers.append('BMY')
except Exception as e:
    print(f"(114/503) Failed to fetch data for BMY: {e}")
    failed_tickers.append('BMY')

# Ticker 115: WM
try:
    data_wm = tv.get_hist(symbol='WM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wm is not None and not data_wm.empty:
        all_data['WM'] = data_wm['close']
        print("(115/503) Successfully fetched data for WM")
    else:
        print("(115/503) No data returned for WM. Skipping.")
        failed_tickers.append('WM')
except Exception as e:
    print(f"(115/503) Failed to fetch data for WM: {e}")
    failed_tickers.append('WM')

# Ticker 116: PH
try:
    data_ph = tv.get_hist(symbol='PH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ph is not None and not data_ph.empty:
        all_data['PH'] = data_ph['close']
        print("(116/503) Successfully fetched data for PH")
    else:
        print("(116/503) No data returned for PH. Skipping.")
        failed_tickers.append('PH')
except Exception as e:
    print(f"(116/503) Failed to fetch data for PH: {e}")
    failed_tickers.append('PH')

# Ticker 117: COIN
try:
    data_coin = tv.get_hist(symbol='COIN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_coin is not None and not data_coin.empty:
        all_data['COIN'] = data_coin['close']
        print("(117/503) Successfully fetched data for COIN")
    else:
        print("(117/503) No data returned for COIN. Skipping.")
        failed_tickers.append('COIN')
except Exception as e:
    print(f"(117/503) Failed to fetch data for COIN: {e}")
    failed_tickers.append('COIN')

# Ticker 118: DUK
try:
    data_duk = tv.get_hist(symbol='DUK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_duk is not None and not data_duk.empty:
        all_data['DUK'] = data_duk['close']
        print("(118/503) Successfully fetched data for DUK")
    else:
        print("(118/503) No data returned for DUK. Skipping.")
        failed_tickers.append('DUK')
except Exception as e:
    print(f"(118/503) Failed to fetch data for DUK: {e}")
    failed_tickers.append('DUK')

# Ticker 119: MCO
try:
    data_mco = tv.get_hist(symbol='MCO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mco is not None and not data_mco.empty:
        all_data['MCO'] = data_mco['close']
        print("(119/503) Successfully fetched data for MCO")
    else:
        print("(119/503) No data returned for MCO. Skipping.")
        failed_tickers.append('MCO')
except Exception as e:
    print(f"(119/503) Failed to fetch data for MCO: {e}")
    failed_tickers.append('MCO')

# Ticker 120: RCL
try:
    data_rcl = tv.get_hist(symbol='RCL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rcl is not None and not data_rcl.empty:
        all_data['RCL'] = data_rcl['close']
        print("(120/503) Successfully fetched data for RCL")
    else:
        print("(120/503) No data returned for RCL. Skipping.")
        failed_tickers.append('RCL')
except Exception as e:
    print(f"(120/503) Failed to fetch data for RCL: {e}")
    failed_tickers.append('RCL')

# Ticker 121: MDLZ
try:
    data_mdlz = tv.get_hist(symbol='MDLZ', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mdlz is not None and not data_mdlz.empty:
        all_data['MDLZ'] = data_mdlz['close']
        print("(121/503) Successfully fetched data for MDLZ")
    else:
        print("(121/503) No data returned for MDLZ. Skipping.")
        failed_tickers.append('MDLZ')
except Exception as e:
    print(f"(121/503) Failed to fetch data for MDLZ: {e}")
    failed_tickers.append('MDLZ')

# Ticker 122: TDG
try:
    data_tdg = tv.get_hist(symbol='TDG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tdg is not None and not data_tdg.empty:
        all_data['TDG'] = data_tdg['close']
        print("(122/503) Successfully fetched data for TDG")
    else:
        print("(122/503) No data returned for TDG. Skipping.")
        failed_tickers.append('TDG')
except Exception as e:
    print(f"(122/503) Failed to fetch data for TDG: {e}")
    failed_tickers.append('TDG')

# Ticker 123: DELL
try:
    data_dell = tv.get_hist(symbol='DELL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dell is not None and not data_dell.empty:
        all_data['DELL'] = data_dell['close']
        print("(123/503) Successfully fetched data for DELL")
    else:
        print("(123/503) No data returned for DELL. Skipping.")
        failed_tickers.append('DELL')
except Exception as e:
    print(f"(123/503) Failed to fetch data for DELL: {e}")
    failed_tickers.append('DELL')

# Ticker 124: CTAS
try:
    data_ctas = tv.get_hist(symbol='CTAS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ctas is not None and not data_ctas.empty:
        all_data['CTAS'] = data_ctas['close']
        print("(124/503) Successfully fetched data for CTAS")
    else:
        print("(124/503) No data returned for CTAS. Skipping.")
        failed_tickers.append('CTAS')
except Exception as e:
    print(f"(124/503) Failed to fetch data for CTAS: {e}")
    failed_tickers.append('CTAS')

# Ticker 125: INTC
try:
    data_intc = tv.get_hist(symbol='INTC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_intc is not None and not data_intc.empty:
        all_data['INTC'] = data_intc['close']
        print("(125/503) Successfully fetched data for INTC")
    else:
        print("(125/503) No data returned for INTC. Skipping.")
        failed_tickers.append('INTC')
except Exception as e:
    print(f"(125/503) Failed to fetch data for INTC: {e}")
    failed_tickers.append('INTC')


# --- EXPORT CHUNK 5 (TICKERS 101-125) ---
print("\n--- Merging and exporting data for companies 101-125 ---")
chunk_5_data = {}
tickers_101_125 = {
    'ICE': 'data_ice', 'SBUX': 'data_sbux', 'SO': 'data_so', 'TT': 'data_tt', 'CEG': 'data_ceg', 'DASH': 'data_dash', 'AMT': 'data_amt', 'PLD': 'data_pld', 'MO': 'data_mo', 'MMC': 'data_mmc', 'CME': 'data_cme', 'CDNS': 'data_cdns', 'LMT': 'data_lmt', 'BMY': 'data_bmy', 'WM': 'data_wm', 'PH': 'data_ph', 'COIN': 'data_coin', 'DUK': 'data_duk', 'MCO': 'data_mco', 'RCL': 'data_rcl', 'MDLZ': 'data_mdlz', 'TDG': 'data_tdg', 'DELL': 'data_dell', 'CTAS': 'data_ctas', 'INTC': 'data_intc'
}
for ticker, data_var_name in tickers_101_125.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_5_data[ticker] = close_series
if chunk_5_data:
    price_df_5 = pd.DataFrame(chunk_5_data)
    price_df_5.sort_index(inplace=True)
    price_df_5.ffill(inplace=True)
    price_df_5.to_csv('sp500_prices_101-125.csv')
    print("--- Successfully exported sp500_prices_101-125.csv ---\n")
else:
    print("--- No data collected for chunk 5, skipping export. ---\n")


# Ticker 126: MCK
try:
    data_mck = tv.get_hist(symbol='MCK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mck is not None and not data_mck.empty:
        all_data['MCK'] = data_mck['close']
        print("(126/503) Successfully fetched data for MCK")
    else:
        print("(126/503) No data returned for MCK. Skipping.")
        failed_tickers.append('MCK')
except Exception as e:
    print(f"(126/503) Failed to fetch data for MCK: {e}")
    failed_tickers.append('MCK')

# Ticker 127: GD
try:
    data_gd = tv.get_hist(symbol='GD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gd is not None and not data_gd.empty:
        all_data['GD'] = data_gd['close']
        print("(127/503) Successfully fetched data for GD")
    else:
        print("(127/503) No data returned for GD. Skipping.")
        failed_tickers.append('GD')
except Exception as e:
    print(f"(127/503) Failed to fetch data for GD: {e}")
    failed_tickers.append('GD')

# Ticker 128: ABNB
try:
    data_abnb = tv.get_hist(symbol='ABNB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_abnb is not None and not data_abnb.empty:
        all_data['ABNB'] = data_abnb['close']
        print("(128/503) Successfully fetched data for ABNB")
    else:
        print("(128/503) No data returned for ABNB. Skipping.")
        failed_tickers.append('ABNB')
except Exception as e:
    print(f"(128/503) Failed to fetch data for ABNB: {e}")
    failed_tickers.append('ABNB')

# Ticker 129: ORLY
try:
    data_orly = tv.get_hist(symbol='ORLY', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_orly is not None and not data_orly.empty:
        all_data['ORLY'] = data_orly['close']
        print("(129/503) Successfully fetched data for ORLY")
    else:
        print("(129/503) No data returned for ORLY. Skipping.")
        failed_tickers.append('ORLY')
except Exception as e:
    print(f"(129/503) Failed to fetch data for ORLY: {e}")
    failed_tickers.append('ORLY')

# Ticker 130: APO
try:
    data_apo = tv.get_hist(symbol='APO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_apo is not None and not data_apo.empty:
        all_data['APO'] = data_apo['close']
        print("(130/503) Successfully fetched data for APO")
    else:
        print("(130/503) No data returned for APO. Skipping.")
        failed_tickers.append('APO')
except Exception as e:
    print(f"(130/503) Failed to fetch data for APO: {e}")
    failed_tickers.append('APO')

# Ticker 131: SHW
try:
    data_shw = tv.get_hist(symbol='SHW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_shw is not None and not data_shw.empty:
        all_data['SHW'] = data_shw['close']
        print("(131/503) Successfully fetched data for SHW")
    else:
        print("(131/503) No data returned for SHW. Skipping.")
        failed_tickers.append('SHW')
except Exception as e:
    print(f"(131/503) Failed to fetch data for SHW: {e}")
    failed_tickers.append('SHW')

# Ticker 132: HCA
try:
    data_hca = tv.get_hist(symbol='HCA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hca is not None and not data_hca.empty:
        all_data['HCA'] = data_hca['close']
        print("(132/503) Successfully fetched data for HCA")
    else:
        print("(132/503) No data returned for HCA. Skipping.")
        failed_tickers.append('HCA')
except Exception as e:
    print(f"(132/503) Failed to fetch data for HCA: {e}")
    failed_tickers.append('HCA')

# Ticker 133: EMR
try:
    data_emr = tv.get_hist(symbol='EMR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_emr is not None and not data_emr.empty:
        all_data['EMR'] = data_emr['close']
        print("(133/503) Successfully fetched data for EMR")
    else:
        print("(133/503) No data returned for EMR. Skipping.")
        failed_tickers.append('EMR')
except Exception as e:
    print(f"(133/503) Failed to fetch data for EMR: {e}")
    failed_tickers.append('EMR')

# Ticker 134: NOC
try:
    data_noc = tv.get_hist(symbol='NOC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_noc is not None and not data_noc.empty:
        all_data['NOC'] = data_noc['close']
        print("(134/503) Successfully fetched data for NOC")
    else:
        print("(134/503) No data returned for NOC. Skipping.")
        failed_tickers.append('NOC')
except Exception as e:
    print(f"(134/503) Failed to fetch data for NOC: {e}")
    failed_tickers.append('NOC')

# Ticker 135: MMM
try:
    data_mmm = tv.get_hist(symbol='MMM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mmm is not None and not data_mmm.empty:
        all_data['MMM'] = data_mmm['close']
        print("(135/503) Successfully fetched data for MMM")
    else:
        print("(135/503) No data returned for MMM. Skipping.")
        failed_tickers.append('MMM')
except Exception as e:
    print(f"(135/503) Failed to fetch data for MMM: {e}")
    failed_tickers.append('MMM')

# Ticker 136: EQIX
try:
    data_eqix = tv.get_hist(symbol='EQIX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_eqix is not None and not data_eqix.empty:
        all_data['EQIX'] = data_eqix['close']
        print("(136/503) Successfully fetched data for EQIX")
    else:
        print("(136/503) No data returned for EQIX. Skipping.")
        failed_tickers.append('EQIX')
except Exception as e:
    print(f"(136/503) Failed to fetch data for EQIX: {e}")
    failed_tickers.append('EQIX')

# Ticker 137: FTNT
try:
    data_ftnt = tv.get_hist(symbol='FTNT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ftnt is not None and not data_ftnt.empty:
        all_data['FTNT'] = data_ftnt['close']
        print("(137/503) Successfully fetched data for FTNT")
    else:
        print("(137/503) No data returned for FTNT. Skipping.")
        failed_tickers.append('FTNT')
except Exception as e:
    print(f"(137/503) Failed to fetch data for FTNT: {e}")
    failed_tickers.append('FTNT')

# Ticker 138: CI
try:
    data_ci = tv.get_hist(symbol='CI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ci is not None and not data_ci.empty:
        all_data['CI'] = data_ci['close']
        print("(138/503) Successfully fetched data for CI")
    else:
        print("(138/503) No data returned for CI. Skipping.")
        failed_tickers.append('CI')
except Exception as e:
    print(f"(138/503) Failed to fetch data for CI: {e}")
    failed_tickers.append('CI')

# Ticker 139: UPS
try:
    data_ups = tv.get_hist(symbol='UPS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ups is not None and not data_ups.empty:
        all_data['UPS'] = data_ups['close']
        print("(139/503) Successfully fetched data for UPS")
    else:
        print("(139/503) No data returned for UPS. Skipping.")
        failed_tickers.append('UPS')
except Exception as e:
    print(f"(139/503) Failed to fetch data for UPS: {e}")
    failed_tickers.append('UPS')

# Ticker 140: FISV
try:
    data_fisv = tv.get_hist(symbol='FISV', exchange='VIE', interval=INTERVAL, n_bars=N_BARS)
    if data_fisv is not None and not data_fisv.empty:
        all_data['FISV'] = data_fisv['close']
        print("(140/503) Successfully fetched data for FISV")
    else:
        print("(140/503) No data returned for FISV. Skipping.")
        failed_tickers.append('FISV')
except Exception as e:
    print(f"(140/503) Failed to fetch data for FISV: {e}")
    failed_tickers.append('FISV')

# Ticker 141: AON
try:
    data_aon = tv.get_hist(symbol='AON', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aon is not None and not data_aon.empty:
        all_data['AON'] = data_aon['close']
        print("(141/503) Successfully fetched data for AON")
    else:
        print("(141/503) No data returned for AON. Skipping.")
        failed_tickers.append('AON')
except Exception as e:
    print(f"(141/503) Failed to fetch data for AON: {e}")
    failed_tickers.append('AON')

# Ticker 142: CVS
try:
    data_cvs = tv.get_hist(symbol='CVS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cvs is not None and not data_cvs.empty:
        all_data['CVS'] = data_cvs['close']
        print("(142/503) Successfully fetched data for CVS")
    else:
        print("(142/503) No data returned for CVS. Skipping.")
        failed_tickers.append('CVS')
except Exception as e:
    print(f"(142/503) Failed to fetch data for CVS: {e}")
    failed_tickers.append('CVS')

# Ticker 143: RSG
try:
    data_rsg = tv.get_hist(symbol='RSG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rsg is not None and not data_rsg.empty:
        all_data['RSG'] = data_rsg['close']
        print("(143/503) Successfully fetched data for RSG")
    else:
        print("(143/503) No data returned for RSG. Skipping.")
        failed_tickers.append('RSG')
except Exception as e:
    print(f"(143/503) Failed to fetch data for RSG: {e}")
    failed_tickers.append('RSG')

# Ticker 144: HWM
try:
    data_hwm = tv.get_hist(symbol='HWM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hwm is not None and not data_hwm.empty:
        all_data['HWM'] = data_hwm['close']
        print("(144/503) Successfully fetched data for HWM")
    else:
        print("(144/503) No data returned for HWM. Skipping.")
        failed_tickers.append('HWM')
except Exception as e:
    print(f"(144/503) Failed to fetch data for HWM: {e}")
    failed_tickers.append('HWM')

# Ticker 145: PNC
try:
    data_pnc = tv.get_hist(symbol='PNC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pnc is not None and not data_pnc.empty:
        all_data['PNC'] = data_pnc['close']
        print("(145/503) Successfully fetched data for PNC")
    else:
        print("(145/503) No data returned for PNC. Skipping.")
        failed_tickers.append('PNC')
except Exception as e:
    print(f"(145/503) Failed to fetch data for PNC: {e}")
    failed_tickers.append('PNC')

# Ticker 146: AJG
try:
    data_ajg = tv.get_hist(symbol='AJG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ajg is not None and not data_ajg.empty:
        all_data['AJG'] = data_ajg['close']
        print("(146/503) Successfully fetched data for AJG")
    else:
        print("(146/503) No data returned for AJG. Skipping.")
        failed_tickers.append('AJG')
except Exception as e:
    print(f"(146/503) Failed to fetch data for AJG: {e}")
    failed_tickers.append('AJG')

# Ticker 147: ITW
try:
    data_itw = tv.get_hist(symbol='ITW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_itw is not None and not data_itw.empty:
        all_data['ITW'] = data_itw['close']
        print("(147/503) Successfully fetched data for ITW")
    else:
        print("(147/503) No data returned for ITW. Skipping.")
        failed_tickers.append('ITW')
except Exception as e:
    print(f"(147/503) Failed to fetch data for ITW: {e}")
    failed_tickers.append('ITW')

# Ticker 148: MAR
try:
    data_mar = tv.get_hist(symbol='MAR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mar is not None and not data_mar.empty:
        all_data['MAR'] = data_mar['close']
        print("(148/503) Successfully fetched data for MAR")
    else:
        print("(148/503) No data returned for MAR. Skipping.")
        failed_tickers.append('MAR')
except Exception as e:
    print(f"(148/503) Failed to fetch data for MAR: {e}")
    failed_tickers.append('MAR')

# Ticker 149: ECL
try:
    data_ecl = tv.get_hist(symbol='ECL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ecl is not None and not data_ecl.empty:
        all_data['ECL'] = data_ecl['close']
        print("(149/503) Successfully fetched data for ECL")
    else:
        print("(149/503) No data returned for ECL. Skipping.")
        failed_tickers.append('ECL')
except Exception as e:
    print(f"(149/503) Failed to fetch data for ECL: {e}")
    failed_tickers.append('ECL')

# Ticker 150: MSI
try:
    data_msi = tv.get_hist(symbol='MSI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_msi is not None and not data_msi.empty:
        all_data['MSI'] = data_msi['close']
        print("(150/503) Successfully fetched data for MSI")
    else:
        print("(150/503) No data returned for MSI. Skipping.")
        failed_tickers.append('MSI')
except Exception as e:
    print(f"(150/503) Failed to fetch data for MSI: {e}")
    failed_tickers.append('MSI')

# --- EXPORT CHUNK 6 (TICKERS 126-150) ---
print("\n--- Merging and exporting data for companies 126-150 ---")
chunk_6_data = {}
tickers_126_150 = {
    'MCK': 'data_mck', 'GD': 'data_gd', 'ABNB': 'data_abnb', 'ORLY': 'data_orly', 'APO': 'data_apo', 'SHW': 'data_shw', 'HCA': 'data_hca', 'EMR': 'data_emr', 'NOC': 'data_noc', 'MMM': 'data_mmm', 'EQIX': 'data_eqix', 'FTNT': 'data_ftnt', 'CI': 'data_ci', 'UPS': 'data_ups', 'FISV': 'data_fisv', 'AON': 'data_aon', 'CVS': 'data_cvs', 'RSG': 'data_rsg', 'HWM': 'data_hwm', 'PNC': 'data_pnc', 'AJG': 'data_ajg', 'ITW': 'data_itw', 'MAR': 'data_mar', 'ECL': 'data_ecl', 'MSI': 'data_msi'
}
for ticker, data_var_name in tickers_126_150.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_6_data[ticker] = close_series
if chunk_6_data:
    price_df_6 = pd.DataFrame(chunk_6_data)
    price_df_6.sort_index(inplace=True)
    price_df_6.ffill(inplace=True)
    price_df_6.to_csv('sp500_prices_126-150.csv')
    print("--- Successfully exported sp500_prices_126-150.csv ---\n")
else:
    print("--- No data collected for chunk 6, skipping export. ---\n")


# Ticker 151: WMB
try:
    data_wmb = tv.get_hist(symbol='WMB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wmb is not None and not data_wmb.empty:
        all_data['WMB'] = data_wmb['close']
        print("(151/503) Successfully fetched data for WMB")
    else:
        print("(151/503) No data returned for WMB. Skipping.")
        failed_tickers.append('WMB')
except Exception as e:
    print(f"(151/503) Failed to fetch data for WMB: {e}")
    failed_tickers.append('WMB')

# Ticker 152: USB
try:
    data_usb = tv.get_hist(symbol='USB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_usb is not None and not data_usb.empty:
        all_data['USB'] = data_usb['close']
        print("(152/503) Successfully fetched data for USB")
    else:
        print("(152/503) No data returned for USB. Skipping.")
        failed_tickers.append('USB')
except Exception as e:
    print(f"(152/503) Failed to fetch data for USB: {e}")
    failed_tickers.append('USB')

# Ticker 153: BK
try:
    data_bk = tv.get_hist(symbol='BK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bk is not None and not data_bk.empty:
        all_data['BK'] = data_bk['close']
        print("(153/503) Successfully fetched data for BK")
    else:
        print("(153/503) No data returned for BK. Skipping.")
        failed_tickers.append('BK')
except Exception as e:
    print(f"(153/503) Failed to fetch data for BK: {e}")
    failed_tickers.append('BK')

# Ticker 154: CL
try:
    data_cl = tv.get_hist(symbol='CL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cl is not None and not data_cl.empty:
        all_data['CL'] = data_cl['close']
        print("(154/503) Successfully fetched data for CL")
    else:
        print("(154/503) No data returned for CL. Skipping.")
        failed_tickers.append('CL')
except Exception as e:
    print(f"(154/503) Failed to fetch data for CL: {e}")
    failed_tickers.append('CL')

# Ticker 155: NEM
try:
    data_nem = tv.get_hist(symbol='NEM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nem is not None and not data_nem.empty:
        all_data['NEM'] = data_nem['close']
        print("(155/503) Successfully fetched data for NEM")
    else:
        print("(155/503) No data returned for NEM. Skipping.")
        failed_tickers.append('NEM')
except Exception as e:
    print(f"(155/503) Failed to fetch data for NEM: {e}")
    failed_tickers.append('NEM')

# Ticker 156: PYPL
try:
    data_pypl = tv.get_hist(symbol='PYPL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pypl is not None and not data_pypl.empty:
        all_data['PYPL'] = data_pypl['close']
        print("(156/503) Successfully fetched data for PYPL")
    else:
        print("(156/503) No data returned for PYPL. Skipping.")
        failed_tickers.append('PYPL')
except Exception as e:
    print(f"(156/503) Failed to fetch data for PYPL: {e}")
    failed_tickers.append('PYPL')

# Ticker 157: JCI
try:
    data_jci = tv.get_hist(symbol='JCI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_jci is not None and not data_jci.empty:
        all_data['JCI'] = data_jci['close']
        print("(157/503) Successfully fetched data for JCI")
    else:
        print("(157/503) No data returned for JCI. Skipping.")
        failed_tickers.append('JCI')
except Exception as e:
    print(f"(157/503) Failed to fetch data for JCI: {e}")
    failed_tickers.append('JCI')

# Ticker 158: ZTS
try:
    data_zts = tv.get_hist(symbol='ZTS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_zts is not None and not data_zts.empty:
        all_data['ZTS'] = data_zts['close']
        print("(158/503) Successfully fetched data for ZTS")
    else:
        print("(158/503) No data returned for ZTS. Skipping.")
        failed_tickers.append('ZTS')
except Exception as e:
    print(f"(158/503) Failed to fetch data for ZTS: {e}")
    failed_tickers.append('ZTS')

# Ticker 159: VST
try:
    data_vst = tv.get_hist(symbol='VST', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vst is not None and not data_vst.empty:
        all_data['VST'] = data_vst['close']
        print("(159/503) Successfully fetched data for VST")
    else:
        print("(159/503) No data returned for VST. Skipping.")
        failed_tickers.append('VST')
except Exception as e:
    print(f"(159/503) Failed to fetch data for VST: {e}")
    failed_tickers.append('VST')

# Ticker 160: EOG
try:
    data_eog = tv.get_hist(symbol='EOG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_eog is not None and not data_eog.empty:
        all_data['EOG'] = data_eog['close']
        print("(160/503) Successfully fetched data for EOG")
    else:
        print("(160/503) No data returned for EOG. Skipping.")
        failed_tickers.append('EOG')
except Exception as e:
    print(f"(160/503) Failed to fetch data for EOG: {e}")
    failed_tickers.append('EOG')

# Ticker 161: ELV
try:
    data_elv = tv.get_hist(symbol='ELV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_elv is not None and not data_elv.empty:
        all_data['ELV'] = data_elv['close']
        print("(161/503) Successfully fetched data for ELV")
    else:
        print("(161/503) No data returned for ELV. Skipping.")
        failed_tickers.append('ELV')
except Exception as e:
    print(f"(161/503) Failed to fetch data for ELV: {e}")
    failed_tickers.append('ELV')

# Ticker 162: CSX
try:
    data_csx = tv.get_hist(symbol='CSX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_csx is not None and not data_csx.empty:
        all_data['CSX'] = data_csx['close']
        print("(162/503) Successfully fetched data for CSX")
    else:
        print("(162/503) No data returned for CSX. Skipping.")
        failed_tickers.append('CSX')
except Exception as e:
    print(f"(162/503) Failed to fetch data for CSX: {e}")
    failed_tickers.append('CSX')

# Ticker 163: APD
try:
    data_apd = tv.get_hist(symbol='APD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_apd is not None and not data_apd.empty:
        all_data['APD'] = data_apd['close']
        print("(163/503) Successfully fetched data for APD")
    else:
        print("(163/503) No data returned for APD. Skipping.")
        failed_tickers.append('APD')
except Exception as e:
    print(f"(163/503) Failed to fetch data for APD: {e}")
    failed_tickers.append('APD')

# Ticker 164: ADSK
try:
    data_adsk = tv.get_hist(symbol='ADSK', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_adsk is not None and not data_adsk.empty:
        all_data['ADSK'] = data_adsk['close']
        print("(164/503) Successfully fetched data for ADSK")
    else:
        print("(164/503) No data returned for ADSK. Skipping.")
        failed_tickers.append('ADSK')
except Exception as e:
    print(f"(164/503) Failed to fetch data for ADSK: {e}")
    failed_tickers.append('ADSK')

# Ticker 165: AZO
try:
    data_azo = tv.get_hist(symbol='AZO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_azo is not None and not data_azo.empty:
        all_data['AZO'] = data_azo['close']
        print("(165/503) Successfully fetched data for AZO")
    else:
        print("(165/503) No data returned for AZO. Skipping.")
        failed_tickers.append('AZO')
except Exception as e:
    print(f"(165/503) Failed to fetch data for AZO: {e}")
    failed_tickers.append('AZO')

# Ticker 166: HLT
try:
    data_hlt = tv.get_hist(symbol='HLT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hlt is not None and not data_hlt.empty:
        all_data['HLT'] = data_hlt['close']
        print("(166/503) Successfully fetched data for HLT")
    else:
        print("(166/503) No data returned for HLT. Skipping.")
        failed_tickers.append('HLT')
except Exception as e:
    print(f"(166/503) Failed to fetch data for HLT: {e}")
    failed_tickers.append('HLT')

# Ticker 167: WDAY
try:
    data_wday = tv.get_hist(symbol='WDAY', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wday is not None and not data_wday.empty:
        all_data['WDAY'] = data_wday['close']
        print("(167/503) Successfully fetched data for WDAY")
    else:
        print("(167/503) No data returned for WDAY. Skipping.")
        failed_tickers.append('WDAY')
except Exception as e:
    print(f"(167/503) Failed to fetch data for WDAY: {e}")
    failed_tickers.append('WDAY')

# Ticker 168: NSC
try:
    data_nsc = tv.get_hist(symbol='NSC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nsc is not None and not data_nsc.empty:
        all_data['NSC'] = data_nsc['close']
        print("(168/503) Successfully fetched data for NSC")
    else:
        print("(168/503) No data returned for NSC. Skipping.")
        failed_tickers.append('NSC')
except Exception as e:
    print(f"(168/503) Failed to fetch data for NSC: {e}")
    failed_tickers.append('NSC')

# Ticker 169: KMI
try:
    data_kmi = tv.get_hist(symbol='KMI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kmi is not None and not data_kmi.empty:
        all_data['KMI'] = data_kmi['close']
        print("(169/503) Successfully fetched data for KMI")
    else:
        print("(169/503) No data returned for KMI. Skipping.")
        failed_tickers.append('KMI')
except Exception as e:
    print(f"(169/503) Failed to fetch data for KMI: {e}")
    failed_tickers.append('KMI')

# Ticker 170: TEL
try:
    data_tel = tv.get_hist(symbol='TEL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tel is not None and not data_tel.empty:
        all_data['TEL'] = data_tel['close']
        print("(170/503) Successfully fetched data for TEL")
    else:
        print("(170/503) No data returned for TEL. Skipping.")
        failed_tickers.append('TEL')
except Exception as e:
    print(f"(170/503) Failed to fetch data for TEL: {e}")
    failed_tickers.append('TEL')

# Ticker 171: CARR
try:
    data_carr = tv.get_hist(symbol='CARR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_carr is not None and not data_carr.empty:
        all_data['CARR'] = data_carr['close']
        print("(171/503) Successfully fetched data for CARR")
    else:
        print("(171/503) No data returned for CARR. Skipping.")
        failed_tickers.append('CARR')
except Exception as e:
    print(f"(171/503) Failed to fetch data for CARR: {e}")
    failed_tickers.append('CARR')

# Ticker 172: PWR
try:
    data_pwr = tv.get_hist(symbol='PWR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pwr is not None and not data_pwr.empty:
        all_data['PWR'] = data_pwr['close']
        print("(172/503) Successfully fetched data for PWR")
    else:
        print("(172/503) No data returned for PWR. Skipping.")
        failed_tickers.append('PWR')
except Exception as e:
    print(f"(172/503) Failed to fetch data for PWR: {e}")
    failed_tickers.append('PWR')

# Ticker 173: DLR
try:
    data_dlr = tv.get_hist(symbol='DLR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dlr is not None and not data_dlr.empty:
        all_data['DLR'] = data_dlr['close']
        print("(173/503) Successfully fetched data for DLR")
    else:
        print("(173/503) No data returned for DLR. Skipping.")
        failed_tickers.append('DLR')
except Exception as e:
    print(f"(173/503) Failed to fetch data for DLR: {e}")
    failed_tickers.append('DLR')

# Ticker 174: REGN
try:
    data_regn = tv.get_hist(symbol='REGN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_regn is not None and not data_regn.empty:
        all_data['REGN'] = data_regn['close']
        print("(174/503) Successfully fetched data for REGN")
    else:
        print("(174/503) No data returned for REGN. Skipping.")
        failed_tickers.append('REGN')
except Exception as e:
    print(f"(174/503) Failed to fetch data for REGN: {e}")
    failed_tickers.append('REGN')

# Ticker 175: ROP
try:
    data_rop = tv.get_hist(symbol='ROP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_rop is not None and not data_rop.empty:
        all_data['ROP'] = data_rop['close']
        print("(175/503) Successfully fetched data for ROP")
    else:
        print("(175/503) No data returned for ROP. Skipping.")
        failed_tickers.append('ROP')
except Exception as e:
    print(f"(175/503) Failed to fetch data for ROP: {e}")
    failed_tickers.append('ROP')

# --- EXPORT CHUNK 7 (TICKERS 151-175) ---
print("\n--- Merging and exporting data for companies 151-175 ---")
chunk_7_data = {}
tickers_151_175 = {
    'WMB': 'data_wmb', 'USB': 'data_usb', 'BK': 'data_bk', 'CL': 'data_cl', 'NEM': 'data_nem', 'PYPL': 'data_pypl', 'JCI': 'data_jci', 'ZTS': 'data_zts', 'VST': 'data_vst', 'EOG': 'data_eog', 'ELV': 'data_elv', 'CSX': 'data_csx', 'APD': 'data_apd', 'ADSK': 'data_adsk', 'AZO': 'data_azo', 'HLT': 'data_hlt', 'WDAY': 'data_wday', 'NSC': 'data_nsc', 'KMI': 'data_kmi', 'TEL': 'data_tel', 'CARR': 'data_carr', 'PWR': 'data_pwr', 'DLR': 'data_dlr', 'REGN': 'data_regn', 'ROP': 'data_rop'
}
for ticker, data_var_name in tickers_151_175.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_7_data[ticker] = close_series
if chunk_7_data:
    price_df_7 = pd.DataFrame(chunk_7_data)
    price_df_7.sort_index(inplace=True)
    price_df_7.ffill(inplace=True)
    price_df_7.to_csv('sp500_prices_151-175.csv')
    print("--- Successfully exported sp500_prices_151-175.csv ---\n")
else:
    print("--- No data collected for chunk 7, skipping export. ---\n")

# Ticker 176: FCX
try:
    data_fcx = tv.get_hist(symbol='FCX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fcx is not None and not data_fcx.empty:
        all_data['FCX'] = data_fcx['close']
        print("(176/503) Successfully fetched data for FCX")
    else:
        print("(176/503) No data returned for FCX. Skipping.")
        failed_tickers.append('FCX')
except Exception as e:
    print(f"(176/503) Failed to fetch data for FCX: {e}")
    failed_tickers.append('FCX')

# Ticker 177: MNST
try:
    data_mnst = tv.get_hist(symbol='MNST', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mnst is not None and not data_mnst.empty:
        all_data['MNST'] = data_mnst['close']
        print("(177/503) Successfully fetched data for MNST")
    else:
        print("(177/503) No data returned for MNST. Skipping.")
        failed_tickers.append('MNST')
except Exception as e:
    print(f"(177/503) Failed to fetch data for MNST: {e}")
    failed_tickers.append('MNST')

# Ticker 178: CMG
try:
    data_cmg = tv.get_hist(symbol='CMG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cmg is not None and not data_cmg.empty:
        all_data['CMG'] = data_cmg['close']
        print("(178/503) Successfully fetched data for CMG")
    else:
        print("(178/503) No data returned for CMG. Skipping.")
        failed_tickers.append('CMG')
except Exception as e:
    print(f"(178/503) Failed to fetch data for CMG: {e}")
    failed_tickers.append('CMG')

# Ticker 179: TRV
try:
    data_trv = tv.get_hist(symbol='TRV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_trv is not None and not data_trv.empty:
        all_data['TRV'] = data_trv['close']
        print("(179/503) Successfully fetched data for TRV")
    else:
        print("(179/503) No data returned for TRV. Skipping.")
        failed_tickers.append('TRV')
except Exception as e:
    print(f"(179/503) Failed to fetch data for TRV: {e}")
    failed_tickers.append('TRV')

# Ticker 180: AEP
try:
    data_aep = tv.get_hist(symbol='AEP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_aep is not None and not data_aep.empty:
        all_data['AEP'] = data_aep['close']
        print("(180/503) Successfully fetched data for AEP")
    else:
        print("(180/503) No data returned for AEP. Skipping.")
        failed_tickers.append('AEP')
except Exception as e:
    print(f"(180/503) Failed to fetch data for AEP: {e}")
    failed_tickers.append('AEP')

# Ticker 181: TFC
try:
    data_tfc = tv.get_hist(symbol='TFC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tfc is not None and not data_tfc.empty:
        all_data['TFC'] = data_tfc['close']
        print("(181/503) Successfully fetched data for TFC")
    else:
        print("(181/503) No data returned for TFC. Skipping.")
        failed_tickers.append('TFC')
except Exception as e:
    print(f"(181/503) Failed to fetch data for TFC: {e}")
    failed_tickers.append('TFC')

# Ticker 182: NXPI
try:
    data_nxpi = tv.get_hist(symbol='NXPI', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_nxpi is not None and not data_nxpi.empty:
        all_data['NXPI'] = data_nxpi['close']
        print("(182/503) Successfully fetched data for NXPI")
    else:
        print("(182/503) No data returned for NXPI. Skipping.")
        failed_tickers.append('NXPI')
except Exception as e:
    print(f"(182/503) Failed to fetch data for NXPI: {e}")
    failed_tickers.append('NXPI')

# Ticker 183: URI
try:
    data_uri = tv.get_hist(symbol='URI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_uri is not None and not data_uri.empty:
        all_data['URI'] = data_uri['close']
        print("(183/503) Successfully fetched data for URI")
    else:
        print("(183/503) No data returned for URI. Skipping.")
        failed_tickers.append('URI')
except Exception as e:
    print(f"(183/503) Failed to fetch data for URI: {e}")
    failed_tickers.append('URI')

# Ticker 184: AXON
try:
    data_axon = tv.get_hist(symbol='AXON', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_axon is not None and not data_axon.empty:
        all_data['AXON'] = data_axon['close']
        print("(184/503) Successfully fetched data for AXON")
    else:
        print("(184/503) No data returned for AXON. Skipping.")
        failed_tickers.append('AXON')
except Exception as e:
    print(f"(184/503) Failed to fetch data for AXON: {e}")
    failed_tickers.append('AXON')

# Ticker 185: COR
try:
    data_cor = tv.get_hist(symbol='COR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cor is not None and not data_cor.empty:
        all_data['COR'] = data_cor['close']
        print("(185/503) Successfully fetched data for COR")
    else:
        print("(185/503) No data returned for COR. Skipping.")
        failed_tickers.append('COR')
except Exception as e:
    print(f"(185/503) Failed to fetch data for COR: {e}")
    failed_tickers.append('COR')

# Ticker 186: FDX
try:
    data_fdx = tv.get_hist(symbol='FDX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fdx is not None and not data_fdx.empty:
        all_data['FDX'] = data_fdx['close']
        print("(186/503) Successfully fetched data for FDX")
    else:
        print("(186/503) No data returned for FDX. Skipping.")
        failed_tickers.append('FDX')
except Exception as e:
    print(f"(186/503) Failed to fetch data for FDX: {e}")
    failed_tickers.append('FDX')

# Ticker 187: NDAQ
try:
    data_ndaq = tv.get_hist(symbol='NDAQ', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ndaq is not None and not data_ndaq.empty:
        all_data['NDAQ'] = data_ndaq['close']
        print("(187/503) Successfully fetched data for NDAQ")
    else:
        print("(187/503) No data returned for NDAQ. Skipping.")
        failed_tickers.append('NDAQ')
except Exception as e:
    print(f"(187/503) Failed to fetch data for NDAQ: {e}")
    failed_tickers.append('NDAQ')

# Ticker 188: AFL
try:
    data_afl = tv.get_hist(symbol='AFL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_afl is not None and not data_afl.empty:
        all_data['AFL'] = data_afl['close']
        print("(188/503) Successfully fetched data for AFL")
    else:
        print("(188/503) No data returned for AFL. Skipping.")
        failed_tickers.append('AFL')
except Exception as e:
    print(f"(188/503) Failed to fetch data for AFL: {e}")
    failed_tickers.append('AFL')

# Ticker 189: SPG
try:
    data_spg = tv.get_hist(symbol='SPG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_spg is not None and not data_spg.empty:
        all_data['SPG'] = data_spg['close']
        print("(189/503) Successfully fetched data for SPG")
    else:
        print("(189/503) No data returned for SPG. Skipping.")
        failed_tickers.append('SPG')
except Exception as e:
    print(f"(189/503) Failed to fetch data for SPG: {e}")
    failed_tickers.append('SPG')

# Ticker 190: GLW
try:
    data_glw = tv.get_hist(symbol='GLW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_glw is not None and not data_glw.empty:
        all_data['GLW'] = data_glw['close']
        print("(190/503) Successfully fetched data for GLW")
    else:
        print("(190/503) No data returned for GLW. Skipping.")
        failed_tickers.append('GLW')
except Exception as e:
    print(f"(190/503) Failed to fetch data for GLW: {e}")
    failed_tickers.append('GLW')

# Ticker 191: FAST
try:
    data_fast = tv.get_hist(symbol='FAST', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_fast is not None and not data_fast.empty:
        all_data['FAST'] = data_fast['close']
        print("(191/503) Successfully fetched data for FAST")
    else:
        print("(191/503) No data returned for FAST. Skipping.")
        failed_tickers.append('FAST')
except Exception as e:
    print(f"(191/503) Failed to fetch data for FAST: {e}")
    failed_tickers.append('FAST')

# Ticker 192: MPC
try:
    data_mpc = tv.get_hist(symbol='MPC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mpc is not None and not data_mpc.empty:
        all_data['MPC'] = data_mpc['close']
        print("(192/503) Successfully fetched data for MPC")
    else:
        print("(192/503) No data returned for MPC. Skipping.")
        failed_tickers.append('MPC')
except Exception as e:
    print(f"(192/503) Failed to fetch data for MPC: {e}")
    failed_tickers.append('MPC')

# Ticker 193: SRE
try:
    data_sre = tv.get_hist(symbol='SRE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_sre is not None and not data_sre.empty:
        all_data['SRE'] = data_sre['close']
        print("(193/503) Successfully fetched data for SRE")
    else:
        print("(193/503) No data returned for SRE. Skipping.")
        failed_tickers.append('SRE')
except Exception as e:
    print(f"(193/503) Failed to fetch data for SRE: {e}")
    failed_tickers.append('SRE')

# Ticker 194: PAYX
try:
    data_payx = tv.get_hist(symbol='PAYX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_payx is not None and not data_payx.empty:
        all_data['PAYX'] = data_payx['close']
        print("(194/503) Successfully fetched data for PAYX")
    else:
        print("(194/503) No data returned for PAYX. Skipping.")
        failed_tickers.append('PAYX')
except Exception as e:
    print(f"(194/503) Failed to fetch data for PAYX: {e}")
    failed_tickers.append('PAYX')

# Ticker 195: SLB
try:
    data_slb = tv.get_hist(symbol='SLB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_slb is not None and not data_slb.empty:
        all_data['SLB'] = data_slb['close']
        print("(195/503) Successfully fetched data for SLB")
    else:
        print("(195/503) No data returned for SLB. Skipping.")
        failed_tickers.append('SLB')
except Exception as e:
    print(f"(195/503) Failed to fetch data for SLB: {e}")
    failed_tickers.append('SLB')

# Ticker 196: MET
try:
    data_met = tv.get_hist(symbol='MET', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_met is not None and not data_met.empty:
        all_data['MET'] = data_met['close']
        print("(196/503) Successfully fetched data for MET")
    else:
        print("(196/503) No data returned for MET. Skipping.")
        failed_tickers.append('MET')
except Exception as e:
    print(f"(196/503) Failed to fetch data for MET: {e}")
    failed_tickers.append('MET')

# Ticker 197: BDX
try:
    data_bdx = tv.get_hist(symbol='BDX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bdx is not None and not data_bdx.empty:
        all_data['BDX'] = data_bdx['close']
        print("(197/503) Successfully fetched data for BDX")
    else:
        print("(197/503) No data returned for BDX. Skipping.")
        failed_tickers.append('BDX')
except Exception as e:
    print(f"(197/503) Failed to fetch data for BDX: {e}")
    failed_tickers.append('BDX')

# Ticker 198: PCAR
try:
    data_pcar = tv.get_hist(symbol='PCAR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pcar is not None and not data_pcar.empty:
        all_data['PCAR'] = data_pcar['close']
        print("(198/503) Successfully fetched data for PCAR")
    else:
        print("(198/503) No data returned for PCAR. Skipping.")
        failed_tickers.append('PCAR')
except Exception as e:
    print(f"(198/503) Failed to fetch data for PCAR: {e}")
    failed_tickers.append('PCAR')

# Ticker 199: OKE
try:
    data_oke = tv.get_hist(symbol='OKE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_oke is not None and not data_oke.empty:
        all_data['OKE'] = data_oke['close']
        print("(199/503) Successfully fetched data for OKE")
    else:
        print("(199/503) No data returned for OKE. Skipping.")
        failed_tickers.append('OKE')
except Exception as e:
    print(f"(199/503) Failed to fetch data for OKE: {e}")
    failed_tickers.append('OKE')

# Ticker 200: O
try:
    data_o = tv.get_hist(symbol='O', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_o is not None and not data_o.empty:
        all_data['O'] = data_o['close']
        print("(200/503) Successfully fetched data for O")
    else:
        print("(200/503) No data returned for O. Skipping.")
        failed_tickers.append('O')
except Exception as e:
    print(f"(200/503) Failed to fetch data for O: {e}")
    failed_tickers.append('O')


# --- EXPORT CHUNK 8 (TICKERS 176-200) ---
print("\n--- Merging and exporting data for companies 176-200 ---")
chunk_8_data = {}
tickers_176_200 = {
    'FCX': 'data_fcx', 'MNST': 'data_mnst', 'CMG': 'data_cmg', 'TRV': 'data_trv', 'AEP': 'data_aep', 'TFC': 'data_tfc', 'NXPI': 'data_nxpi', 'URI': 'data_uri', 'AXON': 'data_axon', 'COR': 'data_cor', 'FDX': 'data_fdx', 'NDAQ': 'data_ndaq', 'AFL': 'data_afl', 'SPG': 'data_spg', 'GLW': 'data_glw', 'FAST': 'data_fast', 'MPC': 'data_mpc', 'SRE': 'data_sre', 'PAYX': 'data_payx', 'SLB': 'data_slb', 'MET': 'data_met', 'BDX': 'data_bdx', 'PCAR': 'data_pcar', 'OKE': 'data_oke', 'O': 'data_o'
}
for ticker, data_var_name in tickers_176_200.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_8_data[ticker] = close_series
if chunk_8_data:
    price_df_8 = pd.DataFrame(chunk_8_data)
    price_df_8.sort_index(inplace=True)
    price_df_8.ffill(inplace=True)
    price_df_8.to_csv('sp500_prices_176-200.csv')
    print("--- Successfully exported sp500_prices_176-200.csv ---\n")
else:
    print("--- No data collected for chunk 8, skipping export. ---\n")

# Ticker 201: DDOG
try:
    data_ddog = tv.get_hist(symbol='DDOG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ddog is not None and not data_ddog.empty:
        all_data['DDOG'] = data_ddog['close']
        print("(201/503) Successfully fetched data for DDOG")
    else:
        print("(201/503) No data returned for DDOG. Skipping.")
        failed_tickers.append('DDOG')
except Exception as e:
    print(f"(201/503) Failed to fetch data for DDOG: {e}")
    failed_tickers.append('DDOG')

# Ticker 202: ALL
try:
    data_all = tv.get_hist(symbol='ALL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_all is not None and not data_all.empty:
        all_data['ALL'] = data_all['close']
        print("(202/503) Successfully fetched data for ALL")
    else:
        print("(202/503) No data returned for ALL. Skipping.")
        failed_tickers.append('ALL')
except Exception as e:
    print(f"(202/503) Failed to fetch data for ALL: {e}")
    failed_tickers.append('ALL')

# Ticker 203: PSX
try:
    data_psx = tv.get_hist(symbol='PSX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_psx is not None and not data_psx.empty:
        all_data['PSX'] = data_psx['close']
        print("(203/503) Successfully fetched data for PSX")
    else:
        print("(203/503) No data returned for PSX. Skipping.")
        failed_tickers.append('PSX')
except Exception as e:
    print(f"(203/503) Failed to fetch data for PSX: {e}")
    failed_tickers.append('PSX')

# Ticker 204: PSA
try:
    data_psa = tv.get_hist(symbol='PSA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_psa is not None and not data_psa.empty:
        all_data['PSA'] = data_psa['close']
        print("(204/503) Successfully fetched data for PSA")
    else:
        print("(204/503) No data returned for PSA. Skipping.")
        failed_tickers.append('PSA')
except Exception as e:
    print(f"(204/503) Failed to fetch data for PSA: {e}")
    failed_tickers.append('PSA')

# Ticker 205: LHX
try:
    data_lhx = tv.get_hist(symbol='LHX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lhx is not None and not data_lhx.empty:
        all_data['LHX'] = data_lhx['close']
        print("(205/503) Successfully fetched data for LHX")
    else:
        print("(205/503) No data returned for LHX. Skipping.")
        failed_tickers.append('LHX')
except Exception as e:
    print(f"(205/503) Failed to fetch data for LHX: {e}")
    failed_tickers.append('LHX')

# Ticker 206: GWW
try:
    data_gww = tv.get_hist(symbol='GWW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gww is not None and not data_gww.empty:
        all_data['GWW'] = data_gww['close']
        print("(206/503) Successfully fetched data for GWW")
    else:
        print("(206/503) No data returned for GWW. Skipping.")
        failed_tickers.append('GWW')
except Exception as e:
    print(f"(206/503) Failed to fetch data for GWW: {e}")
    failed_tickers.append('GWW')

# Ticker 207: CMI
try:
    data_cmi = tv.get_hist(symbol='CMI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cmi is not None and not data_cmi.empty:
        all_data['CMI'] = data_cmi['close']
        print("(207/503) Successfully fetched data for CMI")
    else:
        print("(207/503) No data returned for CMI. Skipping.")
        failed_tickers.append('CMI')
except Exception as e:
    print(f"(207/503) Failed to fetch data for CMI: {e}")
    failed_tickers.append('CMI')

# Ticker 208: GM
try:
    data_gm = tv.get_hist(symbol='GM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gm is not None and not data_gm.empty:
        all_data['GM'] = data_gm['close']
        print("(208/503) Successfully fetched data for GM")
    else:
        print("(208/503) No data returned for GM. Skipping.")
        failed_tickers.append('GM')
except Exception as e:
    print(f"(208/503) Failed to fetch data for GM: {e}")
    failed_tickers.append('GM')

# Ticker 209: D
try:
    data_d = tv.get_hist(symbol='D', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_d is not None and not data_d.empty:
        all_data['D'] = data_d['close']
        print("(209/503) Successfully fetched data for D")
    else:
        print("(209/503) No data returned for D. Skipping.")
        failed_tickers.append('D')
except Exception as e:
    print(f"(209/503) Failed to fetch data for D: {e}")
    failed_tickers.append('D')

# Ticker 210: CTVA
try:
    data_ctva = tv.get_hist(symbol='CTVA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ctva is not None and not data_ctva.empty:
        all_data['CTVA'] = data_ctva['close']
        print("(210/503) Successfully fetched data for CTVA")
    else:
        print("(210/503) No data returned for CTVA. Skipping.")
        failed_tickers.append('CTVA')
except Exception as e:
    print(f"(210/503) Failed to fetch data for CTVA: {e}")
    failed_tickers.append('CTVA')

# Ticker 211: AMP
try:
    data_amp = tv.get_hist(symbol='AMP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_amp is not None and not data_amp.empty:
        all_data['AMP'] = data_amp['close']
        print("(211/503) Successfully fetched data for AMP")
    else:
        print("(211/503) No data returned for AMP. Skipping.")
        failed_tickers.append('AMP')
except Exception as e:
    print(f"(211/503) Failed to fetch data for AMP: {e}")
    failed_tickers.append('AMP')

# Ticker 212: SQ
try:
    data_sq = tv.get_hist(symbol='SQ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_sq is not None and not data_sq.empty:
        all_data['SQ'] = data_sq['close']
        print("(212/503) Successfully fetched data for SQ")
    else:
        print("(212/503) No data returned for SQ. Skipping.")
        failed_tickers.append('SQ')
except Exception as e:
    print(f"(212/503) Failed to fetch data for SQ: {e}")
    failed_tickers.append('SQ')

# Ticker 213: CBRE
try:
    data_cbre = tv.get_hist(symbol='CBRE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cbre is not None and not data_cbre.empty:
        all_data['CBRE'] = data_cbre['close']
        print("(213/503) Successfully fetched data for CBRE")
    else:
        print("(213/503) No data returned for CBRE. Skipping.")
        failed_tickers.append('CBRE')
except Exception as e:
    print(f"(213/503) Failed to fetch data for CBRE: {e}")
    failed_tickers.append('CBRE')

# Ticker 214: CCI
try:
    data_cci = tv.get_hist(symbol='CCI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cci is not None and not data_cci.empty:
        all_data['CCI'] = data_cci['close']
        print("(214/503) Successfully fetched data for CCI")
    else:
        print("(214/503) No data returned for CCI. Skipping.")
        failed_tickers.append('CCI')
except Exception as e:
    print(f"(214/503) Failed to fetch data for CCI: {e}")
    failed_tickers.append('CCI')

# Ticker 215: TGT
try:
    data_tgt = tv.get_hist(symbol='TGT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tgt is not None and not data_tgt.empty:
        all_data['TGT'] = data_tgt['close']
        print("(215/503) Successfully fetched data for TGT")
    else:
        print("(215/503) No data returned for TGT. Skipping.")
        failed_tickers.append('TGT')
except Exception as e:
    print(f"(215/503) Failed to fetch data for TGT: {e}")
    failed_tickers.append('TGT')

# Ticker 216: EW
try:
    data_ew = tv.get_hist(symbol='EW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ew is not None and not data_ew.empty:
        all_data['EW'] = data_ew['close']
        print("(216/503) Successfully fetched data for EW")
    else:
        print("(216/503) No data returned for EW. Skipping.")
        failed_tickers.append('EW')
except Exception as e:
    print(f"(216/503) Failed to fetch data for EW: {e}")
    failed_tickers.append('EW')

# Ticker 217: KR
try:
    data_kr = tv.get_hist(symbol='KR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kr is not None and not data_kr.empty:
        all_data['KR'] = data_kr['close']
        print("(217/503) Successfully fetched data for KR")
    else:
        print("(217/503) No data returned for KR. Skipping.")
        failed_tickers.append('KR')
except Exception as e:
    print(f"(217/503) Failed to fetch data for KR: {e}")
    failed_tickers.append('KR')

# Ticker 218: AIG
try:
    data_aig = tv.get_hist(symbol='AIG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aig is not None and not data_aig.empty:
        all_data['AIG'] = data_aig['close']
        print("(218/503) Successfully fetched data for AIG")
    else:
        print("(218/503) No data returned for AIG. Skipping.")
        failed_tickers.append('AIG')
except Exception as e:
    print(f"(218/503) Failed to fetch data for AIG: {e}")
    failed_tickers.append('AIG')

# Ticker 219: IDXX
try:
    data_idxx = tv.get_hist(symbol='IDXX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_idxx is not None and not data_idxx.empty:
        all_data['IDXX'] = data_idxx['close']
        print("(219/503) Successfully fetched data for IDXX")
    else:
        print("(219/503) No data returned for IDXX. Skipping.")
        failed_tickers.append('IDXX')
except Exception as e:
    print(f"(219/503) Failed to fetch data for IDXX: {e}")
    failed_tickers.append('IDXX')

# Ticker 220: KDP
try:
    data_kdp = tv.get_hist(symbol='KDP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_kdp is not None and not data_kdp.empty:
        all_data['KDP'] = data_kdp['close']
        print("(220/503) Successfully fetched data for KDP")
    else:
        print("(220/503) No data returned for KDP. Skipping.")
        failed_tickers.append('KDP')
except Exception as e:
    print(f"(220/503) Failed to fetch data for KDP: {e}")
    failed_tickers.append('KDP')

# Ticker 221: ROST
try:
    data_rost = tv.get_hist(symbol='ROST', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_rost is not None and not data_rost.empty:
        all_data['ROST'] = data_rost['close']
        print("(221/503) Successfully fetched data for ROST")
    else:
        print("(221/503) No data returned for ROST. Skipping.")
        failed_tickers.append('ROST')
except Exception as e:
    print(f"(221/503) Failed to fetch data for ROST: {e}")
    failed_tickers.append('ROST')

# Ticker 222: GRMN
try:
    data_grmn = tv.get_hist(symbol='GRMN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_grmn is not None and not data_grmn.empty:
        all_data['GRMN'] = data_grmn['close']
        print("(222/503) Successfully fetched data for GRMN")
    else:
        print("(222/503) No data returned for GRMN. Skipping.")
        failed_tickers.append('GRMN')
except Exception as e:
    print(f"(222/503) Failed to fetch data for GRMN: {e}")
    failed_tickers.append('GRMN')

# Ticker 223: BKR
try:
    data_bkr = tv.get_hist(symbol='BKR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_bkr is not None and not data_bkr.empty:
        all_data['BKR'] = data_bkr['close']
        print("(223/503) Successfully fetched data for BKR")
    else:
        print("(223/503) No data returned for BKR. Skipping.")
        failed_tickers.append('BKR')
except Exception as e:
    print(f"(223/503) Failed to fetch data for BKR: {e}")
    failed_tickers.append('BKR')

# Ticker 224: CPRT
try:
    data_cprt = tv.get_hist(symbol='CPRT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cprt is not None and not data_cprt.empty:
        all_data['CPRT'] = data_cprt['close']
        print("(224/503) Successfully fetched data for CPRT")
    else:
        print("(224/503) No data returned for CPRT. Skipping.")
        failed_tickers.append('CPRT')
except Exception as e:
    print(f"(224/503) Failed to fetch data for CPRT: {e}")
    failed_tickers.append('CPRT')

# Ticker 225: EXC
try:
    data_exc = tv.get_hist(symbol='EXC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_exc is not None and not data_exc.empty:
        all_data['EXC'] = data_exc['close']
        print("(225/503) Successfully fetched data for EXC")
    else:
        print("(225/503) No data returned for EXC. Skipping.")
        failed_tickers.append('EXC')
except Exception as e:
    print(f"(225/503) Failed to fetch data for EXC: {e}")
    failed_tickers.append('EXC')


# --- EXPORT CHUNK 9 (TICKERS 201-225) ---
print("\n--- Merging and exporting data for companies 201-225 ---")
chunk_9_data = {}
tickers_201_225 = {
    'DDOG': 'data_ddog', 'ALL': 'data_all', 'PSX': 'data_psx', 'PSA': 'data_psa', 'LHX': 'data_lhx', 'GWW': 'data_gww', 'CMI': 'data_cmi', 'GM': 'data_gm', 'D': 'data_d', 'CTVA': 'data_ctva', 'AMP': 'data_amp', 'SQ': 'data_sq', 'CBRE': 'data_cbre', 'CCI': 'data_cci', 'TGT': 'data_tgt', 'EW': 'data_ew', 'KR': 'data_kr', 'AIG': 'data_aig', 'IDXX': 'data_idxx', 'KDP': 'data_kdp', 'ROST': 'data_rost', 'GRMN': 'data_grmn', 'BKR': 'data_bkr', 'CPRT': 'data_cprt', 'EXC': 'data_exc'
}
for ticker, data_var_name in tickers_201_225.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_9_data[ticker] = close_series
if chunk_9_data:
    price_df_9 = pd.DataFrame(chunk_9_data)
    price_df_9.sort_index(inplace=True)
    price_df_9.ffill(inplace=True)
    price_df_9.to_csv('sp500_prices_201-225.csv')
    print("--- Successfully exported sp500_prices_201-225.csv ---\n")
else:
    print("--- No data collected for chunk 9, skipping export. ---\n")
    
    

# Ticker 226: VLO
try:
    data_vlo = tv.get_hist(symbol='VLO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vlo is not None and not data_vlo.empty:
        all_data['VLO'] = data_vlo['close']
        print("(226/503) Successfully fetched data for VLO")
    else:
        print("(226/503) No data returned for VLO. Skipping.")
        failed_tickers.append('VLO')
except Exception as e:
    print(f"(226/503) Failed to fetch data for VLO: {e}")
    failed_tickers.append('VLO')

# Ticker 227: F
try:
    data_f = tv.get_hist(symbol='F', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_f is not None and not data_f.empty:
        all_data['F'] = data_f['close']
        print("(227/503) Successfully fetched data for F")
    else:
        print("(227/503) No data returned for F. Skipping.")
        failed_tickers.append('F')
except Exception as e:
    print(f"(227/503) Failed to fetch data for F: {e}")
    failed_tickers.append('F')

# Ticker 228: PEG
try:
    data_peg = tv.get_hist(symbol='PEG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_peg is not None and not data_peg.empty:
        all_data['PEG'] = data_peg['close']
        print("(228/503) Successfully fetched data for PEG")
    else:
        print("(228/503) No data returned for PEG. Skipping.")
        failed_tickers.append('PEG')
except Exception as e:
    print(f"(228/503) Failed to fetch data for PEG: {e}")
    failed_tickers.append('PEG')

# Ticker 229: OXY
try:
    data_oxy = tv.get_hist(symbol='OXY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_oxy is not None and not data_oxy.empty:
        all_data['OXY'] = data_oxy['close']
        print("(229/503) Successfully fetched data for OXY")
    else:
        print("(229/503) No data returned for OXY. Skipping.")
        failed_tickers.append('OXY')
except Exception as e:
    print(f"(229/503) Failed to fetch data for OXY: {e}")
    failed_tickers.append('OXY')

# Ticker 230: FANG
try:
    data_fang = tv.get_hist(symbol='FANG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_fang is not None and not data_fang.empty:
        all_data['FANG'] = data_fang['close']
        print("(230/503) Successfully fetched data for FANG")
    else:
        print("(230/503) No data returned for FANG. Skipping.")
        failed_tickers.append('FANG')
except Exception as e:
    print(f"(230/503) Failed to fetch data for FANG: {e}")
    failed_tickers.append('FANG')

# Ticker 231: DHI
try:
    data_dhi = tv.get_hist(symbol='DHI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dhi is not None and not data_dhi.empty:
        all_data['DHI'] = data_dhi['close']
        print("(231/503) Successfully fetched data for DHI")
    else:
        print("(231/503) No data returned for DHI. Skipping.")
        failed_tickers.append('DHI')
except Exception as e:
    print(f"(231/503) Failed to fetch data for DHI: {e}")
    failed_tickers.append('DHI')

# Ticker 232: MSCI
try:
    data_msci = tv.get_hist(symbol='MSCI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_msci is not None and not data_msci.empty:
        all_data['MSCI'] = data_msci['close']
        print("(232/503) Successfully fetched data for MSCI")
    else:
        print("(232/503) No data returned for MSCI. Skipping.")
        failed_tickers.append('MSCI')
except Exception as e:
    print(f"(232/503) Failed to fetch data for MSCI: {e}")
    failed_tickers.append('MSCI')

# Ticker 233: FIS
try:
    data_fis = tv.get_hist(symbol='FIS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fis is not None and not data_fis.empty:
        all_data['FIS'] = data_fis['close']
        print("(233/503) Successfully fetched data for FIS")
    else:
        print("(233/503) No data returned for FIS. Skipping.")
        failed_tickers.append('FIS')
except Exception as e:
    print(f"(233/503) Failed to fetch data for FIS: {e}")
    failed_tickers.append('FIS')

# Ticker 234: KMB
try:
    data_kmb = tv.get_hist(symbol='KMB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_kmb is not None and not data_kmb.empty:
        all_data['KMB'] = data_kmb['close']
        print("(234/503) Successfully fetched data for KMB")
    else:
        print("(234/503) No data returned for KMB. Skipping.")
        failed_tickers.append('KMB')
except Exception as e:
    print(f"(234/503) Failed to fetch data for KMB: {e}")
    failed_tickers.append('KMB')

# Ticker 235: KVUE
try:
    data_kvue = tv.get_hist(symbol='KVUE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kvue is not None and not data_kvue.empty:
        all_data['KVUE'] = data_kvue['close']
        print("(235/503) Successfully fetched data for KVUE")
    else:
        print("(235/503) No data returned for KVUE. Skipping.")
        failed_tickers.append('KVUE')
except Exception as e:
    print(f"(235/503) Failed to fetch data for KVUE: {e}")
    failed_tickers.append('KVUE')

# Ticker 236: XEL
try:
    data_xel = tv.get_hist(symbol='XEL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_xel is not None and not data_xel.empty:
        all_data['XEL'] = data_xel['close']
        print("(236/503) Successfully fetched data for XEL")
    else:
        print("(236/503) No data returned for XEL. Skipping.")
        failed_tickers.append('XEL')
except Exception as e:
    print(f"(236/503) Failed to fetch data for XEL: {e}")
    failed_tickers.append('XEL')

# Ticker 237: VRSK
try:
    data_vrsk = tv.get_hist(symbol='VRSK', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_vrsk is not None and not data_vrsk.empty:
        all_data['VRSK'] = data_vrsk['close']
        print("(237/503) Successfully fetched data for VRSK")
    else:
        print("(237/503) No data returned for VRSK. Skipping.")
        failed_tickers.append('VRSK')
except Exception as e:
    print(f"(237/503) Failed to fetch data for VRSK: {e}")
    failed_tickers.append('VRSK')

# Ticker 238: AME
try:
    data_ame = tv.get_hist(symbol='AME', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ame is not None and not data_ame.empty:
        all_data['AME'] = data_ame['close']
        print("(238/503) Successfully fetched data for AME")
    else:
        print("(238/503) No data returned for AME. Skipping.")
        failed_tickers.append('AME')
except Exception as e:
    print(f"(238/503) Failed to fetch data for AME: {e}")
    failed_tickers.append('AME')

# Ticker 239: TTD
try:
    data_ttd = tv.get_hist(symbol='TTD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ttd is not None and not data_ttd.empty:
        all_data['TTD'] = data_ttd['close']
        print("(239/503) Successfully fetched data for TTD")
    else:
        print("(239/503) No data returned for TTD. Skipping.")
        failed_tickers.append('TTD')
except Exception as e:
    print(f"(239/503) Failed to fetch data for TTD: {e}")
    failed_tickers.append('TTD')

# Ticker 240: TTWO
try:
    data_ttwo = tv.get_hist(symbol='TTWO', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ttwo is not None and not data_ttwo.empty:
        all_data['TTWO'] = data_ttwo['close']
        print("(240/503) Successfully fetched data for TTWO")
    else:
        print("(240/503) No data returned for TTWO. Skipping.")
        failed_tickers.append('TTWO')
except Exception as e:
    print(f"(240/503) Failed to fetch data for TTWO: {e}")
    failed_tickers.append('TTWO')

# Ticker 241: RMD
try:
    data_rmd = tv.get_hist(symbol='RMD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rmd is not None and not data_rmd.empty:
        all_data['RMD'] = data_rmd['close']
        print("(241/503) Successfully fetched data for RMD")
    else:
        print("(241/503) No data returned for RMD. Skipping.")
        failed_tickers.append('RMD')
except Exception as e:
    print(f"(241/503) Failed to fetch data for RMD: {e}")
    failed_tickers.append('RMD')

# Ticker 242: YUM
try:
    data_yum = tv.get_hist(symbol='YUM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_yum is not None and not data_yum.empty:
        all_data['YUM'] = data_yum['close']
        print("(242/503) Successfully fetched data for YUM")
    else:
        print("(242/503) No data returned for YUM. Skipping.")
        failed_tickers.append('YUM')
except Exception as e:
    print(f"(242/503) Failed to fetch data for YUM: {e}")
    failed_tickers.append('YUM')

# Ticker 243: CSGP
try:
    data_csgp = tv.get_hist(symbol='CSGP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_csgp is not None and not data_csgp.empty:
        all_data['CSGP'] = data_csgp['close']
        print("(243/503) Successfully fetched data for CSGP")
    else:
        print("(243/503) No data returned for CSGP. Skipping.")
        failed_tickers.append('CSGP')
except Exception as e:
    print(f"(243/503) Failed to fetch data for CSGP: {e}")
    failed_tickers.append('CSGP')

# Ticker 244: CCL
try:
    data_ccl = tv.get_hist(symbol='CCL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ccl is not None and not data_ccl.empty:
        all_data['CCL'] = data_ccl['close']
        print("(244/503) Successfully fetched data for CCL")
    else:
        print("(244/503) No data returned for CCL. Skipping.")
        failed_tickers.append('CCL')
except Exception as e:
    print(f"(244/503) Failed to fetch data for CCL: {e}")
    failed_tickers.append('CCL')

# Ticker 245: ROK
try:
    data_rok = tv.get_hist(symbol='ROK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rok is not None and not data_rok.empty:
        all_data['ROK'] = data_rok['close']
        print("(245/503) Successfully fetched data for ROK")
    else:
        print("(245/503) No data returned for ROK. Skipping.")
        failed_tickers.append('ROK')
except Exception as e:
    print(f"(245/503) Failed to fetch data for ROK: {e}")
    failed_tickers.append('ROK')

# Ticker 246: ETR
try:
    data_etr = tv.get_hist(symbol='ETR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_etr is not None and not data_etr.empty:
        all_data['ETR'] = data_etr['close']
        print("(246/503) Successfully fetched data for ETR")
    else:
        print("(246/503) No data returned for ETR. Skipping.")
        failed_tickers.append('ETR')
except Exception as e:
    print(f"(246/503) Failed to fetch data for ETR: {e}")
    failed_tickers.append('ETR')

# Ticker 247: CHTR
try:
    data_chtr = tv.get_hist(symbol='CHTR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_chtr is not None and not data_chtr.empty:
        all_data['CHTR'] = data_chtr['close']
        print("(247/503) Successfully fetched data for CHTR")
    else:
        print("(247/503) No data returned for CHTR. Skipping.")
        failed_tickers.append('CHTR')
except Exception as e:
    print(f"(247/503) Failed to fetch data for CHTR: {e}")
    failed_tickers.append('CHTR')

# Ticker 248: SYY
try:
    data_syy = tv.get_hist(symbol='SYY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_syy is not None and not data_syy.empty:
        all_data['SYY'] = data_syy['close']
        print("(248/503) Successfully fetched data for SYY")
    else:
        print("(248/503) No data returned for SYY. Skipping.")
        failed_tickers.append('SYY')
except Exception as e:
    print(f"(248/503) Failed to fetch data for SYY: {e}")
    failed_tickers.append('SYY')

# Ticker 249: MCHP
try:
    data_mchp = tv.get_hist(symbol='MCHP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mchp is not None and not data_mchp.empty:
        all_data['MCHP'] = data_mchp['close']
        print("(249/503) Successfully fetched data for MCHP")
    else:
        print("(249/503) No data returned for MCHP. Skipping.")
        failed_tickers.append('MCHP')
except Exception as e:
    print(f"(249/503) Failed to fetch data for MCHP: {e}")
    failed_tickers.append('MCHP')

# Ticker 250: CAH
try:
    data_cah = tv.get_hist(symbol='CAH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cah is not None and not data_cah.empty:
        all_data['CAH'] = data_cah['close']
        print("(250/503) Successfully fetched data for CAH")
    else:
        print("(250/503) No data returned for CAH. Skipping.")
        failed_tickers.append('CAH')
except Exception as e:
    print(f"(250/503) Failed to fetch data for CAH: {e}")
    failed_tickers.append('CAH')

# --- EXPORT CHUNK 10 (TICKERS 226-250) ---
print("\n--- Merging and exporting data for companies 226-250 ---")
chunk_10_data = {}
tickers_226_250 = {
    'VLO': 'data_vlo', 'F': 'data_f', 'PEG': 'data_peg', 'OXY': 'data_oxy', 'FANG': 'data_fang', 'DHI': 'data_dhi', 'MSCI': 'data_msci', 'FIS': 'data_fis', 'KMB': 'data_kmb', 'KVUE': 'data_kvue', 'XEL': 'data_xel', 'VRSK': 'data_vrsk', 'AME': 'data_ame', 'TTD': 'data_ttd', 'TTWO': 'data_ttwo', 'RMD': 'data_rmd', 'YUM': 'data_yum', 'CSGP': 'data_csgp', 'CCL': 'data_ccl', 'ROK': 'data_rok', 'ETR': 'data_etr', 'CHTR': 'data_chtr', 'SYY': 'data_syy', 'MCHP': 'data_mchp', 'CAH': 'data_cah'
}
for ticker, data_var_name in tickers_226_250.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_10_data[ticker] = close_series
if chunk_10_data:
    price_df_10 = pd.DataFrame(chunk_10_data)
    price_df_10.sort_index(inplace=True)
    price_df_10.ffill(inplace=True)
    price_df_10.to_csv('sp500_prices_226-250.csv')
    print("--- Successfully exported sp500_prices_226-250.csv ---\n")
else:
    print("--- No data collected for chunk 10, skipping export. ---\n")

# Ticker 251: HSY
try:
    data_hsy = tv.get_hist(symbol='HSY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hsy is not None and not data_hsy.empty:
        all_data['HSY'] = data_hsy['close']
        print("(251/503) Successfully fetched data for HSY")
    else:
        print("(251/503) No data returned for HSY. Skipping.")
        failed_tickers.append('HSY')
except Exception as e:
    print(f"(251/503) Failed to fetch data for HSY: {e}")
    failed_tickers.append('HSY')

# Ticker 252: EA
try:
    data_ea = tv.get_hist(symbol='EA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ea is not None and not data_ea.empty:
        all_data['EA'] = data_ea['close']
        print("(252/503) Successfully fetched data for EA")
    else:
        print("(252/503) No data returned for EA. Skipping.")
        failed_tickers.append('EA')
except Exception as e:
    print(f"(252/503) Failed to fetch data for EA: {e}")
    failed_tickers.append('EA')

# Ticker 253: CTSH
try:
    data_ctsh = tv.get_hist(symbol='CTSH', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ctsh is not None and not data_ctsh.empty:
        all_data['CTSH'] = data_ctsh['close']
        print("(253/503) Successfully fetched data for CTSH")
    else:
        print("(253/503) No data returned for CTSH. Skipping.")
        failed_tickers.append('CTSH')
except Exception as e:
    print(f"(253/503) Failed to fetch data for CTSH: {e}")
    failed_tickers.append('CTSH')

# Ticker 254: LVS
try:
    data_lvs = tv.get_hist(symbol='LVS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lvs is not None and not data_lvs.empty:
        all_data['LVS'] = data_lvs['close']
        print("(254/503) Successfully fetched data for LVS")
    else:
        print("(254/503) No data returned for LVS. Skipping.")
        failed_tickers.append('LVS')
except Exception as e:
    print(f"(254/503) Failed to fetch data for LVS: {e}")
    failed_tickers.append('LVS')

# Ticker 255: ED
try:
    data_ed = tv.get_hist(symbol='ED', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ed is not None and not data_ed.empty:
        all_data['ED'] = data_ed['close']
        print("(255/503) Successfully fetched data for ED")
    else:
        print("(255/503) No data returned for ED. Skipping.")
        failed_tickers.append('ED')
except Exception as e:
    print(f"(255/503) Failed to fetch data for ED: {e}")
    failed_tickers.append('ED')

# Ticker 256: FICO
try:
    data_fico = tv.get_hist(symbol='FICO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fico is not None and not data_fico.empty:
        all_data['FICO'] = data_fico['close']
        print("(256/503) Successfully fetched data for FICO")
    else:
        print("(256/503) No data returned for FICO. Skipping.")
        failed_tickers.append('FICO')
except Exception as e:
    print(f"(256/503) Failed to fetch data for FICO: {e}")
    failed_tickers.append('FICO')

# Ticker 257: PRU
try:
    data_pru = tv.get_hist(symbol='PRU', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pru is not None and not data_pru.empty:
        all_data['PRU'] = data_pru['close']
        print("(257/503) Successfully fetched data for PRU")
    else:
        print("(257/503) No data returned for PRU. Skipping.")
        failed_tickers.append('PRU')
except Exception as e:
    print(f"(257/503) Failed to fetch data for PRU: {e}")
    failed_tickers.append('PRU')

# Ticker 258: TRGP
try:
    data_trgp = tv.get_hist(symbol='TRGP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_trgp is not None and not data_trgp.empty:
        all_data['TRGP'] = data_trgp['close']
        print("(258/503) Successfully fetched data for TRGP")
    else:
        print("(258/503) No data returned for TRGP. Skipping.")
        failed_tickers.append('TRGP')
except Exception as e:
    print(f"(258/503) Failed to fetch data for TRGP: {e}")
    failed_tickers.append('TRGP')

# Ticker 259: VMC
try:
    data_vmc = tv.get_hist(symbol='VMC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vmc is not None and not data_vmc.empty:
        all_data['VMC'] = data_vmc['close']
        print("(259/503) Successfully fetched data for VMC")
    else:
        print("(259/503) No data returned for VMC. Skipping.")
        failed_tickers.append('VMC')
except Exception as e:
    print(f"(259/503) Failed to fetch data for VMC: {e}")
    failed_tickers.append('VMC')

# Ticker 260: EBAY
try:
    data_ebay = tv.get_hist(symbol='EBAY', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ebay is not None and not data_ebay.empty:
        all_data['EBAY'] = data_ebay['close']
        print("(260/503) Successfully fetched data for EBAY")
    else:
        print("(260/503) No data returned for EBAY. Skipping.")
        failed_tickers.append('EBAY')
except Exception as e:
    print(f"(260/503) Failed to fetch data for EBAY: {e}")
    failed_tickers.append('EBAY')

# Ticker 261: DAL
try:
    data_dal = tv.get_hist(symbol='DAL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dal is not None and not data_dal.empty:
        all_data['DAL'] = data_dal['close']
        print("(261/503) Successfully fetched data for DAL")
    else:
        print("(261/503) No data returned for DAL. Skipping.")
        failed_tickers.append('DAL')
except Exception as e:
    print(f"(261/503) Failed to fetch data for DAL: {e}")
    failed_tickers.append('DAL')

# Ticker 262: HIG
try:
    data_hig = tv.get_hist(symbol='HIG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hig is not None and not data_hig.empty:
        all_data['HIG'] = data_hig['close']
        print("(262/503) Successfully fetched data for HIG")
    else:
        print("(262/503) No data returned for HIG. Skipping.")
        failed_tickers.append('HIG')
except Exception as e:
    print(f"(262/503) Failed to fetch data for HIG: {e}")
    failed_tickers.append('HIG')

# Ticker 263: GEHC
try:
    data_gehc = tv.get_hist(symbol='GEHC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_gehc is not None and not data_gehc.empty:
        all_data['GEHC'] = data_gehc['close']
        print("(263/503) Successfully fetched data for GEHC")
    else:
        print("(263/503) No data returned for GEHC. Skipping.")
        failed_tickers.append('GEHC')
except Exception as e:
    print(f"(263/503) Failed to fetch data for GEHC: {e}")
    failed_tickers.append('GEHC')

# Ticker 264: SMCI
try:
    data_smci = tv.get_hist(symbol='SMCI', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_smci is not None and not data_smci.empty:
        all_data['SMCI'] = data_smci['close']
        print("(264/503) Successfully fetched data for SMCI")
    else:
        print("(264/503) No data returned for SMCI. Skipping.")
        failed_tickers.append('SMCI')
except Exception as e:
    print(f"(264/503) Failed to fetch data for SMCI: {e}")
    failed_tickers.append('SMCI')

# Ticker 265: DXCM
try:
    data_dxcm = tv.get_hist(symbol='DXCM', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_dxcm is not None and not data_dxcm.empty:
        all_data['DXCM'] = data_dxcm['close']
        print("(265/503) Successfully fetched data for DXCM")
    else:
        print("(265/503) No data returned for DXCM. Skipping.")
        failed_tickers.append('DXCM')
except Exception as e:
    print(f"(265/503) Failed to fetch data for DXCM: {e}")
    failed_tickers.append('DXCM')

# Ticker 266: IR
try:
    data_ir = tv.get_hist(symbol='IR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ir is not None and not data_ir.empty:
        all_data['IR'] = data_ir['close']
        print("(266/503) Successfully fetched data for IR")
    else:
        print("(266/503) No data returned for IR. Skipping.")
        failed_tickers.append('IR')
except Exception as e:
    print(f"(266/503) Failed to fetch data for IR: {e}")
    failed_tickers.append('IR')

# Ticker 267: LYV
try:
    data_lyv = tv.get_hist(symbol='LYV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lyv is not None and not data_lyv.empty:
        all_data['LYV'] = data_lyv['close']
        print("(267/503) Successfully fetched data for LYV")
    else:
        print("(267/503) No data returned for LYV. Skipping.")
        failed_tickers.append('LYV')
except Exception as e:
    print(f"(267/503) Failed to fetch data for LYV: {e}")
    failed_tickers.append('LYV')

# Ticker 268: MLM
try:
    data_mlm = tv.get_hist(symbol='MLM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mlm is not None and not data_mlm.empty:
        all_data['MLM'] = data_mlm['close']
        print("(268/503) Successfully fetched data for MLM")
    else:
        print("(268/503) No data returned for MLM. Skipping.")
        failed_tickers.append('MLM')
except Exception as e:
    print(f"(268/503) Failed to fetch data for MLM: {e}")
    failed_tickers.append('MLM')

# Ticker 269: VICI
try:
    data_vici = tv.get_hist(symbol='VICI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vici is not None and not data_vici.empty:
        all_data['VICI'] = data_vici['close']
        print("(269/503) Successfully fetched data for VICI")
    else:
        print("(269/503) No data returned for VICI. Skipping.")
        failed_tickers.append('VICI')
except Exception as e:
    print(f"(269/503) Failed to fetch data for VICI: {e}")
    failed_tickers.append('VICI')

# Ticker 270: WEC
try:
    data_wec = tv.get_hist(symbol='WEC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wec is not None and not data_wec.empty:
        all_data['WEC'] = data_wec['close']
        print("(270/503) Successfully fetched data for WEC")
    else:
        print("(270/503) No data returned for WEC. Skipping.")
        failed_tickers.append('WEC')
except Exception as e:
    print(f"(270/503) Failed to fetch data for WEC: {e}")
    failed_tickers.append('WEC')

# Ticker 271: MPWR
try:
    data_mpwr = tv.get_hist(symbol='MPWR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mpwr is not None and not data_mpwr.empty:
        all_data['MPWR'] = data_mpwr['close']
        print("(271/503) Successfully fetched data for MPWR")
    else:
        print("(271/503) No data returned for MPWR. Skipping.")
        failed_tickers.append('MPWR')
except Exception as e:
    print(f"(271/503) Failed to fetch data for MPWR: {e}")
    failed_tickers.append('MPWR')

# Ticker 272: OTIS
try:
    data_otis = tv.get_hist(symbol='OTIS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_otis is not None and not data_otis.empty:
        all_data['OTIS'] = data_otis['close']
        print("(272/503) Successfully fetched data for OTIS")
    else:
        print("(272/503) No data returned for OTIS. Skipping.")
        failed_tickers.append('OTIS')
except Exception as e:
    print(f"(272/503) Failed to fetch data for OTIS: {e}")
    failed_tickers.append('OTIS')

# Ticker 273: ODFL
try:
    data_odfl = tv.get_hist(symbol='ODFL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_odfl is not None and not data_odfl.empty:
        all_data['ODFL'] = data_odfl['close']
        print("(273/503) Successfully fetched data for ODFL")
    else:
        print("(273/503) No data returned for ODFL. Skipping.")
        failed_tickers.append('ODFL')
except Exception as e:
    print(f"(273/503) Failed to fetch data for ODFL: {e}")
    failed_tickers.append('ODFL')

# Ticker 274: A
try:
    data_a = tv.get_hist(symbol='A', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_a is not None and not data_a.empty:
        all_data['A'] = data_a['close']
        print("(274/503) Successfully fetched data for A")
    else:
        print("(274/503) No data returned for A. Skipping.")
        failed_tickers.append('A')
except Exception as e:
    print(f"(274/503) Failed to fetch data for A: {e}")
    failed_tickers.append('A')

# Ticker 275: KHC
try:
    data_khc = tv.get_hist(symbol='KHC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_khc is not None and not data_khc.empty:
        all_data['KHC'] = data_khc['close']
        print("(275/503) Successfully fetched data for KHC")
    else:
        print("(275/503) No data returned for KHC. Skipping.")
        failed_tickers.append('KHC')
except Exception as e:
    print(f"(275/503) Failed to fetch data for KHC: {e}")
    failed_tickers.append('KHC')

# --- EXPORT CHUNK 11 (TICKERS 251-275) ---
print("\n--- Merging and exporting data for companies 251-275 ---")
chunk_11_data = {}
tickers_251_275 = {
    'HSY': 'data_hsy', 'EA': 'data_ea', 'CTSH': 'data_ctsh', 'LVS': 'data_lvs', 'ED': 'data_ed', 'FICO': 'data_fico', 'PRU': 'data_pru', 'TRGP': 'data_trgp', 'VMC': 'data_vmc', 'EBAY': 'data_ebay', 'DAL': 'data_dal', 'HIG': 'data_hig', 'GEHC': 'data_gehc', 'SMCI': 'data_smci', 'DXCM': 'data_dxcm', 'IR': 'data_ir', 'LYV': 'data_lyv', 'MLM': 'data_mlm', 'VICI': 'data_vici', 'WEC': 'data_wec', 'MPWR': 'data_mpwr', 'OTIS': 'data_otis', 'ODFL': 'data_odfl', 'A': 'data_a', 'KHC': 'data_khc'
}
for ticker, data_var_name in tickers_251_275.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_11_data[ticker] = close_series
if chunk_11_data:
    price_df_11 = pd.DataFrame(chunk_11_data)
    price_df_11.sort_index(inplace=True)
    price_df_11.ffill(inplace=True)
    price_df_11.to_csv('sp500_prices_251-275.csv')
    print("--- Successfully exported sp500_prices_251-275.csv ---\n")
else:
    print("--- No data collected for chunk 11, skipping export. ---\n")

# Ticker 276: RJF
try:
    data_rjf = tv.get_hist(symbol='RJF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rjf is not None and not data_rjf.empty:
        all_data['RJF'] = data_rjf['close']
        print("(276/503) Successfully fetched data for RJF")
    else:
        print("(276/503) No data returned for RJF. Skipping.")
        failed_tickers.append('RJF')
except Exception as e:
    print(f"(276/503) Failed to fetch data for RJF: {e}")
    failed_tickers.append('RJF')

# Ticker 277: EQT
try:
    data_eqt = tv.get_hist(symbol='EQT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_eqt is not None and not data_eqt.empty:
        all_data['EQT'] = data_eqt['close']
        print("(277/503) Successfully fetched data for EQT")
    else:
        print("(277/503) No data returned for EQT. Skipping.")
        failed_tickers.append('EQT')
except Exception as e:
    print(f"(277/503) Failed to fetch data for EQT: {e}")
    failed_tickers.append('EQT')

# Ticker 278: WAB
try:
    data_wab = tv.get_hist(symbol='WAB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wab is not None and not data_wab.empty:
        all_data['WAB'] = data_wab['close']
        print("(278/503) Successfully fetched data for WAB")
    else:
        print("(278/503) No data returned for WAB. Skipping.")
        failed_tickers.append('WAB')
except Exception as e:
    print(f"(278/503) Failed to fetch data for WAB: {e}")
    failed_tickers.append('WAB')

# Ticker 279: IQV
try:
    data_iqv = tv.get_hist(symbol='IQV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_iqv is not None and not data_iqv.empty:
        all_data['IQV'] = data_iqv['close']
        print("(279/503) Successfully fetched data for IQV")
    else:
        print("(279/503) No data returned for IQV. Skipping.")
        failed_tickers.append('IQV')
except Exception as e:
    print(f"(279/503) Failed to fetch data for IQV: {e}")
    failed_tickers.append('IQV')

# Ticker 280: EL
try:
    data_el = tv.get_hist(symbol='EL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_el is not None and not data_el.empty:
        all_data['EL'] = data_el['close']
        print("(280/503) Successfully fetched data for EL")
    else:
        print("(280/503) No data returned for EL. Skipping.")
        failed_tickers.append('EL')
except Exception as e:
    print(f"(280/503) Failed to fetch data for EL: {e}")
    failed_tickers.append('EL')

# Ticker 281: WBD
try:
    data_wbd = tv.get_hist(symbol='WBD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wbd is not None and not data_wbd.empty:
        all_data['WBD'] = data_wbd['close']
        print("(281/503) Successfully fetched data for WBD")
    else:
        print("(281/503) No data returned for WBD. Skipping.")
        failed_tickers.append('WBD')
except Exception as e:
    print(f"(281/503) Failed to fetch data for WBD: {e}")
    failed_tickers.append('WBD')

# Ticker 282: ACGL
try:
    data_acgl = tv.get_hist(symbol='ACGL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_acgl is not None and not data_acgl.empty:
        all_data['ACGL'] = data_acgl['close']
        print("(282/503) Successfully fetched data for ACGL")
    else:
        print("(282/503) No data returned for ACGL. Skipping.")
        failed_tickers.append('ACGL')
except Exception as e:
    print(f"(282/503) Failed to fetch data for ACGL: {e}")
    failed_tickers.append('ACGL')

# Ticker 283: STX
try:
    data_stx = tv.get_hist(symbol='STX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_stx is not None and not data_stx.empty:
        all_data['STX'] = data_stx['close']
        print("(283/503) Successfully fetched data for STX")
    else:
        print("(283/503) No data returned for STX. Skipping.")
        failed_tickers.append('STX')
except Exception as e:
    print(f"(283/503) Failed to fetch data for STX: {e}")
    failed_tickers.append('STX')

# Ticker 284: STT
try:
    data_stt = tv.get_hist(symbol='STT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_stt is not None and not data_stt.empty:
        all_data['STT'] = data_stt['close']
        print("(284/503) Successfully fetched data for STT")
    else:
        print("(284/503) No data returned for STT. Skipping.")
        failed_tickers.append('STT')
except Exception as e:
    print(f"(284/503) Failed to fetch data for STT: {e}")
    failed_tickers.append('STT')

# Ticker 285: XYL
try:
    data_xyl = tv.get_hist(symbol='XYL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_xyl is not None and not data_xyl.empty:
        all_data['XYL'] = data_xyl['close']
        print("(285/503) Successfully fetched data for XYL")
    else:
        print("(285/503) No data returned for XYL. Skipping.")
        failed_tickers.append('XYL')
except Exception as e:
    print(f"(285/503) Failed to fetch data for XYL: {e}")
    failed_tickers.append('XYL')

# Ticker 286: EXR
try:
    data_exr = tv.get_hist(symbol='EXR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_exr is not None and not data_exr.empty:
        all_data['EXR'] = data_exr['close']
        print("(286/503) Successfully fetched data for EXR")
    else:
        print("(286/503) No data returned for EXR. Skipping.")
        failed_tickers.append('EXR')
except Exception as e:
    print(f"(286/503) Failed to fetch data for EXR: {e}")
    failed_tickers.append('EXR')

# Ticker 287: NUE
try:
    data_nue = tv.get_hist(symbol='NUE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nue is not None and not data_nue.empty:
        all_data['NUE'] = data_nue['close']
        print("(287/503) Successfully fetched data for NUE")
    else:
        print("(287/503) No data returned for NUE. Skipping.")
        failed_tickers.append('NUE')
except Exception as e:
    print(f"(287/503) Failed to fetch data for NUE: {e}")
    failed_tickers.append('NUE')

# Ticker 288: DD
try:
    data_dd = tv.get_hist(symbol='DD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dd is not None and not data_dd.empty:
        all_data['DD'] = data_dd['close']
        print("(288/503) Successfully fetched data for DD")
    else:
        print("(288/503) No data returned for DD. Skipping.")
        failed_tickers.append('DD')
except Exception as e:
    print(f"(288/503) Failed to fetch data for DD: {e}")
    failed_tickers.append('DD')

# Ticker 289: TSCO
try:
    data_tsco = tv.get_hist(symbol='TSCO', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_tsco is not None and not data_tsco.empty:
        all_data['TSCO'] = data_tsco['close']
        print("(289/503) Successfully fetched data for TSCO")
    else:
        print("(289/503) No data returned for TSCO. Skipping.")
        failed_tickers.append('TSCO')
except Exception as e:
    print(f"(289/503) Failed to fetch data for TSCO: {e}")
    failed_tickers.append('TSCO')

# Ticker 290: STZ
try:
    data_stz = tv.get_hist(symbol='STZ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_stz is not None and not data_stz.empty:
        all_data['STZ'] = data_stz['close']
        print("(290/503) Successfully fetched data for STZ")
    else:
        print("(290/503) No data returned for STZ. Skipping.")
        failed_tickers.append('STZ')
except Exception as e:
    print(f"(290/503) Failed to fetch data for STZ: {e}")
    failed_tickers.append('STZ')

# Ticker 291: NRG
try:
    data_nrg = tv.get_hist(symbol='NRG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nrg is not None and not data_nrg.empty:
        all_data['NRG'] = data_nrg['close']
        print("(291/503) Successfully fetched data for NRG")
    else:
        print("(291/503) No data returned for NRG. Skipping.")
        failed_tickers.append('NRG')
except Exception as e:
    print(f"(291/503) Failed to fetch data for NRG: {e}")
    failed_tickers.append('NRG')

# Ticker 292: PCG
try:
    data_pcg = tv.get_hist(symbol='PCG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pcg is not None and not data_pcg.empty:
        all_data['PCG'] = data_pcg['close']
        print("(292/503) Successfully fetched data for PCG")
    else:
        print("(292/503) No data returned for PCG. Skipping.")
        failed_tickers.append('PCG')
except Exception as e:
    print(f"(292/503) Failed to fetch data for PCG: {e}")
    failed_tickers.append('PCG')

# Ticker 293: BRO
try:
    data_bro = tv.get_hist(symbol='BRO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bro is not None and not data_bro.empty:
        all_data['BRO'] = data_bro['close']
        print("(293/503) Successfully fetched data for BRO")
    else:
        print("(293/503) No data returned for BRO. Skipping.")
        failed_tickers.append('BRO')
except Exception as e:
    print(f"(293/503) Failed to fetch data for BRO: {e}")
    failed_tickers.append('BRO')

# Ticker 294: MTB
try:
    data_mtb = tv.get_hist(symbol='MTB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mtb is not None and not data_mtb.empty:
        all_data['MTB'] = data_mtb['close']
        print("(294/503) Successfully fetched data for MTB")
    else:
        print("(294/503) No data returned for MTB. Skipping.")
        failed_tickers.append('MTB')
except Exception as e:
    print(f"(294/503) Failed to fetch data for MTB: {e}")
    failed_tickers.append('MTB')

# Ticker 295: EFX
try:
    data_efx = tv.get_hist(symbol='EFX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_efx is not None and not data_efx.empty:
        all_data['EFX'] = data_efx['close']
        print("(295/503) Successfully fetched data for EFX")
    else:
        print("(295/503) No data returned for EFX. Skipping.")
        failed_tickers.append('EFX')
except Exception as e:
    print(f"(295/503) Failed to fetch data for EFX: {e}")
    failed_tickers.append('EFX')

# Ticker 296: VTR
try:
    data_vtr = tv.get_hist(symbol='VTR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vtr is not None and not data_vtr.empty:
        all_data['VTR'] = data_vtr['close']
        print("(296/503) Successfully fetched data for VTR")
    else:
        print("(296/503) No data returned for VTR. Skipping.")
        failed_tickers.append('VTR')
except Exception as e:
    print(f"(296/503) Failed to fetch data for VTR: {e}")
    failed_tickers.append('VTR')

# Ticker 297: WTW
try:
    data_wtw = tv.get_hist(symbol='WTW', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wtw is not None and not data_wtw.empty:
        all_data['WTW'] = data_wtw['close']
        print("(297/503) Successfully fetched data for WTW")
    else:
        print("(297/503) No data returned for WTW. Skipping.")
        failed_tickers.append('WTW')
except Exception as e:
    print(f"(297/503) Failed to fetch data for WTW: {e}")
    failed_tickers.append('WTW')

# Ticker 298: LEN
try:
    data_len = tv.get_hist(symbol='LEN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_len is not None and not data_len.empty:
        all_data['LEN'] = data_len['close']
        print("(298/503) Successfully fetched data for LEN")
    else:
        print("(298/503) No data returned for LEN. Skipping.")
        failed_tickers.append('LEN')
except Exception as e:
    print(f"(298/503) Failed to fetch data for LEN: {e}")
    failed_tickers.append('LEN')

# Ticker 299: UAL
try:
    data_ual = tv.get_hist(symbol='UAL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ual is not None and not data_ual.empty:
        all_data['UAL'] = data_ual['close']
        print("(299/503) Successfully fetched data for UAL")
    else:
        print("(299/503) No data returned for UAL. Skipping.")
        failed_tickers.append('UAL')
except Exception as e:
    print(f"(299/503) Failed to fetch data for UAL: {e}")
    failed_tickers.append('UAL')

# Ticker 300: BR
try:
    data_br = tv.get_hist(symbol='BR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_br is not None and not data_br.empty:
        all_data['BR'] = data_br['close']
        print("(300/503) Successfully fetched data for BR")
    else:
        print("(300/503) No data returned for BR. Skipping.")
        failed_tickers.append('BR')
except Exception as e:
    print(f"(300/503) Failed to fetch data for BR: {e}")
    failed_tickers.append('BR')

# --- EXPORT CHUNK 12 (TICKERS 276-300) ---
print("\n--- Merging and exporting data for companies 276-300 ---")
chunk_12_data = {}
tickers_276_300 = {
    'RJF': 'data_rjf', 'EQT': 'data_eqt', 'WAB': 'data_wab', 'IQV': 'data_iqv', 'EL': 'data_el', 'WBD': 'data_wbd', 'ACGL': 'data_acgl', 'STX': 'data_stx', 'STT': 'data_stt', 'XYL': 'data_xyl', 'EXR': 'data_exr', 'NUE': 'data_nue', 'DD': 'data_dd', 'TSCO': 'data_tsco', 'STZ': 'data_stz', 'NRG': 'data_nrg', 'PCG': 'data_pcg', 'BRO': 'data_bro', 'MTB': 'data_mtb', 'EFX': 'data_efx', 'VTR': 'data_vtr', 'WTW': 'data_wtw', 'LEN': 'data_len', 'UAL': 'data_ual', 'BR': 'data_br'
}
for ticker, data_var_name in tickers_276_300.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_12_data[ticker] = close_series
if chunk_12_data:
    price_df_12 = pd.DataFrame(chunk_12_data)
    price_df_12.sort_index(inplace=True)
    price_df_12.ffill(inplace=True)
    price_df_12.to_csv('sp500_prices_276-300.csv')
    print("--- Successfully exported sp500_prices_276-300.csv ---\n")
else:
    print("--- No data collected for chunk 12, skipping export. ---\n")

# Ticker 300: BR
try:
    data_br = tv.get_hist(symbol='BR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_br is not None and not data_br.empty:
        all_data['BR'] = data_br['close']
        print("(300/503) Successfully fetched data for BR")
    else:
        print("(300/503) No data returned for BR. Skipping.")
        failed_tickers.append('BR')
except Exception as e:
    print(f"(300/503) Failed to fetch data for BR: {e}")
    failed_tickers.append('BR')

# Ticker 301: IRM
try:
    data_irm = tv.get_hist(symbol='IRM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_irm is not None and not data_irm.empty:
        all_data['IRM'] = data_irm['close']
        print("(301/503) Successfully fetched data for IRM")
    else:
        print("(301/503) No data returned for IRM. Skipping.")
        failed_tickers.append('IRM')
except Exception as e:
    print(f"(301/503) Failed to fetch data for IRM: {e}")
    failed_tickers.append('IRM')

# Ticker 302: IP
try:
    data_ip = tv.get_hist(symbol='IP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ip is not None and not data_ip.empty:
        all_data['IP'] = data_ip['close']
        print("(302/503) Successfully fetched data for IP")
    else:
        print("(302/503) No data returned for IP. Skipping.")
        failed_tickers.append('IP')
except Exception as e:
    print(f"(302/503) Failed to fetch data for IP: {e}")
    failed_tickers.append('IP')

# Ticker 303: AVB
try:
    data_avb = tv.get_hist(symbol='AVB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_avb is not None and not data_avb.empty:
        all_data['AVB'] = data_avb['close']
        print("(303/503) Successfully fetched data for AVB")
    else:
        print("(303/503) No data returned for AVB. Skipping.")
        failed_tickers.append('AVB')
except Exception as e:
    print(f"(303/503) Failed to fetch data for AVB: {e}")
    failed_tickers.append('AVB')

# Ticker 304: KEYS
try:
    data_keys = tv.get_hist(symbol='KEYS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_keys is not None and not data_keys.empty:
        all_data['KEYS'] = data_keys['close']
        print("(304/503) Successfully fetched data for KEYS")
    else:
        print("(304/503) No data returned for KEYS. Skipping.")
        failed_tickers.append('KEYS')
except Exception as e:
    print(f"(304/503) Failed to fetch data for KEYS: {e}")
    failed_tickers.append('KEYS')

# Ticker 305: DTE
try:
    data_dte = tv.get_hist(symbol='DTE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dte is not None and not data_dte.empty:
        all_data['DTE'] = data_dte['close']
        print("(305/503) Successfully fetched data for DTE")
    else:
        print("(305/503) No data returned for DTE. Skipping.")
        failed_tickers.append('DTE')
except Exception as e:
    print(f"(305/503) Failed to fetch data for DTE: {e}")
    failed_tickers.append('DTE')

# Ticker 306: FITB
try:
    data_fitb = tv.get_hist(symbol='FITB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_fitb is not None and not data_fitb.empty:
        all_data['FITB'] = data_fitb['close']
        print("(306/503) Successfully fetched data for FITB")
    else:
        print("(306/503) No data returned for FITB. Skipping.")
        failed_tickers.append('FITB')
except Exception as e:
    print(f"(306/503) Failed to fetch data for FITB: {e}")
    failed_tickers.append('FITB')

# Ticker 307: HUM
try:
    data_hum = tv.get_hist(symbol='HUM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hum is not None and not data_hum.empty:
        all_data['HUM'] = data_hum['close']
        print("(307/503) Successfully fetched data for HUM")
    else:
        print("(307/503) No data returned for HUM. Skipping.")
        failed_tickers.append('HUM')
except Exception as e:
    print(f"(307/503) Failed to fetch data for HUM: {e}")
    failed_tickers.append('HUM')

# Ticker 308: ROL
try:
    data_rol = tv.get_hist(symbol='ROL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rol is not None and not data_rol.empty:
        all_data['ROL'] = data_rol['close']
        print("(308/503) Successfully fetched data for ROL")
    else:
        print("(308/503) No data returned for ROL. Skipping.")
        failed_tickers.append('ROL')
except Exception as e:
    print(f"(308/503) Failed to fetch data for ROL: {e}")
    failed_tickers.append('ROL')

# Ticker 309: K
try:
    data_k = tv.get_hist(symbol='K', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_k is not None and not data_k.empty:
        all_data['K'] = data_k['close']
        print("(309/503) Successfully fetched data for K")
    else:
        print("(309/503) No data returned for K. Skipping.")
        failed_tickers.append('K')
except Exception as e:
    print(f"(309/503) Failed to fetch data for K: {e}")
    failed_tickers.append('K')

# Ticker 310: AWK
try:
    data_awk = tv.get_hist(symbol='AWK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_awk is not None and not data_awk.empty:
        all_data['AWK'] = data_awk['close']
        print("(310/503) Successfully fetched data for AWK")
    else:
        print("(310/503) No data returned for AWK. Skipping.")
        failed_tickers.append('AWK')
except Exception as e:
    print(f"(310/503) Failed to fetch data for AWK: {e}")
    failed_tickers.append('AWK')

# Ticker 311: HPE
try:
    data_hpe = tv.get_hist(symbol='HPE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hpe is not None and not data_hpe.empty:
        all_data['HPE'] = data_hpe['close']
        print("(311/503) Successfully fetched data for HPE")
    else:
        print("(311/503) No data returned for HPE. Skipping.")
        failed_tickers.append('HPE')
except Exception as e:
    print(f"(311/503) Failed to fetch data for HPE: {e}")
    failed_tickers.append('HPE')

# Ticker 312: GIS
try:
    data_gis = tv.get_hist(symbol='GIS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gis is not None and not data_gis.empty:
        all_data['GIS'] = data_gis['close']
        print("(312/503) Successfully fetched data for GIS")
    else:
        print("(312/503) No data returned for GIS. Skipping.")
        failed_tickers.append('GIS')
except Exception as e:
    print(f"(312/503) Failed to fetch data for GIS: {e}")
    failed_tickers.append('GIS')

# Ticker 313: IT
try:
    data_it = tv.get_hist(symbol='IT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_it is not None and not data_it.empty:
        all_data['IT'] = data_it['close']
        print("(313/503) Successfully fetched data for IT")
    else:
        print("(313/503) No data returned for IT. Skipping.")
        failed_tickers.append('IT')
except Exception as e:
    print(f"(313/503) Failed to fetch data for IT: {e}")
    failed_tickers.append('IT')

# Ticker 314: AEE
try:
    data_aee = tv.get_hist(symbol='AEE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aee is not None and not data_aee.empty:
        all_data['AEE'] = data_aee['close']
        print("(314/503) Successfully fetched data for AEE")
    else:
        print("(314/503) No data returned for AEE. Skipping.")
        failed_tickers.append('AEE')
except Exception as e:
    print(f"(314/503) Failed to fetch data for AEE: {e}")
    failed_tickers.append('AEE')

# Ticker 315: PPL
try:
    data_ppl = tv.get_hist(symbol='PPL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ppl is not None and not data_ppl.empty:
        all_data['PPL'] = data_ppl['close']
        print("(315/503) Successfully fetched data for PPL")
    else:
        print("(315/503) No data returned for PPL. Skipping.")
        failed_tickers.append('PPL')
except Exception as e:
    print(f"(315/503) Failed to fetch data for PPL: {e}")
    failed_tickers.append('PPL')

# Ticker 316: SYF
try:
    data_syf = tv.get_hist(symbol='SYF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_syf is not None and not data_syf.empty:
        all_data['SYF'] = data_syf['close']
        print("(316/503) Successfully fetched data for SYF")
    else:
        print("(316/503) No data returned for SYF. Skipping.")
        failed_tickers.append('SYF')
except Exception as e:
    print(f"(316/503) Failed to fetch data for SYF: {e}")
    failed_tickers.append('SYF')

# Ticker 317: MTD
try:
    data_mtd = tv.get_hist(symbol='MTD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mtd is not None and not data_mtd.empty:
        all_data['MTD'] = data_mtd['close']
        print("(317/503) Successfully fetched data for MTD")
    else:
        print("(317/503) No data returned for MTD. Skipping.")
        failed_tickers.append('MTD')
except Exception as e:
    print(f"(317/503) Failed to fetch data for MTD: {e}")
    failed_tickers.append('MTD')

# Ticker 318: WRB
try:
    data_wrb = tv.get_hist(symbol='WRB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wrb is not None and not data_wrb.empty:
        all_data['WRB'] = data_wrb['close']
        print("(318/503) Successfully fetched data for WRB")
    else:
        print("(318/503) No data returned for WRB. Skipping.")
        failed_tickers.append('WRB')
except Exception as e:
    print(f"(318/503) Failed to fetch data for WRB: {e}")
    failed_tickers.append('WRB')

# Ticker 319: VRSN
try:
    data_vrsn = tv.get_hist(symbol='VRSN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_vrsn is not None and not data_vrsn.empty:
        all_data['VRSN'] = data_vrsn['close']
        print("(319/503) Successfully fetched data for VRSN")
    else:
        print("(319/503) No data returned for VRSN. Skipping.")
        failed_tickers.append('VRSN')
except Exception as e:
    print(f"(319/503) Failed to fetch data for VRSN: {e}")
    failed_tickers.append('VRSN')

# Ticker 320: ADM
try:
    data_adm = tv.get_hist(symbol='ADM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_adm is not None and not data_adm.empty:
        all_data['ADM'] = data_adm['close']
        print("(320/503) Successfully fetched data for ADM")
    else:
        print("(320/503) No data returned for ADM. Skipping.")
        failed_tickers.append('ADM')
except Exception as e:
    print(f"(320/503) Failed to fetch data for ADM: {e}")
    failed_tickers.append('ADM')

# Ticker 321: VLTO
try:
    data_vlto = tv.get_hist(symbol='VLTO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_vlto is not None and not data_vlto.empty:
        all_data['VLTO'] = data_vlto['close']
        print("(321/503) Successfully fetched data for VLTO")
    else:
        print("(321/503) No data returned for VLTO. Skipping.")
        failed_tickers.append('VLTO')
except Exception as e:
    print(f"(321/503) Failed to fetch data for VLTO: {e}")
    failed_tickers.append('VLTO')

# Ticker 322: TDY
try:
    data_tdy = tv.get_hist(symbol='TDY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tdy is not None and not data_tdy.empty:
        all_data['TDY'] = data_tdy['close']
        print("(322/503) Successfully fetched data for TDY")
    else:
        print("(322/503) No data returned for TDY. Skipping.")
        failed_tickers.append('TDY')
except Exception as e:
    print(f"(322/503) Failed to fetch data for TDY: {e}")
    failed_tickers.append('TDY')

# Ticker 323: LULU
try:
    data_lulu = tv.get_hist(symbol='LULU', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_lulu is not None and not data_lulu.empty:
        all_data['LULU'] = data_lulu['close']
        print("(323/503) Successfully fetched data for LULU")
    else:
        print("(323/503) No data returned for LULU. Skipping.")
        failed_tickers.append('LULU')
except Exception as e:
    print(f"(323/503) Failed to fetch data for LULU: {e}")
    failed_tickers.append('LULU')

# Ticker 324: EQR
try:
    data_eqr = tv.get_hist(symbol='EQR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_eqr is not None and not data_eqr.empty:
        all_data['EQR'] = data_eqr['close']
        print("(324/503) Successfully fetched data for EQR")
    else:
        print("(324/503) No data returned for EQR. Skipping.")
        failed_tickers.append('EQR')
except Exception as e:
    print(f"(324/503) Failed to fetch data for EQR: {e}")
    failed_tickers.append('EQR')

# Ticker 325: PPG
try:
    data_ppg = tv.get_hist(symbol='PPG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ppg is not None and not data_ppg.empty:
        all_data['PPG'] = data_ppg['close']
        print("(325/503) Successfully fetched data for PPG")
    else:
        print("(325/503) No data returned for PPG. Skipping.")
        failed_tickers.append('PPG')
except Exception as e:
    print(f"(325/503) Failed to fetch data for PPG: {e}")
    failed_tickers.append('PPG')

# --- EXPORT CHUNK 13 (TICKERS 301-325) ---
print("\n--- Merging and exporting data for companies 301-325 ---")
chunk_13_data = {}
tickers_301_325 = {
    'IRM': 'data_irm', 'IP': 'data_ip', 'AVB': 'data_avb', 'KEYS': 'data_keys', 'DTE': 'data_dte', 'FITB': 'data_fitb', 'HUM': 'data_hum', 'ROL': 'data_rol', 'K': 'data_k', 'AWK': 'data_awk', 'HPE': 'data_hpe', 'GIS': 'data_gis', 'IT': 'data_it', 'AEE': 'data_aee', 'PPL': 'data_ppl', 'SYF': 'data_syf', 'MTD': 'data_mtd', 'WRB': 'data_wrb', 'VRSN': 'data_vrsn', 'ADM': 'data_adm', 'VLTO': 'data_vlto', 'TDY': 'data_tdy', 'LULU': 'data_lulu', 'EQR': 'data_eqr', 'PPG': 'data_ppg'
}
for ticker, data_var_name in tickers_301_325.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_13_data[ticker] = close_series
if chunk_13_data:
    price_df_13 = pd.DataFrame(chunk_13_data)
    price_df_13.sort_index(inplace=True)
    price_df_13.ffill(inplace=True)
    price_df_13.to_csv('sp500_prices_301-325.csv')
    print("--- Successfully exported sp500_prices_301-325.csv ---\n")
else:
    print("--- No data collected for chunk 13, skipping export. ---\n")

# Ticker 326: DOV
try:
    data_dov = tv.get_hist(symbol='DOV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dov is not None and not data_dov.empty:
        all_data['DOV'] = data_dov['close']
        print("(326/503) Successfully fetched data for DOV")
    else:
        print("(326/503) No data returned for DOV. Skipping.")
        failed_tickers.append('DOV')
except Exception as e:
    print(f"(326/503) Failed to fetch data for DOV: {e}")
    failed_tickers.append('DOV')

# Ticker 327: CBOE
try:
    data_cboe = tv.get_hist(symbol='CBOE', exchange='CBOE', interval=INTERVAL, n_bars=N_BARS)
    if data_cboe is not None and not data_cboe.empty:
        all_data['CBOE'] = data_cboe['close']
        print("(327/503) Successfully fetched data for CBOE")
    else:
        print("(327/503) No data returned for CBOE. Skipping.")
        failed_tickers.append('CBOE')
except Exception as e:
    print(f"(327/503) Failed to fetch data for CBOE: {e}")
    failed_tickers.append('CBOE')

# Ticker 328: WRK
try:
    data_wrk = tv.get_hist(symbol='WRK', exchange='ASX', interval=INTERVAL, n_bars=N_BARS)
    if data_wrk is not None and not data_wrk.empty:
        all_data['WRK'] = data_wrk['close']
        print("(328/503) Successfully fetched data for WRK")
    else:
        print("(328/503) No data returned for WRK. Skipping.")
        failed_tickers.append('WRK')
except Exception as e:
    print(f"(328/503) Failed to fetch data for WRK: {e}")
    failed_tickers.append('WRK')

# Ticker 329: NTRS
try:
    data_ntrs = tv.get_hist(symbol='NTRS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ntrs is not None and not data_ntrs.empty:
        all_data['NTRS'] = data_ntrs['close']
        print("(329/503) Successfully fetched data for NTRS")
    else:
        print("(329/503) No data returned for NTRS. Skipping.")
        failed_tickers.append('NTRS')
except Exception as e:
    print(f"(329/503) Failed to fetch data for NTRS: {e}")
    failed_tickers.append('NTRS')

# Ticker 330: CNP
try:
    data_cnp = tv.get_hist(symbol='CNP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cnp is not None and not data_cnp.empty:
        all_data['CNP'] = data_cnp['close']
        print("(330/503) Successfully fetched data for CNP")
    else:
        print("(330/503) No data returned for CNP. Skipping.")
        failed_tickers.append('CNP')
except Exception as e:
    print(f"(330/503) Failed to fetch data for CNP: {e}")
    failed_tickers.append('CNP')

# Ticker 331: ATO
try:
    data_ato = tv.get_hist(symbol='ATO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ato is not None and not data_ato.empty:
        all_data['ATO'] = data_ato['close']
        print("(331/503) Successfully fetched data for ATO")
    else:
        print("(331/503) No data returned for ATO. Skipping.")
        failed_tickers.append('ATO')
except Exception as e:
    print(f"(331/503) Failed to fetch data for ATO: {e}")
    failed_tickers.append('ATO')

# Ticker 332: HBAN
try:
    data_hban = tv.get_hist(symbol='HBAN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_hban is not None and not data_hban.empty:
        all_data['HBAN'] = data_hban['close']
        print("(332/503) Successfully fetched data for HBAN")
    else:
        print("(332/503) No data returned for HBAN. Skipping.")
        failed_tickers.append('HBAN')
except Exception as e:
    print(f"(332/503) Failed to fetch data for HBAN: {e}")
    failed_tickers.append('HBAN')

# Ticker 333: SBAC
try:
    data_sbac = tv.get_hist(symbol='SBAC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_sbac is not None and not data_sbac.empty:
        all_data['SBAC'] = data_sbac['close']
        print("(333/503) Successfully fetched data for SBAC")
    else:
        print("(333/503) No data returned for SBAC. Skipping.")
        failed_tickers.append('SBAC')
except Exception as e:
    print(f"(333/503) Failed to fetch data for SBAC: {e}")
    failed_tickers.append('SBAC')

# Ticker 334: JBL
try:
    data_jbl = tv.get_hist(symbol='JBL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_jbl is not None and not data_jbl.empty:
        all_data['JBL'] = data_jbl['close']
        print("(334/503) Successfully fetched data for JBL")
    else:
        print("(334/503) No data returned for JBL. Skipping.")
        failed_tickers.append('JBL')
except Exception as e:
    print(f"(334/503) Failed to fetch data for JBL: {e}")
    failed_tickers.append('JBL')

# Ticker 335: WDC
try:
    data_wdc = tv.get_hist(symbol='WDC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wdc is not None and not data_wdc.empty:
        all_data['WDC'] = data_wdc['close']
        print("(335/503) Successfully fetched data for WDC")
    else:
        print("(335/503) No data returned for WDC. Skipping.")
        failed_tickers.append('WDC')
except Exception as e:
    print(f"(335/503) Failed to fetch data for WDC: {e}")
    failed_tickers.append('WDC')

# Ticker 336: ON
try:
    data_on = tv.get_hist(symbol='ON', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_on is not None and not data_on.empty:
        all_data['ON'] = data_on['close']
        print("(336/503) Successfully fetched data for ON")
    else:
        print("(336/503) No data returned for ON. Skipping.")
        failed_tickers.append('ON')
except Exception as e:
    print(f"(336/503) Failed to fetch data for ON: {e}")
    failed_tickers.append('ON')

# Ticker 337: PTC
try:
    data_ptc = tv.get_hist(symbol='PTC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ptc is not None and not data_ptc.empty:
        all_data['PTC'] = data_ptc['close']
        print("(337/503) Successfully fetched data for PTC")
    else:
        print("(337/503) No data returned for PTC. Skipping.")
        failed_tickers.append('PTC')
except Exception as e:
    print(f"(337/503) Failed to fetch data for PTC: {e}")
    failed_tickers.append('PTC')

# Ticker 338: ES
try:
    data_es = tv.get_hist(symbol='ES', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_es is not None and not data_es.empty:
        all_data['ES'] = data_es['close']
        print("(338/503) Successfully fetched data for ES")
    else:
        print("(338/503) No data returned for ES. Skipping.")
        failed_tickers.append('ES')
except Exception as e:
    print(f"(338/503) Failed to fetch data for ES: {e}")
    failed_tickers.append('ES')

# Ticker 339: HPQ
try:
    data_hpq = tv.get_hist(symbol='HPQ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hpq is not None and not data_hpq.empty:
        all_data['HPQ'] = data_hpq['close']
        print("(339/503) Successfully fetched data for HPQ")
    else:
        print("(339/503) No data returned for HPQ. Skipping.")
        failed_tickers.append('HPQ')
except Exception as e:
    print(f"(339/503) Failed to fetch data for HPQ: {e}")
    failed_tickers.append('HPQ')

# Ticker 340: FE
try:
    data_fe = tv.get_hist(symbol='FE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fe is not None and not data_fe.empty:
        all_data['FE'] = data_fe['close']
        print("(340/503) Successfully fetched data for FE")
    else:
        print("(340/503) No data returned for FE. Skipping.")
        failed_tickers.append('FE')
except Exception as e:
    print(f"(340/503) Failed to fetch data for FE: {e}")
    failed_tickers.append('FE')

# Ticker 341: CINF
try:
    data_cinf = tv.get_hist(symbol='CINF', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cinf is not None and not data_cinf.empty:
        all_data['CINF'] = data_cinf['close']
        print("(341/503) Successfully fetched data for CINF")
    else:
        print("(341/503) No data returned for CINF. Skipping.")
        failed_tickers.append('CINF')
except Exception as e:
    print(f"(341/503) Failed to fetch data for CINF: {e}")
    failed_tickers.append('CINF')

# Ticker 342: CHD
try:
    data_chd = tv.get_hist(symbol='CHD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_chd is not None and not data_chd.empty:
        all_data['CHD'] = data_chd['close']
        print("(342/503) Successfully fetched data for CHD")
    else:
        print("(342/503) No data returned for CHD. Skipping.")
        failed_tickers.append('CHD')
except Exception as e:
    print(f"(342/503) Failed to fetch data for CHD: {e}")
    failed_tickers.append('CHD')

# Ticker 343: CDW
try:
    data_cdw = tv.get_hist(symbol='CDW', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cdw is not None and not data_cdw.empty:
        all_data['CDW'] = data_cdw['close']
        print("(343/503) Successfully fetched data for CDW")
    else:
        print("(343/503) No data returned for CDW. Skipping.")
        failed_tickers.append('CDW')
except Exception as e:
    print(f"(343/503) Failed to fetch data for CDW: {e}")
    failed_tickers.append('CDW')

# Ticker 344: TYL
try:
    data_tyl = tv.get_hist(symbol='TYL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tyl is not None and not data_tyl.empty:
        all_data['TYL'] = data_tyl['close']
        print("(344/503) Successfully fetched data for TYL")
    else:
        print("(344/503) No data returned for TYL. Skipping.")
        failed_tickers.append('TYL')
except Exception as e:
    print(f"(344/503) Failed to fetch data for TYL: {e}")
    failed_tickers.append('TYL')

# Ticker 345: EXPD
try:
    data_expd = tv.get_hist(symbol='EXPD', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_expd is not None and not data_expd.empty:
        all_data['EXPD'] = data_expd['close']
        print("(345/503) Successfully fetched data for EXPD")
    else:
        print("(345/503) No data returned for EXPD. Skipping.")
        failed_tickers.append('EXPD')
except Exception as e:
    print(f"(345/503) Failed to fetch data for EXPD: {e}")
    failed_tickers.append('EXPD')

# Ticker 346: DLTR
try:
    data_dltr = tv.get_hist(symbol='DLTR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_dltr is not None and not data_dltr.empty:
        all_data['DLTR'] = data_dltr['close']
        print("(346/503) Successfully fetched data for DLTR")
    else:
        print("(346/503) No data returned for DLTR. Skipping.")
        failed_tickers.append('DLTR')
except Exception as e:
    print(f"(346/503) Failed to fetch data for DLTR: {e}")
    failed_tickers.append('DLTR')

# Ticker 347: DRI
try:
    data_dri = tv.get_hist(symbol='DRI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dri is not None and not data_dri.empty:
        all_data['DRI'] = data_dri['close']
        print("(347/503) Successfully fetched data for DRI")
    else:
        print("(347/503) No data returned for DRI. Skipping.")
        failed_tickers.append('DRI')
except Exception as e:
    print(f"(347/503) Failed to fetch data for DRI: {e}")
    failed_tickers.append('DRI')

# Ticker 348: RF
try:
    data_rf = tv.get_hist(symbol='RF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rf is not None and not data_rf.empty:
        all_data['RF'] = data_rf['close']
        print("(348/503) Successfully fetched data for RF")
    else:
        print("(348/503) No data returned for RF. Skipping.")
        failed_tickers.append('RF')
except Exception as e:
    print(f"(348/503) Failed to fetch data for RF: {e}")
    failed_tickers.append('RF')

# Ticker 349: GDDY
try:
    data_gddy = tv.get_hist(symbol='GDDY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gddy is not None and not data_gddy.empty:
        all_data['GDDY'] = data_gddy['close']
        print("(349/503) Successfully fetched data for GDDY")
    else:
        print("(349/503) No data returned for GDDY. Skipping.")
        failed_tickers.append('GDDY')
except Exception as e:
    print(f"(349/503) Failed to fetch data for GDDY: {e}")
    failed_tickers.append('GDDY')

# Ticker 350: DG
try:
    data_dg = tv.get_hist(symbol='DG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dg is not None and not data_dg.empty:
        all_data['DG'] = data_dg['close']
        print("(350/503) Successfully fetched data for DG")
    else:
        print("(350/503) No data returned for DG. Skipping.")
        failed_tickers.append('DG')
except Exception as e:
    print(f"(350/503) Failed to fetch data for DG: {e}")
    failed_tickers.append('DG')

# --- EXPORT CHUNK 14 (TICKERS 326-350) ---
print("\n--- Merging and exporting data for companies 326-350 ---")
chunk_14_data = {}
tickers_326_350 = {
    'DOV': 'data_dov', 'CBOE': 'data_cboe', 'WRK': 'data_wrk', 'NTRS': 'data_ntrs', 'CNP': 'data_cnp', 'ATO': 'data_ato', 'HBAN': 'data_hban', 'SBAC': 'data_sbac', 'JBL': 'data_jbl', 'WDC': 'data_wdc', 'ON': 'data_on', 'PTC': 'data_ptc', 'ES': 'data_es', 'HPQ': 'data_hpq', 'FE': 'data_fe', 'CINF': 'data_cinf', 'CHD': 'data_chd', 'CDW': 'data_cdw', 'TYL': 'data_tyl', 'EXPD': 'data_expd', 'DLTR': 'data_dltr', 'DRI': 'data_dri', 'RF': 'data_rf', 'GDDY': 'data_gddy', 'DG': 'data_dg'
}
for ticker, data_var_name in tickers_326_350.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_14_data[ticker] = close_series
if chunk_14_data:
    price_df_14 = pd.DataFrame(chunk_14_data)
    price_df_14.sort_index(inplace=True)
    price_df_14.ffill(inplace=True)
    price_df_14.to_csv('sp500_prices_326-350.csv')
    print("--- Successfully exported sp500_prices_326-350.csv ---\n")
else:
    print("--- No data collected for chunk 14, skipping export. ---\n")

# Ticker 351: EXPE
try:
    data_expe = tv.get_hist(symbol='EXPE', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_expe is not None and not data_expe.empty:
        all_data['EXPE'] = data_expe['close']
        print("(351/503) Successfully fetched data for EXPE")
    else:
        print("(351/503) No data returned for EXPE. Skipping.")
        failed_tickers.append('EXPE')
except Exception as e:
    print(f"(351/503) Failed to fetch data for EXPE: {e}")
    failed_tickers.append('EXPE')

# Ticker 352: CPAY
try:
    data_cpay = tv.get_hist(symbol='CPAY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cpay is not None and not data_cpay.empty:
        all_data['CPAY'] = data_cpay['close']
        print("(352/503) Successfully fetched data for CPAY")
    else:
        print("(352/503) No data returned for CPAY. Skipping.")
        failed_tickers.append('CPAY')
except Exception as e:
    print(f"(352/503) Failed to fetch data for CPAY: {e}")
    failed_tickers.append('CPAY')

# Ticker 353: TROW
try:
    data_trow = tv.get_hist(symbol='TROW', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_trow is not None and not data_trow.empty:
        all_data['TROW'] = data_trow['close']
        print("(353/503) Successfully fetched data for TROW")
    else:
        print("(353/503) No data returned for TROW. Skipping.")
        failed_tickers.append('TROW')
except Exception as e:
    print(f"(353/503) Failed to fetch data for TROW: {e}")
    failed_tickers.append('TROW')

# Ticker 354: ULTA
try:
    data_ulta = tv.get_hist(symbol='ULTA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ulta is not None and not data_ulta.empty:
        all_data['ULTA'] = data_ulta['close']
        print("(354/503) Successfully fetched data for ULTA")
    else:
        print("(354/503) No data returned for ULTA. Skipping.")
        failed_tickers.append('ULTA')
except Exception as e:
    print(f"(354/503) Failed to fetch data for ULTA: {e}")
    failed_tickers.append('ULTA')

# Ticker 355: PHM
try:
    data_phm = tv.get_hist(symbol='PHM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_phm is not None and not data_phm.empty:
        all_data['PHM'] = data_phm['close']
        print("(355/503) Successfully fetched data for PHM")
    else:
        print("(355/503) No data returned for PHM. Skipping.")
        failed_tickers.append('PHM')
except Exception as e:
    print(f"(355/503) Failed to fetch data for PHM: {e}")
    failed_tickers.append('PHM')

# Ticker 356: HUBB
try:
    data_hubb = tv.get_hist(symbol='HUBB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hubb is not None and not data_hubb.empty:
        all_data['HUBB'] = data_hubb['close']
        print("(356/503) Successfully fetched data for HUBB")
    else:
        print("(356/503) No data returned for HUBB. Skipping.")
        failed_tickers.append('HUBB')
except Exception as e:
    print(f"(356/503) Failed to fetch data for HUBB: {e}")
    failed_tickers.append('HUBB')

# Ticker 357: WSM
try:
    data_wsm = tv.get_hist(symbol='WSM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wsm is not None and not data_wsm.empty:
        all_data['WSM'] = data_wsm['close']
        print("(357/503) Successfully fetched data for WSM")
    else:
        print("(357/503) No data returned for WSM. Skipping.")
        failed_tickers.append('WSM')
except Exception as e:
    print(f"(357/503) Failed to fetch data for WSM: {e}")
    failed_tickers.append('WSM')

# Ticker 358: LII
try:
    data_lii = tv.get_hist(symbol='LII', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lii is not None and not data_lii.empty:
        all_data['LII'] = data_lii['close']
        print("(358/503) Successfully fetched data for LII")
    else:
        print("(358/503) No data returned for LII. Skipping.")
        failed_tickers.append('LII')
except Exception as e:
    print(f"(358/503) Failed to fetch data for LII: {e}")
    failed_tickers.append('LII')

# Ticker 359: STE
try:
    data_ste = tv.get_hist(symbol='STE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ste is not None and not data_ste.empty:
        all_data['STE'] = data_ste['close']
        print("(359/503) Successfully fetched data for STE")
    else:
        print("(359/503) No data returned for STE. Skipping.")
        failed_tickers.append('STE')
except Exception as e:
    print(f"(359/503) Failed to fetch data for STE: {e}")
    failed_tickers.append('STE')

# Ticker 360: TPR
try:
    data_tpr = tv.get_hist(symbol='TPR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tpr is not None and not data_tpr.empty:
        all_data['TPR'] = data_tpr['close']
        print("(360/503) Successfully fetched data for TPR")
    else:
        print("(360/503) No data returned for TPR. Skipping.")
        failed_tickers.append('TPR')
except Exception as e:
    print(f"(360/503) Failed to fetch data for TPR: {e}")
    failed_tickers.append('TPR')

# Ticker 361: TPL
try:
    data_tpl = tv.get_hist(symbol='TPL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tpl is not None and not data_tpl.empty:
        all_data['TPL'] = data_tpl['close']
        print("(361/503) Successfully fetched data for TPL")
    else:
        print("(361/503) No data returned for TPL. Skipping.")
        failed_tickers.append('TPL')
except Exception as e:
    print(f"(361/503) Failed to fetch data for TPL: {e}")
    failed_tickers.append('TPL')

# Ticker 362: AMCR
try:
    data_amcr = tv.get_hist(symbol='AMCR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_amcr is not None and not data_amcr.empty:
        all_data['AMCR'] = data_amcr['close']
        print("(362/503) Successfully fetched data for AMCR")
    else:
        print("(362/503) No data returned for AMCR. Skipping.")
        failed_tickers.append('AMCR')
except Exception as e:
    print(f"(362/503) Failed to fetch data for AMCR: {e}")
    failed_tickers.append('AMCR')

# Ticker 363: LH
try:
    data_lh = tv.get_hist(symbol='LH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lh is not None and not data_lh.empty:
        all_data['LH'] = data_lh['close']
        print("(363/503) Successfully fetched data for LH")
    else:
        print("(363/503) No data returned for LH. Skipping.")
        failed_tickers.append('LH')
except Exception as e:
    print(f"(363/503) Failed to fetch data for LH: {e}")
    failed_tickers.append('LH')

# Ticker 364: DVN
try:
    data_dvn = tv.get_hist(symbol='DVN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dvn is not None and not data_dvn.empty:
        all_data['DVN'] = data_dvn['close']
        print("(364/503) Successfully fetched data for DVN")
    else:
        print("(364/503) No data returned for DVN. Skipping.")
        failed_tickers.append('DVN')
except Exception as e:
    print(f"(364/503) Failed to fetch data for DVN: {e}")
    failed_tickers.append('DVN')

# Ticker 365: NVR
try:
    data_nvr = tv.get_hist(symbol='NVR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nvr is not None and not data_nvr.empty:
        all_data['NVR'] = data_nvr['close']
        print("(365/503) Successfully fetched data for NVR")
    else:
        print("(365/503) No data returned for NVR. Skipping.")
        failed_tickers.append('NVR')
except Exception as e:
    print(f"(365/503) Failed to fetch data for NVR: {e}")
    failed_tickers.append('NVR')

# Ticker 366: CMS
try:
    data_cms = tv.get_hist(symbol='CMS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cms is not None and not data_cms.empty:
        all_data['CMS'] = data_cms['close']
        print("(366/503) Successfully fetched data for CMS")
    else:
        print("(366/503) No data returned for CMS. Skipping.")
        failed_tickers.append('CMS')
except Exception as e:
    print(f"(366/503) Failed to fetch data for CMS: {e}")
    failed_tickers.append('CMS')

# Ticker 367: CFG
try:
    data_cfg = tv.get_hist(symbol='CFG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cfg is not None and not data_cfg.empty:
        all_data['CFG'] = data_cfg['close']
        print("(367/503) Successfully fetched data for CFG")
    else:
        print("(367/503) No data returned for CFG. Skipping.")
        failed_tickers.append('CFG')
except Exception as e:
    print(f"(367/503) Failed to fetch data for CFG: {e}")
    failed_tickers.append('CFG')

# Ticker 368: NTAP
try:
    data_ntap = tv.get_hist(symbol='NTAP', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ntap is not None and not data_ntap.empty:
        all_data['NTAP'] = data_ntap['close']
        print("(368/503) Successfully fetched data for NTAP")
    else:
        print("(368/503) No data returned for NTAP. Skipping.")
        failed_tickers.append('NTAP')
except Exception as e:
    print(f"(368/503) Failed to fetch data for NTAP: {e}")
    failed_tickers.append('NTAP')

# Ticker 369: LDOS
try:
    data_ldos = tv.get_hist(symbol='LDOS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ldos is not None and not data_ldos.empty:
        all_data['LDOS'] = data_ldos['close']
        print("(369/503) Successfully fetched data for LDOS")
    else:
        print("(369/503) No data returned for LDOS. Skipping.")
        failed_tickers.append('LDOS')
except Exception as e:
    print(f"(369/503) Failed to fetch data for LDOS: {e}")
    failed_tickers.append('LDOS')

# Ticker 370: PODD
try:
    data_podd = tv.get_hist(symbol='PODD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_podd is not None and not data_podd.empty:
        all_data['PODD'] = data_podd['close']
        print("(370/503) Successfully fetched data for PODD")
    else:
        print("(370/503) No data returned for PODD. Skipping.")
        failed_tickers.append('PODD')
except Exception as e:
    print(f"(370/503) Failed to fetch data for PODD: {e}")
    failed_tickers.append('PODD')

# Ticker 371: KEY
try:
    data_key = tv.get_hist(symbol='KEY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_key is not None and not data_key.empty:
        all_data['KEY'] = data_key['close']
        print("(371/503) Successfully fetched data for KEY")
    else:
        print("(371/503) No data returned for KEY. Skipping.")
        failed_tickers.append('KEY')
except Exception as e:
    print(f"(371/503) Failed to fetch data for KEY: {e}")
    failed_tickers.append('KEY')

# Ticker 372: GPN
try:
    data_gpn = tv.get_hist(symbol='GPN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gpn is not None and not data_gpn.empty:
        all_data['GPN'] = data_gpn['close']
        print("(372/503) Successfully fetched data for GPN")
    else:
        print("(372/503) No data returned for GPN. Skipping.")
        failed_tickers.append('GPN')
except Exception as e:
    print(f"(372/503) Failed to fetch data for GPN: {e}")
    failed_tickers.append('GPN')

# Ticker 373: EIX
try:
    data_eix = tv.get_hist(symbol='EIX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_eix is not None and not data_eix.empty:
        all_data['EIX'] = data_eix['close']
        print("(373/503) Successfully fetched data for EIX")
    else:
        print("(373/503) No data returned for EIX. Skipping.")
        failed_tickers.append('EIX')
except Exception as e:
    print(f"(373/503) Failed to fetch data for EIX: {e}")
    failed_tickers.append('EIX')

# Ticker 374: TRMB
try:
    data_trmb = tv.get_hist(symbol='TRMB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_trmb is not None and not data_trmb.empty:
        all_data['TRMB'] = data_trmb['close']
        print("(374/503) Successfully fetched data for TRMB")
    else:
        print("(374/503) No data returned for TRMB. Skipping.")
        failed_tickers.append('TRMB')
except Exception as e:
    print(f"(374/503) Failed to fetch data for TRMB: {e}")
    failed_tickers.append('TRMB')

# Ticker 375: LYB
try:
    data_lyb = tv.get_hist(symbol='LYB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lyb is not None and not data_lyb.empty:
        all_data['LYB'] = data_lyb['close']
        print("(375/503) Successfully fetched data for LYB")
    else:
        print("(375/503) No data returned for LYB. Skipping.")
        failed_tickers.append('LYB')
except Exception as e:
    print(f"(375/503) Failed to fetch data for LYB: {e}")
    failed_tickers.append('LYB')


# --- EXPORT CHUNK 15 (TICKERS 351-375) ---
print("\n--- Merging and exporting data for companies 351-375 ---")
chunk_15_data = {}
tickers_351_375 = {
    'EXPE': 'data_expe', 'CPAY': 'data_cpay', 'TROW': 'data_trow', 'ULTA': 'data_ulta', 'PHM': 'data_phm', 'HUBB': 'data_hubb', 'WSM': 'data_wsm', 'LII': 'data_lii', 'STE': 'data_ste', 'TPR': 'data_tpr', 'TPL': 'data_tpl', 'AMCR': 'data_amcr', 'LH': 'data_lh', 'DVN': 'data_dvn', 'NVR': 'data_nvr', 'CMS': 'data_cms', 'CFG': 'data_cfg', 'NTAP': 'data_ntap', 'LDOS': 'data_ldos', 'PODD': 'data_podd', 'KEY': 'data_key', 'GPN': 'data_gpn', 'EIX': 'data_eix', 'TRMB': 'data_trmb', 'LYB': 'data_lyb'
}
for ticker, data_var_name in tickers_351_375.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_15_data[ticker] = close_series
if chunk_15_data:
    price_df_15 = pd.DataFrame(chunk_15_data)
    price_df_15.sort_index(inplace=True)
    price_df_15.ffill(inplace=True)
    price_df_15.to_csv('sp500_prices_351-375.csv')
    print("--- Successfully exported sp500_prices_351-375.csv ---\n")
else:
    print("--- No data collected for chunk 15, skipping export. ---\n")

# Ticker 376: NI
try:
    data_ni = tv.get_hist(symbol='NI', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ni is not None and not data_ni.empty:
        all_data['NI'] = data_ni['close']
        print("(376/503) Successfully fetched data for NI")
    else:
        print("(376/503) No data returned for NI. Skipping.")
        failed_tickers.append('NI')
except Exception as e:
    print(f"(376/503) Failed to fetch data for NI: {e}")
    failed_tickers.append('NI')

# Ticker 377: MKC
try:
    data_mkc = tv.get_hist(symbol='MKC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mkc is not None and not data_mkc.empty:
        all_data['MKC'] = data_mkc['close']
        print("(377/503) Successfully fetched data for MKC")
    else:
        print("(377/503) No data returned for MKC. Skipping.")
        failed_tickers.append('MKC')
except Exception as e:
    print(f"(377/503) Failed to fetch data for MKC: {e}")
    failed_tickers.append('MKC')

# Ticker 378: FSLR
try:
    data_fslr = tv.get_hist(symbol='FSLR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_fslr is not None and not data_fslr.empty:
        all_data['FSLR'] = data_fslr['close']
        print("(378/503) Successfully fetched data for FSLR")
    else:
        print("(378/503) No data returned for FSLR. Skipping.")
        failed_tickers.append('FSLR')
except Exception as e:
    print(f"(378/503) Failed to fetch data for FSLR: {e}")
    failed_tickers.append('FSLR')

# Ticker 379: INVH
try:
    data_invh = tv.get_hist(symbol='INVH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_invh is not None and not data_invh.empty:
        all_data['INVH'] = data_invh['close']
        print("(379/503) Successfully fetched data for INVH")
    else:
        print("(379/503) No data returned for INVH. Skipping.")
        failed_tickers.append('INVH')
except Exception as e:
    print(f"(379/503) Failed to fetch data for INVH: {e}")
    failed_tickers.append('INVH')

# Ticker 380: HAL
try:
    data_hal = tv.get_hist(symbol='HAL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hal is not None and not data_hal.empty:
        all_data['HAL'] = data_hal['close']
        print("(380/503) Successfully fetched data for HAL")
    else:
        print("(380/503) No data returned for HAL. Skipping.")
        failed_tickers.append('HAL')
except Exception as e:
    print(f"(380/503) Failed to fetch data for HAL: {e}")
    failed_tickers.append('HAL')

# Ticker 381: TSN
try:
    data_tsn = tv.get_hist(symbol='TSN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tsn is not None and not data_tsn.empty:
        all_data['TSN'] = data_tsn['close']
        print("(381/503) Successfully fetched data for TSN")
    else:
        print("(381/503) No data returned for TSN. Skipping.")
        failed_tickers.append('TSN')
except Exception as e:
    print(f"(381/503) Failed to fetch data for TSN: {e}")
    failed_tickers.append('TSN')

# Ticker 382: L
try:
    data_l = tv.get_hist(symbol='L', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_l is not None and not data_l.empty:
        all_data['L'] = data_l['close']
        print("(382/503) Successfully fetched data for L")
    else:
        print("(382/503) No data returned for L. Skipping.")
        failed_tickers.append('L')
except Exception as e:
    print(f"(382/503) Failed to fetch data for L: {e}")
    failed_tickers.append('L')

# Ticker 383: IFF
try:
    data_iff = tv.get_hist(symbol='IFF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_iff is not None and not data_iff.empty:
        all_data['IFF'] = data_iff['close']
        print("(383/503) Successfully fetched data for IFF")
    else:
        print("(383/503) No data returned for IFF. Skipping.")
        failed_tickers.append('IFF')
except Exception as e:
    print(f"(383/503) Failed to fetch data for IFF: {e}")
    failed_tickers.append('IFF')

# Ticker 384: ZBH
try:
    data_zbh = tv.get_hist(symbol='ZBH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_zbh is not None and not data_zbh.empty:
        all_data['ZBH'] = data_zbh['close']
        print("(384/503) Successfully fetched data for ZBH")
    else:
        print("(384/503) No data returned for ZBH. Skipping.")
        failed_tickers.append('ZBH')
except Exception as e:
    print(f"(384/503) Failed to fetch data for ZBH: {e}")
    failed_tickers.append('ZBH')

# Ticker 385: DGX
try:
    data_dgx = tv.get_hist(symbol='DGX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dgx is not None and not data_dgx.empty:
        all_data['DGX'] = data_dgx['close']
        print("(385/503) Successfully fetched data for DGX")
    else:
        print("(385/503) No data returned for DGX. Skipping.")
        failed_tickers.append('DGX')
except Exception as e:
    print(f"(385/503) Failed to fetch data for DGX: {e}")
    failed_tickers.append('DGX')

# Ticker 386: STLD
try:
    data_stld = tv.get_hist(symbol='STLD', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_stld is not None and not data_stld.empty:
        all_data['STLD'] = data_stld['close']
        print("(386/503) Successfully fetched data for STLD")
    else:
        print("(386/503) No data returned for STLD. Skipping.")
        failed_tickers.append('STLD')
except Exception as e:
    print(f"(386/503) Failed to fetch data for STLD: {e}")
    failed_tickers.append('STLD')

# Ticker 387: BIIB
try:
    data_biib = tv.get_hist(symbol='BIIB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_biib is not None and not data_biib.empty:
        all_data['BIIB'] = data_biib['close']
        print("(387/503) Successfully fetched data for BIIB")
    else:
        print("(387/503) No data returned for BIIB. Skipping.")
        failed_tickers.append('BIIB')
except Exception as e:
    print(f"(387/503) Failed to fetch data for BIIB: {e}")
    failed_tickers.append('BIIB')

# Ticker 388: GEN
try:
    data_gen = tv.get_hist(symbol='GEN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_gen is not None and not data_gen.empty:
        all_data['GEN'] = data_gen['close']
        print("(388/503) Successfully fetched data for GEN")
    else:
        print("(388/503) No data returned for GEN. Skipping.")
        failed_tickers.append('GEN')
except Exception as e:
    print(f"(388/503) Failed to fetch data for GEN: {e}")
    failed_tickers.append('GEN')

# Ticker 389: WY
try:
    data_wy = tv.get_hist(symbol='WY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wy is not None and not data_wy.empty:
        all_data['WY'] = data_wy['close']
        print("(389/503) Successfully fetched data for WY")
    else:
        print("(389/503) No data returned for WY. Skipping.")
        failed_tickers.append('WY')
except Exception as e:
    print(f"(389/503) Failed to fetch data for WY: {e}")
    failed_tickers.append('WY')

# Ticker 390: ERIE
try:
    data_erie = tv.get_hist(symbol='ERIE', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_erie is not None and not data_erie.empty:
        all_data['ERIE'] = data_erie['close']
        print("(390/503) Successfully fetched data for ERIE")
    else:
        print("(390/503) No data returned for ERIE. Skipping.")
        failed_tickers.append('ERIE')
except Exception as e:
    print(f"(390/503) Failed to fetch data for ERIE: {e}")
    failed_tickers.append('ERIE')

# Ticker 391: ESS
try:
    data_ess = tv.get_hist(symbol='ESS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ess is not None and not data_ess.empty:
        all_data['ESS'] = data_ess['close']
        print("(391/503) Successfully fetched data for ESS")
    else:
        print("(391/503) No data returned for ESS. Skipping.")
        failed_tickers.append('ESS')
except Exception as e:
    print(f"(391/503) Failed to fetch data for ESS: {e}")
    failed_tickers.append('ESS')

# Ticker 392: GPC
try:
    data_gpc = tv.get_hist(symbol='GPC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gpc is not None and not data_gpc.empty:
        all_data['GPC'] = data_gpc['close']
        print("(392/503) Successfully fetched data for GPC")
    else:
        print("(392/503) No data returned for GPC. Skipping.")
        failed_tickers.append('GPC')
except Exception as e:
    print(f"(392/503) Failed to fetch data for GPC: {e}")
    failed_tickers.append('GPC')

# Ticker 393: CTRA
try:
    data_ctra = tv.get_hist(symbol='CTRA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ctra is not None and not data_ctra.empty:
        all_data['CTRA'] = data_ctra['close']
        print("(393/503) Successfully fetched data for CTRA")
    else:
        print("(393/503) No data returned for CTRA. Skipping.")
        failed_tickers.append('CTRA')
except Exception as e:
    print(f"(393/503) Failed to fetch data for CTRA: {e}")
    failed_tickers.append('CTRA')

# Ticker 394: WST
try:
    data_wst = tv.get_hist(symbol='WST', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wst is not None and not data_wst.empty:
        all_data['WST'] = data_wst['close']
        print("(394/503) Successfully fetched data for WST")
    else:
        print("(394/503) No data returned for WST. Skipping.")
        failed_tickers.append('WST')
except Exception as e:
    print(f"(394/503) Failed to fetch data for WST: {e}")
    failed_tickers.append('WST')

# Ticker 395: PKG
try:
    data_pkg = tv.get_hist(symbol='PKG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pkg is not None and not data_pkg.empty:
        all_data['PKG'] = data_pkg['close']
        print("(395/503) Successfully fetched data for PKG")
    else:
        print("(395/503) No data returned for PKG. Skipping.")
        failed_tickers.append('PKG')
except Exception as e:
    print(f"(395/503) Failed to fetch data for PKG: {e}")
    failed_tickers.append('PKG')

# Ticker 396: PFG
try:
    data_pfg = tv.get_hist(symbol='PFG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pfg is not None and not data_pfg.empty:
        all_data['PFG'] = data_pfg['close']
        print("(396/503) Successfully fetched data for PFG")
    else:
        print("(396/503) No data returned for PFG. Skipping.")
        failed_tickers.append('PFG')
except Exception as e:
    print(f"(396/503) Failed to fetch data for PFG: {e}")
    failed_tickers.append('PFG')

# Ticker 397: RL
try:
    data_rl = tv.get_hist(symbol='RL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rl is not None and not data_rl.empty:
        all_data['RL'] = data_rl['close']
        print("(397/503) Successfully fetched data for RL")
    else:
        print("(397/503) No data returned for RL. Skipping.")
        failed_tickers.append('RL')
except Exception as e:
    print(f"(397/503) Failed to fetch data for RL: {e}")
    failed_tickers.append('RL')

# Ticker 398: WAT
try:
    data_wat = tv.get_hist(symbol='WAT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_wat is not None and not data_wat.empty:
        all_data['WAT'] = data_wat['close']
        print("(398/503) Successfully fetched data for WAT")
    else:
        print("(398/503) No data returned for WAT. Skipping.")
        failed_tickers.append('WAT')
except Exception as e:
    print(f"(398/503) Failed to fetch data for WAT: {e}")
    failed_tickers.append('WAT')

# Ticker 399: DOW
try:
    data_dow = tv.get_hist(symbol='DOW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dow is not None and not data_dow.empty:
        all_data['DOW'] = data_dow['close']
        print("(399/503) Successfully fetched data for DOW")
    else:
        print("(399/503) No data returned for DOW. Skipping.")
        failed_tickers.append('DOW')
except Exception as e:
    print(f"(399/503) Failed to fetch data for DOW: {e}")
    failed_tickers.append('DOW')

# Ticker 400: MAA
try:
    data_maa = tv.get_hist(symbol='MAA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_maa is not None and not data_maa.empty:
        all_data['MAA'] = data_maa['close']
        print("(400/503) Successfully fetched data for MAA")
    else:
        print("(400/503) No data returned for MAA. Skipping.")
        failed_tickers.append('MAA')
except Exception as e:
    print(f"(400/503) Failed to fetch data for MAA: {e}")
    failed_tickers.append('MAA')

# --- EXPORT CHUNK 16 (TICKERS 376-400) ---
print("\n--- Merging and exporting data for companies 376-400 ---")
chunk_16_data = {}
tickers_376_400 = {
    'NI': 'data_ni', 'MKC': 'data_mkc', 'FSLR': 'data_fslr', 'INVH': 'data_invh', 'HAL': 'data_hal', 'TSN': 'data_tsn', 'L': 'data_l', 'IFF': 'data_iff', 'ZBH': 'data_zbh', 'DGX': 'data_dgx', 'STLD': 'data_stld', 'BIIB': 'data_biib', 'GEN': 'data_gen', 'WY': 'data_wy', 'ERIE': 'data_erie', 'ESS': 'data_ess', 'GPC': 'data_gpc', 'CTRA': 'data_ctra', 'WST': 'data_wst', 'PKG': 'data_pkg', 'PFG': 'data_pfg', 'RL': 'data_rl', 'WAT': 'data_wat', 'DOW': 'data_dow', 'MAA': 'data_maa'
}
for ticker, data_var_name in tickers_376_400.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_16_data[ticker] = close_series
if chunk_16_data:
    price_df_16 = pd.DataFrame(chunk_16_data)
    price_df_16.sort_index(inplace=True)
    price_df_16.ffill(inplace=True)
    price_df_16.to_csv('sp500_prices_376-400.csv')
    print("--- Successfully exported sp500_prices_376-400.csv ---\n")
else:
    print("--- No data collected for chunk 16, skipping export. ---\n")

# Ticker 401: FTV
try:
    data_ftv = tv.get_hist(symbol='FTV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ftv is not None and not data_ftv.empty:
        all_data['FTV'] = data_ftv['close']
        print("(401/503) Successfully fetched data for FTV")
    else:
        print("(401/503) No data returned for FTV. Skipping.")
        failed_tickers.append('FTV')
except Exception as e:
    print(f"(401/503) Failed to fetch data for FTV: {e}")
    failed_tickers.append('FTV')

# Ticker 402: J
try:
    data_j = tv.get_hist(symbol='J', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_j is not None and not data_j.empty:
        all_data['J'] = data_j['close']
        print("(402/503) Successfully fetched data for J")
    else:
        print("(402/503) No data returned for J. Skipping.")
        failed_tickers.append('J')
except Exception as e:
    print(f"(402/503) Failed to fetch data for J: {e}")
    failed_tickers.append('J')

# Ticker 403: FFIV
try:
    data_ffiv = tv.get_hist(symbol='FFIV', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ffiv is not None and not data_ffiv.empty:
        all_data['FFIV'] = data_ffiv['close']
        print("(403/503) Successfully fetched data for FFIV")
    else:
        print("(403/503) No data returned for FFIV. Skipping.")
        failed_tickers.append('FFIV')
except Exception as e:
    print(f"(403/503) Failed to fetch data for FFIV: {e}")
    failed_tickers.append('FFIV')

# Ticker 404: SNA
try:
    data_sna = tv.get_hist(symbol='SNA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_sna is not None and not data_sna.empty:
        all_data['SNA'] = data_sna['close']
        print("(404/503) Successfully fetched data for SNA")
    else:
        print("(404/503) No data returned for SNA. Skipping.")
        failed_tickers.append('SNA')
except Exception as e:
    print(f"(404/503) Failed to fetch data for SNA: {e}")
    failed_tickers.append('SNA')

# Ticker 405: DECK
try:
    data_deck = tv.get_hist(symbol='DECK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_deck is not None and not data_deck.empty:
        all_data['DECK'] = data_deck['close']
        print("(405/503) Successfully fetched data for DECK")
    else:
        print("(405/503) No data returned for DECK. Skipping.")
        failed_tickers.append('DECK')
except Exception as e:
    print(f"(405/503) Failed to fetch data for DECK: {e}")
    failed_tickers.append('DECK')

# Ticker 406: ZBRA
try:
    data_zbra = tv.get_hist(symbol='ZBRA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_zbra is not None and not data_zbra.empty:
        all_data['ZBRA'] = data_zbra['close']
        print("(406/503) Successfully fetched data for ZBRA")
    else:
        print("(406/503) No data returned for ZBRA. Skipping.")
        failed_tickers.append('ZBRA')
except Exception as e:
    print(f"(406/503) Failed to fetch data for ZBRA: {e}")
    failed_tickers.append('ZBRA')

# Ticker 407: PNR
try:
    data_pnr = tv.get_hist(symbol='PNR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pnr is not None and not data_pnr.empty:
        all_data['PNR'] = data_pnr['close']
        print("(407/503) Successfully fetched data for PNR")
    else:
        print("(407/503) No data returned for PNR. Skipping.")
        failed_tickers.append('PNR')
except Exception as e:
    print(f"(407/503) Failed to fetch data for PNR: {e}")
    failed_tickers.append('PNR')

# Ticker 408: LUV
try:
    data_luv = tv.get_hist(symbol='LUV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_luv is not None and not data_luv.empty:
        all_data['LUV'] = data_luv['close']
        print("(408/503) Successfully fetched data for LUV")
    else:
        print("(408/503) No data returned for LUV. Skipping.")
        failed_tickers.append('LUV')
except Exception as e:
    print(f"(408/503) Failed to fetch data for LUV: {e}")
    failed_tickers.append('LUV')

# Ticker 409: LNT
try:
    data_lnt = tv.get_hist(symbol='LNT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_lnt is not None and not data_lnt.empty:
        all_data['LNT'] = data_lnt['close']
        print("(409/503) Successfully fetched data for LNT")
    else:
        print("(409/503) No data returned for LNT. Skipping.")
        failed_tickers.append('LNT')
except Exception as e:
    print(f"(409/503) Failed to fetch data for LNT: {e}")
    failed_tickers.append('LNT')

# Ticker 410: BALL
try:
    data_ball = tv.get_hist(symbol='BALL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ball is not None and not data_ball.empty:
        all_data['BALL'] = data_ball['close']
        print("(410/503) Successfully fetched data for BALL")
    else:
        print("(410/503) No data returned for BALL. Skipping.")
        failed_tickers.append('BALL')
except Exception as e:
    print(f"(410/503) Failed to fetch data for BALL: {e}")
    failed_tickers.append('BALL')

# Ticker 411: EVRG
try:
    data_evrg = tv.get_hist(symbol='EVRG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_evrg is not None and not data_evrg.empty:
        all_data['EVRG'] = data_evrg['close']
        print("(411/503) Successfully fetched data for EVRG")
    else:
        print("(411/503) No data returned for EVRG. Skipping.")
        failed_tickers.append('EVRG')
except Exception as e:
    print(f"(411/503) Failed to fetch data for EVRG: {e}")
    failed_tickers.append('EVRG')

# Ticker 412: DPZ
try:
    data_dpz = tv.get_hist(symbol='DPZ', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_dpz is not None and not data_dpz.empty:
        all_data['DPZ'] = data_dpz['close']
        print("(412/503) Successfully fetched data for DPZ")
    else:
        print("(412/503) No data returned for DPZ. Skipping.")
        failed_tickers.append('DPZ')
except Exception as e:
    print(f"(412/503) Failed to fetch data for DPZ: {e}")
    failed_tickers.append('DPZ')

# Ticker 413: HRL
try:
    data_hrl = tv.get_hist(symbol='HRL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hrl is not None and not data_hrl.empty:
        all_data['HRL'] = data_hrl['close']
        print("(413/503) Successfully fetched data for HRL")
    else:
        print("(413/503) No data returned for HRL. Skipping.")
        failed_tickers.append('HRL')
except Exception as e:
    print(f"(413/503) Failed to fetch data for HRL: {e}")
    failed_tickers.append('HRL')

# Ticker 414: CLX
try:
    data_clx = tv.get_hist(symbol='CLX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_clx is not None and not data_clx.empty:
        all_data['CLX'] = data_clx['close']
        print("(414/503) Successfully fetched data for CLX")
    else:
        print("(414/503) No data returned for CLX. Skipping.")
        failed_tickers.append('CLX')
except Exception as e:
    print(f"(414/503) Failed to fetch data for CLX: {e}")
    failed_tickers.append('CLX')

# Ticker 415: FDS
try:
    data_fds = tv.get_hist(symbol='FDS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_fds is not None and not data_fds.empty:
        all_data['FDS'] = data_fds['close']
        print("(415/503) Successfully fetched data for FDS")
    else:
        print("(415/503) No data returned for FDS. Skipping.")
        failed_tickers.append('FDS')
except Exception as e:
    print(f"(415/503) Failed to fetch data for FDS: {e}")
    failed_tickers.append('FDS')

# Ticker 416: BG
try:
    data_bg = tv.get_hist(symbol='BG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bg is not None and not data_bg.empty:
        all_data['BG'] = data_bg['close']
        print("(416/503) Successfully fetched data for BG")
    else:
        print("(416/503) No data returned for BG. Skipping.")
        failed_tickers.append('BG')
except Exception as e:
    print(f"(416/503) Failed to fetch data for BG: {e}")
    failed_tickers.append('BG')

# Ticker 417: CF
try:
    data_cf = tv.get_hist(symbol='CF', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cf is not None and not data_cf.empty:
        all_data['CF'] = data_cf['close']
        print("(417/503) Successfully fetched data for CF")
    else:
        print("(417/503) No data returned for CF. Skipping.")
        failed_tickers.append('CF')
except Exception as e:
    print(f"(417/503) Failed to fetch data for CF: {e}")
    failed_tickers.append('CF')

# Ticker 418: ALGN
try:
    data_algn = tv.get_hist(symbol='ALGN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_algn is not None and not data_algn.empty:
        all_data['ALGN'] = data_algn['close']
        print("(418/503) Successfully fetched data for ALGN")
    else:
        print("(418/503) No data returned for ALGN. Skipping.")
        failed_tickers.append('ALGN')
except Exception as e:
    print(f"(418/503) Failed to fetch data for ALGN: {e}")
    failed_tickers.append('ALGN')

# Ticker 419: APTV
try:
    data_aptv = tv.get_hist(symbol='APTV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aptv is not None and not data_aptv.empty:
        all_data['APTV'] = data_aptv['close']
        print("(419/503) Successfully fetched data for APTV")
    else:
        print("(419/503) No data returned for APTV. Skipping.")
        failed_tickers.append('APTV')
except Exception as e:
    print(f"(419/503) Failed to fetch data for APTV: {e}")
    failed_tickers.append('APTV')

# Ticker 420: BAX
try:
    data_bax = tv.get_hist(symbol='BAX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bax is not None and not data_bax.empty:
        all_data['BAX'] = data_bax['close']
        print("(420/503) Successfully fetched data for BAX")
    else:
        print("(420/503) No data returned for BAX. Skipping.")
        failed_tickers.append('BAX')
except Exception as e:
    print(f"(420/503) Failed to fetch data for BAX: {e}")
    failed_tickers.append('BAX')

# Ticker 421: INCY
try:
    data_incy = tv.get_hist(symbol='INCY', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_incy is not None and not data_incy.empty:
        all_data['INCY'] = data_incy['close']
        print("(421/503) Successfully fetched data for INCY")
    else:
        print("(421/503) No data returned for INCY. Skipping.")
        failed_tickers.append('INCY')
except Exception as e:
    print(f"(421/503) Failed to fetch data for INCY: {e}")
    failed_tickers.append('INCY')

# Ticker 422: KIM
try:
    data_kim = tv.get_hist(symbol='KIM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kim is not None and not data_kim.empty:
        all_data['KIM'] = data_kim['close']
        print("(422/503) Successfully fetched data for KIM")
    else:
        print("(422/503) No data returned for KIM. Skipping.")
        failed_tickers.append('KIM')
except Exception as e:
    print(f"(422/503) Failed to fetch data for KIM: {e}")
    failed_tickers.append('KIM')

# Ticker 423: HOLX
try:
    data_holx = tv.get_hist(symbol='HOLX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_holx is not None and not data_holx.empty:
        all_data['HOLX'] = data_holx['close']
        print("(423/503) Successfully fetched data for HOLX")
    else:
        print("(423/503) No data returned for HOLX. Skipping.")
        failed_tickers.append('HOLX')
except Exception as e:
    print(f"(423/503) Failed to fetch data for HOLX: {e}")
    failed_tickers.append('HOLX')

# Ticker 424: BLDR
try:
    data_bldr = tv.get_hist(symbol='BLDR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bldr is not None and not data_bldr.empty:
        all_data['BLDR'] = data_bldr['close']
        print("(424/503) Successfully fetched data for BLDR")
    else:
        print("(424/503) No data returned for BLDR. Skipping.")
        failed_tickers.append('BLDR')
except Exception as e:
    print(f"(424/503) Failed to fetch data for BLDR: {e}")
    failed_tickers.append('BLDR')

# Ticker 425: COO
try:
    data_coo = tv.get_hist(symbol='COO', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_coo is not None and not data_coo.empty:
        all_data['COO'] = data_coo['close']
        print("(425/503) Successfully fetched data for COO")
    else:
        print("(425/503) No data returned for COO. Skipping.")
        failed_tickers.append('COO')
except Exception as e:
    print(f"(425/503) Failed to fetch data for COO: {e}")
    failed_tickers.append('COO')

# --- EXPORT CHUNK 17 (TICKERS 401-425) ---
print("\n--- Merging and exporting data for companies 401-425 ---")
chunk_17_data = {}
tickers_401_425 = {
    'FTV': 'data_ftv', 'J': 'data_j', 'FFIV': 'data_ffiv', 'SNA': 'data_sna', 'DECK': 'data_deck', 'ZBRA': 'data_zbra', 'PNR': 'data_pnr', 'LUV': 'data_luv', 'LNT': 'data_lnt', 'BALL': 'data_ball', 'EVRG': 'data_evrg', 'DPZ': 'data_dpz', 'HRL': 'data_hrl', 'CLX': 'data_clx', 'FDS': 'data_fds', 'BG': 'data_bg', 'CF': 'data_cf', 'ALGN': 'data_algn', 'APTV': 'data_aptv', 'BAX': 'data_bax', 'INCY': 'data_incy', 'KIM': 'data_kim', 'HOLX': 'data_holx', 'BLDR': 'data_bldr', 'COO': 'data_coo'
}
for ticker, data_var_name in tickers_401_425.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_17_data[ticker] = close_series
if chunk_17_data:
    price_df_17 = pd.DataFrame(chunk_17_data)
    price_df_17.sort_index(inplace=True)
    price_df_17.ffill(inplace=True)
    price_df_17.to_csv('sp500_prices_401-425.csv')
    print("--- Successfully exported sp500_prices_401-425.csv ---\n")
else:
    print("--- No data collected for chunk 17, skipping export. ---\n")

# Ticker 426: OMC
try:
    data_omc = tv.get_hist(symbol='OMC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_omc is not None and not data_omc.empty:
        all_data['OMC'] = data_omc['close']
        print("(426/503) Successfully fetched data for OMC")
    else:
        print("(426/503) No data returned for OMC. Skipping.")
        failed_tickers.append('OMC')
except Exception as e:
    print(f"(426/503) Failed to fetch data for OMC: {e}")
    failed_tickers.append('OMC')

# Ticker 427: TER
try:
    data_ter = tv.get_hist(symbol='TER', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ter is not None and not data_ter.empty:
        all_data['TER'] = data_ter['close']
        print("(427/503) Successfully fetched data for TER")
    else:
        print("(427/503) No data returned for TER. Skipping.")
        failed_tickers.append('TER')
except Exception as e:
    print(f"(427/503) Failed to fetch data for TER: {e}")
    failed_tickers.append('TER')

# Ticker 428: JBHT
try:
    data_jbht = tv.get_hist(symbol='JBHT', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_jbht is not None and not data_jbht.empty:
        all_data['JBHT'] = data_jbht['close']
        print("(428/503) Successfully fetched data for JBHT")
    else:
        print("(428/503) No data returned for JBHT. Skipping.")
        failed_tickers.append('JBHT')
except Exception as e:
    print(f"(428/503) Failed to fetch data for JBHT: {e}")
    failed_tickers.append('JBHT')

# Ticker 429: BF.B
try:
    data_bfb = tv.get_hist(symbol='BF.B', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bfb is not None and not data_bfb.empty:
        all_data['BF.B'] = data_bfb['close']
        print("(429/503) Successfully fetched data for BF.B")
    else:
        print("(429/503) No data returned for BF.B. Skipping.")
        failed_tickers.append('BF.B')
except Exception as e:
    print(f"(429/503) Failed to fetch data for BF.B: {e}")
    failed_tickers.append('BF.B')

# Ticker 430: EG
try:
    data_eg = tv.get_hist(symbol='EG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_eg is not None and not data_eg.empty:
        all_data['EG'] = data_eg['close']
        print("(430/503) Successfully fetched data for EG")
    else:
        print("(430/503) No data returned for EG. Skipping.")
        failed_tickers.append('EG')
except Exception as e:
    print(f"(430/503) Failed to fetch data for EG: {e}")
    failed_tickers.append('EG')

# Ticker 431: ALLE
try:
    data_alle = tv.get_hist(symbol='ALLE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_alle is not None and not data_alle.empty:
        all_data['ALLE'] = data_alle['close']
        print("(431/503) Successfully fetched data for ALLE")
    else:
        print("(431/503) No data returned for ALLE. Skipping.")
        failed_tickers.append('ALLE')
except Exception as e:
    print(f"(431/503) Failed to fetch data for ALLE: {e}")
    failed_tickers.append('ALLE')

# Ticker 432: BBY
try:
    data_bby = tv.get_hist(symbol='BBY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bby is not None and not data_bby.empty:
        all_data['BBY'] = data_bby['close']
        print("(432/503) Successfully fetched data for BBY")
    else:
        print("(432/503) No data returned for BBY. Skipping.")
        failed_tickers.append('BBY')
except Exception as e:
    print(f"(432/503) Failed to fetch data for BBY: {e}")
    failed_tickers.append('BBY')

# Ticker 433: MAS
try:
    data_mas = tv.get_hist(symbol='MAS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mas is not None and not data_mas.empty:
        all_data['MAS'] = data_mas['close']
        print("(433/503) Successfully fetched data for MAS")
    else:
        print("(433/503) No data returned for MAS. Skipping.")
        failed_tickers.append('MAS')
except Exception as e:
    print(f"(433/503) Failed to fetch data for MAS: {e}")
    failed_tickers.append('MAS')

# Ticker 434: TXT
try:
    data_txt = tv.get_hist(symbol='TXT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_txt is not None and not data_txt.empty:
        all_data['TXT'] = data_txt['close']
        print("(434/503) Successfully fetched data for TXT")
    else:
        print("(434/503) No data returned for TXT. Skipping.")
        failed_tickers.append('TXT')
except Exception as e:
    print(f"(434/503) Failed to fetch data for TXT: {e}")
    failed_tickers.append('TXT')

# Ticker 435: IEX
try:
    data_iex = tv.get_hist(symbol='IEX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_iex is not None and not data_iex.empty:
        all_data['IEX'] = data_iex['close']
        print("(435/503) Successfully fetched data for IEX")
    else:
        print("(435/503) No data returned for IEX. Skipping.")
        failed_tickers.append('IEX')
except Exception as e:
    print(f"(435/503) Failed to fetch data for IEX: {e}")
    failed_tickers.append('IEX')

# Ticker 436: TKO
try:
    data_tko = tv.get_hist(symbol='TKO', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tko is not None and not data_tko.empty:
        all_data['TKO'] = data_tko['close']
        print("(436/503) Successfully fetched data for TKO")
    else:
        print("(436/503) No data returned for TKO. Skipping.")
        failed_tickers.append('TKO')
except Exception as e:
    print(f"(436/503) Failed to fetch data for TKO: {e}")
    failed_tickers.append('TKO')

# Ticker 437: AVY
try:
    data_avy = tv.get_hist(symbol='AVY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_avy is not None and not data_avy.empty:
        all_data['AVY'] = data_avy['close']
        print("(437/503) Successfully fetched data for AVY")
    else:
        print("(437/503) No data returned for AVY. Skipping.")
        failed_tickers.append('AVY')
except Exception as e:
    print(f"(437/503) Failed to fetch data for AVY: {e}")
    failed_tickers.append('AVY')

# Ticker 438: ARE
try:
    data_are = tv.get_hist(symbol='ARE', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_are is not None and not data_are.empty:
        all_data['ARE'] = data_are['close']
        print("(438/503) Successfully fetched data for ARE")
    else:
        print("(438/503) No data returned for ARE. Skipping.")
        failed_tickers.append('ARE')
except Exception as e:
    print(f"(438/503) Failed to fetch data for ARE: {e}")
    failed_tickers.append('ARE')

# Ticker 439: UDR
try:
    data_udr = tv.get_hist(symbol='UDR', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_udr is not None and not data_udr.empty:
        all_data['UDR'] = data_udr['close']
        print("(439/503) Successfully fetched data for UDR")
    else:
        print("(439/503) No data returned for UDR. Skipping.")
        failed_tickers.append('UDR')
except Exception as e:
    print(f"(439/503) Failed to fetch data for UDR: {e}")
    failed_tickers.append('UDR')

# Ticker 440: PAYC
try:
    data_payc = tv.get_hist(symbol='PAYC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_payc is not None and not data_payc.empty:
        all_data['PAYC'] = data_payc['close']
        print("(440/503) Successfully fetched data for PAYC")
    else:
        print("(440/503) No data returned for PAYC. Skipping.")
        failed_tickers.append('PAYC')
except Exception as e:
    print(f"(440/503) Failed to fetch data for PAYC: {e}")
    failed_tickers.append('PAYC')

# Ticker 441: CNC
try:
    data_cnc = tv.get_hist(symbol='CNC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cnc is not None and not data_cnc.empty:
        all_data['CNC'] = data_cnc['close']
        print("(441/503) Successfully fetched data for CNC")
    else:
        print("(441/503) No data returned for CNC. Skipping.")
        failed_tickers.append('CNC')
except Exception as e:
    print(f"(441/503) Failed to fetch data for CNC: {e}")
    failed_tickers.append('CNC')

# Ticker 442: REG
try:
    data_reg = tv.get_hist(symbol='REG', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_reg is not None and not data_reg.empty:
        all_data['REG'] = data_reg['close']
        print("(442/503) Successfully fetched data for REG")
    else:
        print("(442/503) No data returned for REG. Skipping.")
        failed_tickers.append('REG')
except Exception as e:
    print(f"(442/503) Failed to fetch data for REG: {e}")
    failed_tickers.append('REG')

# Ticker 443: BEN
try:
    data_ben = tv.get_hist(symbol='BEN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ben is not None and not data_ben.empty:
        all_data['BEN'] = data_ben['close']
        print("(443/503) Successfully fetched data for BEN")
    else:
        print("(443/503) No data returned for BEN. Skipping.")
        failed_tickers.append('BEN')
except Exception as e:
    print(f"(443/503) Failed to fetch data for BEN: {e}")
    failed_tickers.append('BEN')

# Ticker 444: JKHY
try:
    data_jkhy = tv.get_hist(symbol='JKHY', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_jkhy is not None and not data_jkhy.empty:
        all_data['JKHY'] = data_jkhy['close']
        print("(444/503) Successfully fetched data for JKHY")
    else:
        print("(444/503) No data returned for JKHY. Skipping.")
        failed_tickers.append('JKHY')
except Exception as e:
    print(f"(444/503) Failed to fetch data for JKHY: {e}")
    failed_tickers.append('JKHY')

# Ticker 445: SOLV
try:
    data_solv = tv.get_hist(symbol='SOLV', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_solv is not None and not data_solv.empty:
        all_data['SOLV'] = data_solv['close']
        print("(445/503) Successfully fetched data for SOLV")
    else:
        print("(445/503) No data returned for SOLV. Skipping.")
        failed_tickers.append('SOLV')
except Exception as e:
    print(f"(445/503) Failed to fetch data for SOLV: {e}")
    failed_tickers.append('SOLV')

# Ticker 446: MRNA
try:
    data_mrna = tv.get_hist(symbol='MRNA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mrna is not None and not data_mrna.empty:
        all_data['MRNA'] = data_mrna['close']
        print("(446/503) Successfully fetched data for MRNA")
    else:
        print("(446/503) No data returned for MRNA. Skipping.")
        failed_tickers.append('MRNA')
except Exception as e:
    print(f"(446/503) Failed to fetch data for MRNA: {e}")
    failed_tickers.append('MRNA')

# Ticker 447: NDSN
try:
    data_ndsn = tv.get_hist(symbol='NDSN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_ndsn is not None and not data_ndsn.empty:
        all_data['NDSN'] = data_ndsn['close']
        print("(447/503) Successfully fetched data for NDSN")
    else:
        print("(447/503) No data returned for NDSN. Skipping.")
        failed_tickers.append('NDSN')
except Exception as e:
    print(f"(447/503) Failed to fetch data for NDSN: {e}")
    failed_tickers.append('NDSN')

# Ticker 448: CPT
try:
    data_cpt = tv.get_hist(symbol='CPT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cpt is not None and not data_cpt.empty:
        all_data['CPT'] = data_cpt['close']
        print("(448/503) Successfully fetched data for CPT")
    else:
        print("(448/503) No data returned for CPT. Skipping.")
        failed_tickers.append('CPT')
except Exception as e:
    print(f"(448/503) Failed to fetch data for CPT: {e}")
    failed_tickers.append('CPT')

# Ticker 449: FOX
try:
    data_fox = tv.get_hist(symbol='FOX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_fox is not None and not data_fox.empty:
        all_data['FOX'] = data_fox['close']
        print("(449/503) Successfully fetched data for FOX")
    else:
        print("(449/503) No data returned for FOX. Skipping.")
        failed_tickers.append('FOX')
except Exception as e:
    print(f"(449/503) Failed to fetch data for FOX: {e}")
    failed_tickers.append('FOX')

# Ticker 450: PEAK
try:
    data_peak = tv.get_hist(symbol='PEAK', exchange='TSXV', interval=INTERVAL, n_bars=N_BARS)
    if data_peak is not None and not data_peak.empty:
        all_data['PEAK'] = data_peak['close']
        print("(450/503) Successfully fetched data for PEAK")
    else:
        print("(450/503) No data returned for PEAK. Skipping.")
        failed_tickers.append('PEAK')
except Exception as e:
    print(f"(450/503) Failed to fetch data for PEAK: {e}")
    failed_tickers.append('PEAK')


# --- EXPORT CHUNK 18 (TICKERS 426-450) ---
print("\n--- Merging and exporting data for companies 426-450 ---")
chunk_18_data = {}
tickers_426_450 = {
    'OMC': 'data_omc', 'TER': 'data_ter', 'JBHT': 'data_jbht', 'BF.B': 'data_bf_b', 'EG': 'data_eg', 'ALLE': 'data_alle', 'BBY': 'data_bby', 'MAS': 'data_mas', 'TXT': 'data_txt', 'IEX': 'data_iex', 'TKO': 'data_tko', 'AVY': 'data_avy', 'ARE': 'data_are', 'UDR': 'data_udr', 'PAYC': 'data_payc', 'CNC': 'data_cnc', 'REG': 'data_reg', 'BEN': 'data_ben', 'JKHY': 'data_jkhy', 'SOLV': 'data_solv', 'MRNA': 'data_mrna', 'NDSN': 'data_ndsn', 'CPT': 'data_cpt', 'FOX': 'data_fox', 'PEAK': 'data_peak'
}
for ticker, data_var_name in tickers_426_450.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_18_data[ticker] = close_series
if chunk_18_data:
    price_df_18 = pd.DataFrame(chunk_18_data)
    price_df_18.sort_index(inplace=True)
    price_df_18.ffill(inplace=True)
    price_df_18.to_csv('sp500_prices_426-450.csv')
    print("--- Successfully exported sp500_prices_426-450.csv ---\n")
else:
    print("--- No data collected for chunk 18, skipping export. ---\n")
    
    

# Ticker 451: FOXA
try:
    data_foxa = tv.get_hist(symbol='FOXA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_foxa is not None and not data_foxa.empty:
        all_data['FOXA'] = data_foxa['close']
        print("(451/503) Successfully fetched data for FOXA")
    else:
        print("(451/503) No data returned for FOXA. Skipping.")
        failed_tickers.append('FOXA')
except Exception as e:
    print(f"(451/503) Failed to fetch data for FOXA: {e}")
    failed_tickers.append('FOXA')

# Ticker 452: POOL
try:
    data_pool = tv.get_hist(symbol='POOL', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_pool is not None and not data_pool.empty:
        all_data['POOL'] = data_pool['close']
        print("(452/503) Successfully fetched data for POOL")
    else:
        print("(452/503) No data returned for POOL. Skipping.")
        failed_tickers.append('POOL')
except Exception as e:
    print(f"(452/503) Failed to fetch data for POOL: {e}")
    failed_tickers.append('POOL')

# Ticker 453: CHRW
try:
    data_chrw = tv.get_hist(symbol='CHRW', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_chrw is not None and not data_chrw.empty:
        all_data['CHRW'] = data_chrw['close']
        print("(453/503) Successfully fetched data for CHRW")
    else:
        print("(453/503) No data returned for CHRW. Skipping.")
        failed_tickers.append('CHRW')
except Exception as e:
    print(f"(453/503) Failed to fetch data for CHRW: {e}")
    failed_tickers.append('CHRW')

# Ticker 454: SJM
try:
    data_sjm = tv.get_hist(symbol='SJM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_sjm is not None and not data_sjm.empty:
        all_data['SJM'] = data_sjm['close']
        print("(454/503) Successfully fetched data for SJM")
    else:
        print("(454/503) No data returned for SJM. Skipping.")
        failed_tickers.append('SJM')
except Exception as e:
    print(f"(454/503) Failed to fetch data for SJM: {e}")
    failed_tickers.append('SJM')

# Ticker 455: GL
try:
    data_gl = tv.get_hist(symbol='GL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gl is not None and not data_gl.empty:
        all_data['GL'] = data_gl['close']
        print("(455/503) Successfully fetched data for GL")
    else:
        print("(455/503) No data returned for GL. Skipping.")
        failed_tickers.append('GL')
except Exception as e:
    print(f"(455/503) Failed to fetch data for GL: {e}")
    failed_tickers.append('GL')

# Ticker 456: MOS
try:
    data_mos = tv.get_hist(symbol='MOS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mos is not None and not data_mos.empty:
        all_data['MOS'] = data_mos['close']
        print("(456/503) Successfully fetched data for MOS")
    else:
        print("(456/503) No data returned for MOS. Skipping.")
        failed_tickers.append('MOS')
except Exception as e:
    print(f"(456/503) Failed to fetch data for MOS: {e}")
    failed_tickers.append('MOS')

# Ticker 457: WYNN
try:
    data_wynn = tv.get_hist(symbol='WYNN', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wynn is not None and not data_wynn.empty:
        all_data['WYNN'] = data_wynn['close']
        print("(457/503) Successfully fetched data for WYNN")
    else:
        print("(457/503) No data returned for WYNN. Skipping.")
        failed_tickers.append('WYNN')
except Exception as e:
    print(f"(457/503) Failed to fetch data for WYNN: {e}")
    failed_tickers.append('WYNN')

# Ticker 458: HST
try:
    data_hst = tv.get_hist(symbol='HST', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_hst is not None and not data_hst.empty:
        all_data['HST'] = data_hst['close']
        print("(458/503) Successfully fetched data for HST")
    else:
        print("(458/503) No data returned for HST. Skipping.")
        failed_tickers.append('HST')
except Exception as e:
    print(f"(458/503) Failed to fetch data for HST: {e}")
    failed_tickers.append('HST')

# Ticker 459: AKAM
try:
    data_akam = tv.get_hist(symbol='AKAM', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_akam is not None and not data_akam.empty:
        all_data['AKAM'] = data_akam['close']
        print("(459/503) Successfully fetched data for AKAM")
    else:
        print("(459/503) No data returned for AKAM. Skipping.")
        failed_tickers.append('AKAM')
except Exception as e:
    print(f"(459/503) Failed to fetch data for AKAM: {e}")
    failed_tickers.append('AKAM')

# Ticker 460: RVTY
try:
    data_rvty = tv.get_hist(symbol='RVTY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rvty is not None and not data_rvty.empty:
        all_data['RVTY'] = data_rvty['close']
        print("(460/503) Successfully fetched data for RVTY")
    else:
        print("(460/503) No data returned for RVTY. Skipping.")
        failed_tickers.append('RVTY')
except Exception as e:
    print(f"(460/503) Failed to fetch data for RVTY: {e}")
    failed_tickers.append('RVTY')

# Ticker 461: DVA
try:
    data_dva = tv.get_hist(symbol='DVA', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_dva is not None and not data_dva.empty:
        all_data['DVA'] = data_dva['close']
        print("(461/503) Successfully fetched data for DVA")
    else:
        print("(461/503) No data returned for DVA. Skipping.")
        failed_tickers.append('DVA')
except Exception as e:
    print(f"(461/503) Failed to fetch data for DVA: {e}")
    failed_tickers.append('DVA')

# Ticker 462: NWSA
try:
    data_nwsa = tv.get_hist(symbol='NWSA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_nwsa is not None and not data_nwsa.empty:
        all_data['NWSA'] = data_nwsa['close']
        print("(462/503) Successfully fetched data for NWSA")
    else:
        print("(462/503) No data returned for NWSA. Skipping.")
        failed_tickers.append('NWSA')
except Exception as e:
    print(f"(462/503) Failed to fetch data for NWSA: {e}")
    failed_tickers.append('NWSA')

# Ticker 463: BXP
try:
    data_bxp = tv.get_hist(symbol='BXP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_bxp is not None and not data_bxp.empty:
        all_data['BXP'] = data_bxp['close']
        print("(463/503) Successfully fetched data for BXP")
    else:
        print("(463/503) No data returned for BXP. Skipping.")
        failed_tickers.append('BXP')
except Exception as e:
    print(f"(463/503) Failed to fetch data for BXP: {e}")
    failed_tickers.append('BXP')

# Ticker 464: VTRS
try:
    data_vtrs = tv.get_hist(symbol='VTRS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_vtrs is not None and not data_vtrs.empty:
        all_data['VTRS'] = data_vtrs['close']
        print("(464/503) Successfully fetched data for VTRS")
    else:
        print("(464/503) No data returned for VTRS. Skipping.")
        failed_tickers.append('VTRS')
except Exception as e:
    print(f"(464/503) Failed to fetch data for VTRS: {e}")
    failed_tickers.append('VTRS')

# Ticker 465: PNW
try:
    data_pnw = tv.get_hist(symbol='PNW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_pnw is not None and not data_pnw.empty:
        all_data['PNW'] = data_pnw['close']
        print("(465/503) Successfully fetched data for PNW")
    else:
        print("(465/503) No data returned for PNW. Skipping.")
        failed_tickers.append('PNW')
except Exception as e:
    print(f"(465/503) Failed to fetch data for PNW: {e}")
    failed_tickers.append('PNW')

# Ticker 466: HAS
try:
    data_has = tv.get_hist(symbol='HAS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_has is not None and not data_has.empty:
        all_data['HAS'] = data_has['close']
        print("(466/503) Successfully fetched data for HAS")
    else:
        print("(466/503) No data returned for HAS. Skipping.")
        failed_tickers.append('HAS')
except Exception as e:
    print(f"(466/503) Failed to fetch data for HAS: {e}")
    failed_tickers.append('HAS')

# Ticker 467: SWKS
try:
    data_swks = tv.get_hist(symbol='SWKS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_swks is not None and not data_swks.empty:
        all_data['SWKS'] = data_swks['close']
        print("(467/503) Successfully fetched data for SWKS")
    else:
        print("(467/503) No data returned for SWKS. Skipping.")
        failed_tickers.append('SWKS')
except Exception as e:
    print(f"(467/503) Failed to fetch data for SWKS: {e}")
    failed_tickers.append('SWKS')

# Ticker 468: NCLH
try:
    data_nclh = tv.get_hist(symbol='NCLH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_nclh is not None and not data_nclh.empty:
        all_data['NCLH'] = data_nclh['close']
        print("(468/503) Successfully fetched data for NCLH")
    else:
        print("(468/503) No data returned for NCLH. Skipping.")
        failed_tickers.append('NCLH')
except Exception as e:
    print(f"(468/503) Failed to fetch data for NCLH: {e}")
    failed_tickers.append('NCLH')

# Ticker 469: SWK
try:
    data_swk = tv.get_hist(symbol='SWK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_swk is not None and not data_swk.empty:
        all_data['SWK'] = data_swk['close']
        print("(469/503) Successfully fetched data for SWK")
    else:
        print("(469/503) No data returned for SWK. Skipping.")
        failed_tickers.append('SWK')
except Exception as e:
    print(f"(469/503) Failed to fetch data for SWK: {e}")
    failed_tickers.append('SWK')

# Ticker 470: UHS
try:
    data_uhs = tv.get_hist(symbol='UHS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_uhs is not None and not data_uhs.empty:
        all_data['UHS'] = data_uhs['close']
        print("(470/503) Successfully fetched data for UHS")
    else:
        print("(470/503) No data returned for UHS. Skipping.")
        failed_tickers.append('UHS')
except Exception as e:
    print(f"(470/503) Failed to fetch data for UHS: {e}")
    failed_tickers.append('UHS')

# Ticker 471: HII
try:
    data_hii = tv.get_hist(symbol='HII', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_hii is not None and not data_hii.empty:
        all_data['HII'] = data_hii['close']
        print("(471/503) Successfully fetched data for HII")
    else:
        print("(471/503) No data returned for HII. Skipping.")
        failed_tickers.append('HII')
except Exception as e:
    print(f"(471/503) Failed to fetch data for HII: {e}")
    failed_tickers.append('HII')

# Ticker 472: TAP
try:
    data_tap = tv.get_hist(symbol='TAP', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_tap is not None and not data_tap.empty:
        all_data['TAP'] = data_tap['close']
        print("(472/503) Successfully fetched data for TAP")
    else:
        print("(472/503) No data returned for TAP. Skipping.")
        failed_tickers.append('TAP')
except Exception as e:
    print(f"(472/503) Failed to fetch data for TAP: {e}")
    failed_tickers.append('TAP')

# Ticker 473: MGM
try:
    data_mgm = tv.get_hist(symbol='MGM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mgm is not None and not data_mgm.empty:
        all_data['MGM'] = data_mgm['close']
        print("(473/503) Successfully fetched data for MGM")
    else:
        print("(473/503) No data returned for MGM. Skipping.")
        failed_tickers.append('MGM')
except Exception as e:
    print(f"(473/503) Failed to fetch data for MGM: {e}")
    failed_tickers.append('MGM')

# Ticker 474: WBA
try:
    data_wba = tv.get_hist(symbol='WBA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_wba is not None and not data_wba.empty:
        all_data['WBA'] = data_wba['close']
        print("(474/503) Successfully fetched data for WBA")
    else:
        print("(474/503) No data returned for WBA. Skipping.")
        failed_tickers.append('WBA')
except Exception as e:
    print(f"(474/503) Failed to fetch data for WBA: {e}")
    failed_tickers.append('WBA')

# Ticker 475: AOS
try:
    data_aos = tv.get_hist(symbol='AOS', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aos is not None and not data_aos.empty:
        all_data['AOS'] = data_aos['close']
        print("(475/503) Successfully fetched data for AOS")
    else:
        print("(475/503) No data returned for AOS. Skipping.")
        failed_tickers.append('AOS')
except Exception as e:
    print(f"(475/503) Failed to fetch data for AOS: {e}")
    failed_tickers.append('AOS')

# --- EXPORT CHUNK 19 (TICKERS 451-475) ---
print("\n--- Merging and exporting data for companies 451-475 ---")
chunk_19_data = {}
tickers_451_475 = {
    'FOXA': 'data_foxa', 'POOL': 'data_pool', 'CHRW': 'data_chrw', 'SJM': 'data_sjm', 'GL': 'data_gl', 'MOS': 'data_mos', 'WYNN': 'data_wynn', 'HST': 'data_hst', 'AKAM': 'data_akam', 'RVTY': 'data_rvty', 'DVA': 'data_dva', 'NWSA': 'data_nwsa', 'BXP': 'data_bxp', 'VTRS': 'data_vtrs', 'PNW': 'data_pnw', 'HAS': 'data_has', 'SWKS': 'data_swks', 'NCLH': 'data_nclh', 'SWK': 'data_swk', 'UHS': 'data_uhs', 'HII': 'data_hii', 'TAP': 'data_tap', 'MGM': 'data_mgm', 'WBA': 'data_wba', 'AOS': 'data_aos'
}
for ticker, data_var_name in tickers_451_475.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_19_data[ticker] = close_series
if chunk_19_data:
    price_df_19 = pd.DataFrame(chunk_19_data)
    price_df_19.sort_index(inplace=True)
    price_df_19.ffill(inplace=True)
    price_df_19.to_csv('sp500_prices_451-475.csv')
    print("--- Successfully exported sp500_prices_451-475.csv ---\n")
else:
    print("--- No data collected for chunk 19, skipping export. ---\n")

# Ticker 476: CPB
try:
    data_cpb = tv.get_hist(symbol='CPB', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_cpb is not None and not data_cpb.empty:
        all_data['CPB'] = data_cpb['close']
        print("(476/503) Successfully fetched data for CPB")
    else:
        print("(476/503) No data returned for CPB. Skipping.")
        failed_tickers.append('CPB')
except Exception as e:
    print(f"(476/503) Failed to fetch data for CPB: {e}")
    failed_tickers.append('CPB')

# Ticker 477: IVZ
try:
    data_ivz = tv.get_hist(symbol='IVZ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ivz is not None and not data_ivz.empty:
        all_data['IVZ'] = data_ivz['close']
        print("(477/503) Successfully fetched data for IVZ")
    else:
        print("(477/503) No data returned for IVZ. Skipping.")
        failed_tickers.append('IVZ')
except Exception as e:
    print(f"(477/503) Failed to fetch data for IVZ: {e}")
    failed_tickers.append('IVZ')

# Ticker 478: EPAM
try:
    data_epam = tv.get_hist(symbol='EPAM', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_epam is not None and not data_epam.empty:
        all_data['EPAM'] = data_epam['close']
        print("(478/503) Successfully fetched data for EPAM")
    else:
        print("(478/503) No data returned for EPAM. Skipping.")
        failed_tickers.append('EPAM')
except Exception as e:
    print(f"(478/503) Failed to fetch data for EPAM: {e}")
    failed_tickers.append('EPAM')

# Ticker 479: AES
try:
    data_aes = tv.get_hist(symbol='AES', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aes is not None and not data_aes.empty:
        all_data['AES'] = data_aes['close']
        print("(479/503) Successfully fetched data for AES")
    else:
        print("(479/503) No data returned for AES. Skipping.")
        failed_tickers.append('AES')
except Exception as e:
    print(f"(479/503) Failed to fetch data for AES: {e}")
    failed_tickers.append('AES')

# Ticker 480: AIZ
try:
    data_aiz = tv.get_hist(symbol='AIZ', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_aiz is not None and not data_aiz.empty:
        all_data['AIZ'] = data_aiz['close']
        print("(480/503) Successfully fetched data for AIZ")
    else:
        print("(480/503) No data returned for AIZ. Skipping.")
        failed_tickers.append('AIZ')
except Exception as e:
    print(f"(480/503) Failed to fetch data for AIZ: {e}")
    failed_tickers.append('AIZ')

# Ticker 481: DAY
try:
    data_day = tv.get_hist(symbol='DAY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_day is not None and not data_day.empty:
        all_data['DAY'] = data_day['close']
        print("(481/503) Successfully fetched data for DAY")
    else:
        print("(481/503) No data returned for DAY. Skipping.")
        failed_tickers.append('DAY')
except Exception as e:
    print(f"(481/503) Failed to fetch data for DAY: {e}")
    failed_tickers.append('DAY')

# Ticker 482: IPG
try:
    data_ipg = tv.get_hist(symbol='IPG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_ipg is not None and not data_ipg.empty:
        all_data['IPG'] = data_ipg['close']
        print("(482/503) Successfully fetched data for IPG")
    else:
        print("(482/503) No data returned for IPG. Skipping.")
        failed_tickers.append('IPG')
except Exception as e:
    print(f"(482/503) Failed to fetch data for IPG: {e}")
    failed_tickers.append('IPG')

# Ticker 483: CAG
try:
    data_cag = tv.get_hist(symbol='CAG', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_cag is not None and not data_cag.empty:
        all_data['CAG'] = data_cag['close']
        print("(483/503) Successfully fetched data for CAG")
    else:
        print("(483/503) No data returned for CAG. Skipping.")
        failed_tickers.append('CAG')
except Exception as e:
    print(f"(483/503) Failed to fetch data for CAG: {e}")
    failed_tickers.append('CAG')

# Ticker 484: MOH
try:
    data_moh = tv.get_hist(symbol='MOH', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_moh is not None and not data_moh.empty:
        all_data['MOH'] = data_moh['close']
        print("(484/503) Successfully fetched data for MOH")
    else:
        print("(484/503) No data returned for MOH. Skipping.")
        failed_tickers.append('MOH')
except Exception as e:
    print(f"(484/503) Failed to fetch data for MOH: {e}")
    failed_tickers.append('MOH')

# Ticker 485: GNRC
try:
    data_gnrc = tv.get_hist(symbol='GNRC', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_gnrc is not None and not data_gnrc.empty:
        all_data['GNRC'] = data_gnrc['close']
        print("(485/503) Successfully fetched data for GNRC")
    else:
        print("(485/503) No data returned for GNRC. Skipping.")
        failed_tickers.append('GNRC')
except Exception as e:
    print(f"(485/503) Failed to fetch data for GNRC: {e}")
    failed_tickers.append('GNRC')

# Ticker 486: TECH
try:
    data_tech = tv.get_hist(symbol='TECH', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_tech is not None and not data_tech.empty:
        all_data['TECH'] = data_tech['close']
        print("(486/503) Successfully fetched data for TECH")
    else:
        print("(486/503) No data returned for TECH. Skipping.")
        failed_tickers.append('TECH')
except Exception as e:
    print(f"(486/503) Failed to fetch data for TECH: {e}")
    failed_tickers.append('TECH')

# Ticker 487: PARA
try:
    data_para = tv.get_hist(symbol='PARA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_para is not None and not data_para.empty:
        all_data['PARA'] = data_para['close']
        print("(487/503) Successfully fetched data for PARA")
    else:
        print("(487/503) No data returned for PARA. Skipping.")
        failed_tickers.append('PARA')
except Exception as e:
    print(f"(487/503) Failed to fetch data for PARA: {e}")
    failed_tickers.append('PARA')

# Ticker 488: KMX
try:
    data_kmx = tv.get_hist(symbol='KMX', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_kmx is not None and not data_kmx.empty:
        all_data['KMX'] = data_kmx['close']
        print("(488/503) Successfully fetched data for KMX")
    else:
        print("(488/503) No data returned for KMX. Skipping.")
        failed_tickers.append('KMX')
except Exception as e:
    print(f"(488/503) Failed to fetch data for KMX: {e}")
    failed_tickers.append('KMX')

# Ticker 489: HSIC
try:
    data_hsic = tv.get_hist(symbol='HSIC', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_hsic is not None and not data_hsic.empty:
        all_data['HSIC'] = data_hsic['close']
        print("(489/503) Successfully fetched data for HSIC")
    else:
        print("(489/503) No data returned for HSIC. Skipping.")
        failed_tickers.append('HSIC')
except Exception as e:
    print(f"(489/503) Failed to fetch data for HSIC: {e}")
    failed_tickers.append('HSIC')

# Ticker 490: EMN
try:
    data_emn = tv.get_hist(symbol='EMN', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_emn is not None and not data_emn.empty:
        all_data['EMN'] = data_emn['close']
        print("(490/503) Successfully fetched data for EMN")
    else:
        print("(490/503) No data returned for EMN. Skipping.")
        failed_tickers.append('EMN')
except Exception as e:
    print(f"(490/503) Failed to fetch data for EMN: {e}")
    failed_tickers.append('EMN')

# Ticker 491: CRL
try:
    data_crl = tv.get_hist(symbol='CRL', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_crl is not None and not data_crl.empty:
        all_data['CRL'] = data_crl['close']
        print("(491/503) Successfully fetched data for CRL")
    else:
        print("(491/503) No data returned for CRL. Skipping.")
        failed_tickers.append('CRL')
except Exception as e:
    print(f"(491/503) Failed to fetch data for CRL: {e}")
    failed_tickers.append('CRL')

# Ticker 492: ALB
try:
    data_alb = tv.get_hist(symbol='ALB', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_alb is not None and not data_alb.empty:
        all_data['ALB'] = data_alb['close']
        print("(492/503) Successfully fetched data for ALB")
    else:
        print("(492/503) No data returned for ALB. Skipping.")
        failed_tickers.append('ALB')
except Exception as e:
    print(f"(492/503) Failed to fetch data for ALB: {e}")
    failed_tickers.append('ALB')

# Ticker 493: MTCH
try:
    data_mtch = tv.get_hist(symbol='MTCH', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mtch is not None and not data_mtch.empty:
        all_data['MTCH'] = data_mtch['close']
        print("(493/503) Successfully fetched data for MTCH")
    else:
        print("(493/503) No data returned for MTCH. Skipping.")
        failed_tickers.append('MTCH')
except Exception as e:
    print(f"(493/503) Failed to fetch data for MTCH: {e}")
    failed_tickers.append('MTCH')

# Ticker 494: LW
try:
    data_lw = tv.get_hist(symbol='LW', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_lw is not None and not data_lw.empty:
        all_data['LW'] = data_lw['close']
        print("(494/503) Successfully fetched data for LW")
    else:
        print("(494/503) No data returned for LW. Skipping.")
        failed_tickers.append('LW')
except Exception as e:
    print(f"(494/503) Failed to fetch data for LW: {e}")
    failed_tickers.append('LW')

# Ticker 495: FRT
try:
    data_frt = tv.get_hist(symbol='FRT', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_frt is not None and not data_frt.empty:
        all_data['FRT'] = data_frt['close']
        print("(495/503) Successfully fetched data for FRT")
    else:
        print("(495/503) No data returned for FRT. Skipping.")
        failed_tickers.append('FRT')
except Exception as e:
    print(f"(495/503) Failed to fetch data for FRT: {e}")
    failed_tickers.append('FRT')

# Ticker 496: LKQ
try:
    data_lkq = tv.get_hist(symbol='LKQ', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_lkq is not None and not data_lkq.empty:
        all_data['LKQ'] = data_lkq['close']
        print("(496/503) Successfully fetched data for LKQ")
    else:
        print("(496/503) No data returned for LKQ. Skipping.")
        failed_tickers.append('LKQ')
except Exception as e:
    print(f"(496/503) Failed to fetch data for LKQ: {e}")
    failed_tickers.append('LKQ')

# Ticker 497: MKTX
try:
    data_mktx = tv.get_hist(symbol='MKTX', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_mktx is not None and not data_mktx.empty:
        all_data['MKTX'] = data_mktx['close']
        print("(497/503) Successfully fetched data for MKTX")
    else:
        print("(497/503) No data returned for MKTX. Skipping.")
        failed_tickers.append('MKTX')
except Exception as e:
    print(f"(497/503) Failed to fetch data for MKTX: {e}")
    failed_tickers.append('MKTX')

# Ticker 498: MHK
try:
    data_mhk = tv.get_hist(symbol='MHK', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_mhk is not None and not data_mhk.empty:
        all_data['MHK'] = data_mhk['close']
        print("(498/503) Successfully fetched data for MHK")
    else:
        print("(498/503) No data returned for MHK. Skipping.")
        failed_tickers.append('MHK')
except Exception as e:
    print(f"(498/503) Failed to fetch data for MHK: {e}")
    failed_tickers.append('MHK')

# Ticker 499: APA
try:
    data_apa = tv.get_hist(symbol='APA', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_apa is not None and not data_apa.empty:
        all_data['APA'] = data_apa['close']
        print("(499/503) Successfully fetched data for APA")
    else:
        print("(499/503) No data returned for APA. Skipping.")
        failed_tickers.append('APA')
except Exception as e:
    print(f"(499/503) Failed to fetch data for APA: {e}")
    failed_tickers.append('APA')

# Ticker 500: NWS
try:
    data_nws = tv.get_hist(symbol='NWS', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_nws is not None and not data_nws.empty:
        all_data['NWS'] = data_nws['close']
        print("(500/503) Successfully fetched data for NWS")
    else:
        print("(500/503) No data returned for NWS. Skipping.")
        failed_tickers.append('NWS')
except Exception as e:
    print(f"(500/503) Failed to fetch data for NWS: {e}")
    failed_tickers.append('NWS')

# Ticker 501: CZR
try:
    data_czr = tv.get_hist(symbol='CZR', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_czr is not None and not data_czr.empty:
        all_data['CZR'] = data_czr['close']
        print("(501/503) Successfully fetched data for CZR")
    else:
        print("(501/503) No data returned for CZR. Skipping.")
        failed_tickers.append('CZR')
except Exception as e:
    print(f"(501/503) Failed to fetch data for CZR: {e}")
    failed_tickers.append('CZR')

# Ticker 502: ENPH
try:
    data_enph = tv.get_hist(symbol='ENPH', exchange='NASDAQ', interval=INTERVAL, n_bars=N_BARS)
    if data_enph is not None and not data_enph.empty:
        all_data['ENPH'] = data_enph['close']
        print("(502/503) Successfully fetched data for ENPH")
    else:
        print("(502/503) No data returned for ENPH. Skipping.")
        failed_tickers.append('ENPH')
except Exception as e:
    print(f"(502/503) Failed to fetch data for ENPH: {e}")
    failed_tickers.append('ENPH')

# Ticker 503: RVTY (Assuming RVTY from earlier lists, as the PDF is inconsistent)
try:
    data_rvty = tv.get_hist(symbol='RVTY', exchange='NYSE', interval=INTERVAL, n_bars=N_BARS)
    if data_rvty is not None and not data_rvty.empty:
        all_data['RVTY'] = data_rvty['close']
        print("(503/503) Successfully fetched data for RVTY")
    else:
        print("(503/503) No data returned for RVTY. Skipping.")
        failed_tickers.append('RVTY')
except Exception as e:
    print(f"(503/503) Failed to fetch data for RVTY: {e}")
    failed_tickers.append('RVTY')


# --- EXPORT FINAL CHUNK (TICKERS 476-503) ---
print("\n--- Merging and exporting data for companies 476-503 ---")
chunk_final_data = {}
tickers_476_503 = {
    'CPB': 'data_cpb', 'IVZ': 'data_ivz', 'EPAM': 'data_epam', 'AES': 'data_aes', 'AIZ': 'data_aiz', 'DAY': 'data_day', 'IPG': 'data_ipg', 'CAG': 'data_cag', 'MOH': 'data_moh', 'GNRC': 'data_gnrc', 'TECH': 'data_tech', 'PARA': 'data_para', 'KMX': 'data_kmx', 'HSIC': 'data_hsic', 'EMN': 'data_emn', 'CRL': 'data_crl', 'ALB': 'data_alb', 'MTCH': 'data_mtch', 'LW': 'data_lw', 'FRT': 'data_frt', 'LKQ': 'data_lkq', 'MKTX': 'data_mktx', 'MHK': 'data_mhk', 'APA': 'data_apa', 'NWS': 'data_nws', 'CZR': 'data_czr', 'ENPH': 'data_enph', 'RVTY': 'data_rvty'
}
for ticker, data_var_name in tickers_476_503.items():
    if data_var_name in locals() and locals()[data_var_name] is not None and not locals()[data_var_name].empty:
        close_series = locals()[data_var_name]['close']
        close_series.index = close_series.index.tz_localize(None).normalize()
        chunk_final_data[ticker] = close_series
if chunk_final_data:
    price_df_final = pd.DataFrame(chunk_final_data)
    price_df_final.sort_index(inplace=True)
    price_df_final.ffill(inplace=True)
    price_df_final.to_csv('sp500_prices_476-503.csv')
    print("--- Successfully exported sp500_prices_476-503.csv ---\n")
else:
    print("--- No data collected for the final chunk, skipping export. ---\n")

