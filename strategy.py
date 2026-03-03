# формулы стратегии (mean10, mean8worst, D, сравнение с акциями)

def calculate_dispersion(price_dataframe):
    total_returns = (price_dataframe.iloc[-1] / price_dataframe.iloc[0]) - 1
    portfolio_return = total_returns.mean()
    worst_8_returns = total_returns.sort_values()[:8].mean()
    total_spread = portfolio_return - worst_8_returns
    return total_spread