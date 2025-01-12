import pandas as pd
import re 

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

def name_to_word_pattern(name):
    name_without_parentheses = re.sub(r'\([^)]*\)', '', name).strip() #A
    words = re.findall(r'\b\w+\b|\.|,', name_without_parentheses)
    pattern = []
    for word in words:
        if word in [',', '.']:
            pattern.append(word)
        elif word.lower() in ['mr', 'mrs', 'miss', 
                              'master', 'dr', 'rev', 
                              'col', 'major', 'capt']:
            pattern.append('TITLE')
        elif word.lower() in ['van', 'de', 'der', 'du', 
                              'di', 'la', 'le']:
            pattern.append('PREFIX')
        else:
            if not pattern or pattern[-1] != 'NAME':
                pattern.append('NAME')
    return ' '.join(pattern)

if __name__ == "__main__":
    df = initialize()
    df['NamePattern'] = df['Name'].apply(name_to_word_pattern)
    print(df['NamePattern'].value_counts())