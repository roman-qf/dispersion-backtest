# точка входа: принимает тикеры, запускает бэктест, печатает/рисует результат
from data import load_adj_close
from backtest import run_backtest
from report import show_charts, build_report

if __name__ == "__main__":

    # tickers = [input() for _ in range(10)]
    tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "JPM", "V", "WMT"]   # Configuration
    # product_period = int(input())
    product_period = 5  # Configuration
    product_period_days = product_period * 252
    dt = 1      # Configuration, сдвиг бэктест
    rf = 0      # Безрисковая ставка
    prices = load_adj_close(tickers,"2010-01-01", "2026-02-10")

    df = run_backtest(prices, product_period_days, dt)
    print(df)
    
    res_df, benchmarks = build_report(df=df, rf=rf)
    print(res_df)
    print("--- Результаты бэктеста ---")
    for key, value in benchmarks.items():
        if key == 'Sharpe':
            print(f'{key} {value:.2f}')
        else:
            print(f'{key} {value:.2%}')

    show_charts(res_df)