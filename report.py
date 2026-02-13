# группировки по диапазонам, итоговые цифры, графики (позже)
import matplotlib.pyplot as plt

def get_category(cagr):
    if cagr < 0:
        return "Убыток"
    elif cagr <= 0.19:
        return "0-19%"
    elif cagr <= 0.49:
        return "20-49%"
    elif cagr <= 0.99:
        return "50-99%"
    else:
        return "100% +"

def build_report(df):
    df['CAGR_5'] = (1 + df['Profit'])**(1/5) - 1
    df['Category'] = df['CAGR_5'].apply(get_category) 
    print(df['Category'].value_counts())
    return df

def show_charts(df):
    counts = df['Category'].value_counts()
    plt.pie(counts.values, labels=counts.index)
    plt.show()