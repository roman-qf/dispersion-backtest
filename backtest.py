# генерация окон сделок и сбор результатов в таблицу
from strategy import calculate_dispersion

def run_backtest(prices, product_period_days, dt):
    total_returns = prices / prices.shift(product_period_days) - 1
    res = calculate_dispersion(total_returns)
    return res.iloc[::dt].dropna()
