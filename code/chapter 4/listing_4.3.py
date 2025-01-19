import pandas as pd
import json

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe
    Returns:
        dataframe: dataset
    """
    # read the JSON file
    with open(C.DATASET_FOLDER + 'vgames/games_genres_valve.json', 'r',  encoding='utf-8-sig') as file:
        data = json.load(file) #A
        df_json = pd.DataFrame(data) 
    return df_json

if __name__ == "__main__":
    df_json = initialize()
    print(df_json.head())