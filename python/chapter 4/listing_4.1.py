import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: dataset read
    """
    # read the CSV file
    df_csv = pd.read_csv(C.DATASET_FOLDER + 'vgames/games_about.csv', delimiter=",")
    return df_csv

if __name__ == "__main__":
    df_csv = initialize()
    print(df_csv.head())