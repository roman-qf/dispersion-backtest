# формулы стратегии (mean10, mean8worst, D, сравнение с акциями)
import pandas as pd


def calculate_dispersion(total_returns):
    portfolio_return = total_returns.mean(axis=1)
    worst_8_returns = total_returns.apply(lambda row: row.nsmallest(8).mean(), axis=1)
    total_spread = portfolio_return - worst_8_returns
    df_results = pd.concat([portfolio_return, worst_8_returns, total_spread], axis=1, keys=['Portfolio', 'Worst_8', 'Spread'])
    return df_results