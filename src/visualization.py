import pandas as pd
import matplotlib.pyplot as plt
from clustering import load_data, run_clustering, label_data


def visualize_clusters(data):
    plt.figure(figsize=(10, 10))
    plt.scatter(
        data['Annual Income (k$)'],
        data['Spending Score (1-100)'],
        c=data['Cluster'],
        cmap='coolwarm'
    )
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Customer Segments')
    plt.show()


if __name__ == "__main__":
    raw_data = pd.read_csv("data/Customer shopping data.csv")
    data = raw_data.drop(['CustomerID', 'Genre', 'Age'], axis=1)
    labels = run_clustering(data)
    labeled_data = label_data(data, labels)
    visualize_clusters(labeled_data)
