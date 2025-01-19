import pandas as pd
from scipy import stats
import numpy as np

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

def zscore_method(data, threshold=3):
    """ Identifies potential outliers in a dataset using the z-score method.  
    Calculates the z-scores for each data point and returns the points that exceed a specified threshold.
    Parameters:
        data (pd.Series or np.ndarray): The dataset to analyze for outliers.
        threshold (float, optional): The z-score threshold for outlier detection. Defaults to 3.
    Returns:
        pd.Series or np.ndarray: A subset of the input data containing the detected outliers.
    """
    z_scores = np.abs(stats.zscore(data))
    outliers = data[z_scores > threshold]
    return outliers

if __name__ == "__main__":
    df = initialize()
    distrib = df['Age'].dropna()

    # Using the Z-Score method on ages
    zscore_outliers = zscore_method(distrib)
    
    print("Number of outliers", len(zscore_outliers))
    print(', '.join(map(str, zscore_outliers.values)))