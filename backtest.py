# генерация окон сделок и сбор результатов в таблицу
from strategy import calculate_dispersion
import pandas as pd
from report import build_report

def run_backtest(prices, product_period_days, dt):
    backtest_res = []
    # цикл бэктеста
    for i in range(0, len(prices) - product_period_days, dt):
        current_window = prices.iloc[i:product_period_days+i]
        deal_data = {'Date': current_window.index[0], 'Profit': calculate_dispersion(price_dataframe=current_window)}
        backtest_res.append(deal_data)
    df = pd.DataFrame(backtest_res)
    df = build_report(df)
    return df
