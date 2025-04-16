import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc


def load_data(filepath):
    return pd.read_csv(filepath)


def prepare_data(df):
    return df.drop(['CustomerID', 'Genre', 'Age'], axis=1)


def plot_dendrogram(data, save_path="dendrogram_plot.png"):
    plt.figure(figsize=(10, 10))
    plt.title("Customer Dendrogram")
    dendrogram = shc.dendrogram(shc.linkage(data, method='ward'))
    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    df = load_data("data/Customer shopping data.csv")
    clean_data = prepare_data(df)
    plot_dendrogram(clean_data)
