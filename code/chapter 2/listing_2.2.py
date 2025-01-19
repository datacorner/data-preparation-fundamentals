import pandas as pd
import matplotlib.pyplot as plt

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

def analyzeBySex(_df):
    """Analyze the Titnaic dataset by sex
    Args:
        _df (dataframe): titanic dataset
    """
    print(_df["Sex"].value_counts())
    # Group by 'Sex' and 'Survived', then count the number of occurrences
    survival_counts = df.groupby(['Sex', 'Survived']).size().unstack()

    # Create a bar chart
    survival_counts.plot(kind='bar', stacked=False, color=['salmon', 'lightblue'], figsize=(6, 4))
    # Set the title and labels
    plt.title('Survival Counts by Sex on the Titanic')
    plt.xlabel('Sex')
    plt.ylabel('Number of Passengers')
    plt.xticks(rotation=0)
    plt.legend(['Did Not Survive', 'Survived'], title='Outcome')
    plt.show()

if __name__ == "__main__":
    df = initialize()
    analyzeBySex(df)
