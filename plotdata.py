from attr import attr
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns


def plot_chart(filename, attributes):
    df = pd.read_csv(filename, sep='\t')
    sns.set(rc={'figure.figsize': (12, 6)})
    n = len(attributes)
    if n == 1:
        _, axs = plt.subplots(2)
        sns.boxplot(ax=axs[0], data=df, x=attributes[0])
        sns.histplot(ax=axs[1], data=df, x=attributes[0])
    elif n == 2:
        sns.regplot(x=attributes[0], y=attributes[1], data=df)
    elif n > 2:
        sns.pairplot(data=df[attributes])

    plt.savefig('plot', bbox_inches='tight')
    return

