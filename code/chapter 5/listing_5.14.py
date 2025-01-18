import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "/titanic/train.csv")

    features = ['Pclass', 'Age', 'Fare'] #A
    X = df[features].copy()

    imputer = SimpleImputer(strategy='mean') #B
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    scaler = StandardScaler() #C
    X_scaled = scaler.fit_transform(X)
    inertias = []
    k_range = range(1, 11)

    # Choose number of clusters (let's say 3 for this example)
    n_clusters = 3

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Analyze the clusters
    cluster_summary = df.groupby('Cluster').agg({
        'Survived': 'mean',
        'Pclass': 'mean',
        'Age': 'mean',
        'Fare': 'mean',
        'Sex': lambda x: x.value_counts().index[0]  # most common sex
    }).round(2)

    print("Cluster Summary:")
    print(cluster_summary)

    # Visualizing the clusters 
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    scatter = plt.scatter(X['Age'], X['Fare'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Clusters by Age and Fare')
    plt.colorbar(scatter)
    plt.subplot(1, 2, 2)
    scatter = plt.scatter(X['Pclass'], X['Fare'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('Pclass')
    plt.ylabel('Fare')
    plt.title('Clusters by Pclass and Fare')
    plt.colorbar(scatter)
    plt.tight_layout()
    plt.show()
