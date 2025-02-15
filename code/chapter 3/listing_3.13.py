import pandas as pd
from sklearn.covariance import EllipticEnvelope

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    distrib = df['Age'].dropna()

    # Using the mahalanobis test on ages
    X = distrib.values.reshape(-1, 1) #A
    outlier_detector = EllipticEnvelope(contamination=0.1, 
                                        random_state=42) #B
    outlier_labels = outlier_detector.fit_predict(X)
    mahalanobis_outliers = distrib[outlier_labels == -1] #C
    
    print("Number of outliers", len(mahalanobis_outliers))
    print(', '.join(map(str, mahalanobis_outliers.values)))
