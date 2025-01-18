import pandas as pd
# It may be necessary to install the openpyxl library
# $ pip install openpyxl

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
    # read the Excel file
    df_excel = pd.read_excel(C.DATASET_FOLDER + 'vgames/games_reviews.xlsx')
    return df_excel

def categorize_rating(text):
    if 'Positive' in text:
        return 'Positive'
    elif 'Negative' in text:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    df_excel = initialize()
    df_excel['overall_player_rating'] = df_excel['overall_player_rating'].apply(categorize_rating) 
    print(df_excel.head())