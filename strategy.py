# формулы стратегии (mean10, mean8worst, D, сравнение с акциями)

def calculate_dispersion(price_dataframe):
    return_list = (price_dataframe.iloc[-1] / price_dataframe.iloc[0]) - 1
    worst_8_returns = sorted(return_list)[0:8]
    mean_best_10 = sum(return_list)/len(return_list)
    mean_worst_8 = sum(worst_8_returns)/len(worst_8_returns)
    res = mean_best_10 - mean_worst_8
    return res