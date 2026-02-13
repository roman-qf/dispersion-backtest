# точка входа: принимает тикеры, запускает бэктест, печатает/рисует результат
from data import load_adj_close
from backtest import run_backtest
from report import show_charts

if __name__ == "__main__":

    # tickers = [input() for _ in range(10)]
    tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "JPM", "V", "WMT"]   # Configuration
    # product_period = int(input())
    product_period = 5  # Configuration
    product_period_days = product_period * 252
    dt = 2      # Configuration    # сдвиг бэктеста
    prices = load_adj_close(tickers,"2015-01-01", "2026-02-10")

    df = run_backtest(prices, product_period_days, dt)

    show_charts(df)