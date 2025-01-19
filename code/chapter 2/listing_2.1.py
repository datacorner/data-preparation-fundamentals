import pandas as pd
from ydata_profiling import ProfileReport

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

def firstlook(_df):
    """displays some Pandas basics stats about the dataset
    Args:
        _df (dataframe): dataset to analyze
    """
    print(_df.head())
    print(_df.info())
    print(_df.describe())
    
def eda(_df):
    """ Build out the YData-Profiling report (HTML)
    Args:
        _df (dataframe): dataset to analyze
    """
    # Generate the profile report
    profile = ProfileReport(_df, title="Titanic Dataset Profiling Report")
    # Build the report
    profile.to_file(C.PROFILE_FOLDER + "titanic_report.html")
    
if __name__ == "__main__":
    df = initialize()
    #firstlook(df)
    eda(df)
