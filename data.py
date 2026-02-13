# загрузка цен и приведение к нужной частоте (месяц)
import yfinance as yf

def load_adj_close(tickers, start, end):
    raw = yf.download(tickers=tickers, start=start, end=end, auto_adjust=False)
    if "Adj Close" in raw.columns.get_level_values(0):
        prices = raw["Adj Close"]
    else:
        prices = raw["Close"]
    return prices
