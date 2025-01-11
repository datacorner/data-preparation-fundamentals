import pandas as pd
import json

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: dataset
    """
    # read the JSON file
    with open('../vgames/games_genres_valve.json', 'r',  encoding='utf-8-sig') as file:
        data = json.load(file) #A
        df_json = pd.DataFrame(data) 
    return df_json

if __name__ == "__main__":
    df_json = initialize()
    print(df_json.head())