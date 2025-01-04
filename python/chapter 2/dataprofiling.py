import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

def initialize():
    # read the CSV file
    df = pd.read_csv("../Titanic disaster/train.csv")
    # survived=0 means the passenger died, survived=1 means he survived, let's make it more clear in the dataset:
    df['SurvivedProba'] = df['Survived']
    df['SurvivedLabel'] = df['Survived'].map({1: 'alive' , 0: 'dead'})
    return df

def firstlook(_df):
    print(_df.head())
    print(_df.info())
    print(_df.describe())
    
def eda(_df):
    # Generate the profile report
    profile = ProfileReport(_df, title="Titanic Dataset Profiling Report")
    # Build the report
    profile.to_file("titanic_report.html")
    
if __name__ == "__main__":
    df = initialize()
    firstlook(df)
    eda(df)
