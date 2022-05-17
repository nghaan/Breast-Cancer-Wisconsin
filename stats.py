import pandas as pd

def stats_columns(filename, attribute):
    df = pd.read_csv(filename, sep='\t')

    xdata = df[attribute].describe()
    return xdata
