import pandas as pd
from sklearn.covariance import EllipticEnvelope

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C


def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: titanic dataset
    """
    # read the CSV file
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # survived=0 means the passenger died, survived=1 means he survived, let's make it more clear in the dataset:
    df['SurvivedProba'] = df['Survived']
    df['SurvivedLabel'] = df['Survived'].map({1: 'alive' , 0: 'dead'})
    return df

def mahalanobis_method(data):
    X = data.values.reshape(-1, 1) #A
    outlier_detector = EllipticEnvelope(contamination=0.1, 
                                        random_state=42) #B
    outlier_labels = outlier_detector.fit_predict(X)
    outliers = data[outlier_labels == -1] #C
    return outliers

if __name__ == "__main__":
    df = initialize()
    distrib = df['Age'].dropna()

    # Using the mahalanobis test on ages
    mahalanobis_outliers = mahalanobis_method(distrib)
    print("Number of outliers", len(mahalanobis_outliers))
    print(', '.join(map(str, mahalanobis_outliers.values)))
