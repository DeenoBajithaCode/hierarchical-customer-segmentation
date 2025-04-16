import pandas as pd
from sklearn.cluster import AgglomerativeClustering


def load_data(filepath):
    df = pd.read_csv(filepath)
    return df.drop(['CustomerID', 'Genre', 'Age'], axis=1)


def run_clustering(data, n_clusters=5):
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    labels = model.fit_predict(data)
    return labels


def label_data(data, labels):
    data = data.copy()
    data['Cluster'] = labels
    return data


if __name__ == "__main__":
    data = load_data("data/Customer shopping data.csv")
    labels = run_clustering(data)
    labeled_data = label_data(data, labels)
    print(labeled_data.head())
