# группировки по диапазонам, итоговые цифры, графики (позже)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def build_report(df, rf):
    df['CAGR_5'] = cagr(spread=df['Spread'])

    bins = [-np.inf, 0, 0.19, 0.49, 0.99, np.inf]
    labels = ["Убыток", "0-19%", "20-49%", "50-99%", "100% +"]
    df['Category'] = pd.cut(df['CAGR_5'], bins=bins, labels=labels)

    sharpe_ratio =  calc_sharpe(returns=df['CAGR_5'], rf=rf)

    prob_of_profit = calc_win_rate(cargs=df['CAGR_5'])
    return df, dict(Sharpe=sharpe_ratio, AVG_Cagr=df['CAGR_5'].mean(), Win_Rate = prob_of_profit)


def cagr(spread):
    cagr = (1 + spread)**(1/5) - 1
    return cagr


def calc_win_rate(cargs):
    prob_of_profit = (cargs > 0).mean()
    return prob_of_profit


def calc_sharpe(returns, rf):
    sharpe_ratio = (returns.mean() - rf) / returns.std()
    return sharpe_ratio


def show_charts(df):
    counts = df['Category'].value_counts()
    plt.pie(counts.values, labels=counts.index)
    plt.show()