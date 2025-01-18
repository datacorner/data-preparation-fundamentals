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

def iqr_method(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    print(f"IQR={IQR}")
    lower_bound = Q1 - 1.5 * IQR
    print(f"lower_bound={lower_bound}")
    upper_bound = Q3 + 1.5 * IQR
    print(f"upper_bound={upper_bound}")
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers

if __name__ == "__main__":
    df = initialize()
    distrib = df['Age'].dropna()
    
    # Create the box plot to visualize the Age repartition
    plt.figure(figsize=(10, 6))
    distrib.plot(kind='box')
    plt.title('Age Distribution in the Dataset')
    plt.ylabel('Age distribution')
    plt.xlabel('Age')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7) # Add grid for better readability
    # Show the plot
    plt.show()
    
    # IQR method
    iqr_outliers = iqr_method(distrib)
    print("Number of outliers", len(iqr_outliers))
    print(', '.join(map(str, iqr_outliers.values)))