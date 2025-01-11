import pandas as pd

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: dataset read
    """
    # read the CSV file
    df_csv = pd.read_csv('../vgames/games_about.csv', delimiter=",")
    return df_csv

if __name__ == "__main__":
    df_csv = initialize()
    print(df_csv.head())