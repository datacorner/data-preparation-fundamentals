import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

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

def parse_name(name):
    """ This function parses a name string into its components, extracting the 
        individual names, any title (e.g., Mr., Dr.), and any prefix 
        (e.g., van, de). The function is designed to handle names with punctuation 
        and parentheses gracefully, removing irrelevant elements before processing.
    Parameters:
        name (str): The input name string to parse. It may include titles, prefixes, 
                    parentheses, and punctuation.
    Returns:
        dict: A dictionary containing the parsed components:
            - 'names' (list): A list of individual name components (excluding titles and prefixes).
            - 'prefix' (str or None): The identified prefix (if any).
            - 'title' (str or None): The identified title (if any).
    """
    name_without_parentheses = re.sub(r'\([^)]*\)', '', name).strip() #A
    words = re.findall(r'\b\w+\b|\.|,', name_without_parentheses) #B
    names = []
    prefix = None
    title = None
    for word in words:
        if word.lower() in ['mr', 'mrs', 'miss', 
                            'master', 'dr', 'rev', 
                            'col', 'major', 'capt']:
            title = word
        elif word.lower() in ['van', 'de', 'der', 'du', 'di', 'la', 'le']:
            prefix = word
        elif word not in [',', '.']:
            names.append(word)

    return {
        'names': names,
        'prefix': prefix,
        'title': title
    }

def categorize_title(title):
    """ This function categorizes a given title into predefined groups based on its 
        social or professional context. Titles are grouped as 'Common', 'Rich', or 
        'Professional', while unrecognized titles are assigned a NaN value.
    Parameters:
        title (str): The input title to categorize (e.g., 'Mr', 'Dr', 'Lady').
    Returns:
        str or np.nan: The category of the title:
            - 'Common' for widely used social titles (e.g., 'Mr', 'Miss').
            - 'Rich' for titles typically associated with wealth or nobility 
            (e.g., 'Don', 'Lady').
            - 'Professional' for titles related to professions or ranks 
            (e.g., 'Dr', 'Major').
            - np.nan if the title does not match any predefined categories.
    """
    if title in ['Mr', 'Mrs', 'Ms', 'Miss', 'Mme', 'Mlle']:
        return 'Common'
    elif title in ['Master', 'Don', 'Lady', 'Sir', 'Jonkheer', 'Dona']:
        return 'Rich'
    elif title in ['Rev', 'Dr', 'Major', 'Col', 'Capt']:
        return 'Professional'
    else:
        return np.nan

def plotByGroupAndRate(df, col):
    """ This function visualizes the relationship between a categorical feature (group)
        and survival outcomes in a dataset. It generates two side-by-side plots:
        1. A count plot showing the distribution of survivors and non-survivors by group.
        2. A bar plot showing the average survival rate by group.
    Parameters:
        df (pd.DataFrame): The input dataset containing the survival data.
            Required columns:
                - 'Survived': Binary column indicating survival status (0 = did not survive, 1 = survived).
                - 'SurvivedProba': Column with probabilities or mean survival rates for each group.
        col (str): The name of the categorical column used for grouping (e.g., titles, age groups).
    Returns:
        None: The function displays the plots directly.
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    sns.countplot(x=col, hue="Survived", 
                data=df[df["Survived"].notnull()], 
                ax=axs[0], 
                palette="Greys")
    axs[0].set_title("Survival by Group")
    axs[0].set_xlabel("Group")
    axs[0].set_ylabel("Count")

    survival_rates = df.groupby(col)['SurvivedProba'].mean()
    sns.barplot(x=survival_rates.index, y=survival_rates.values, ax=axs[1], palette="Greys")
    axs[1].set_title('Survival Rate by Group')
    axs[1].set_xlabel('Title Group')
    axs[1].set_ylabel('Survival Rate')
    axs[1].set_ylim(0, 1)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = initialize()
    df['NameComponents'] = df['Name'].apply(parse_name) #C
    df['NameList'] = df['NameComponents'].apply(lambda x: x['names'])
    df['Prefix'] = df['NameComponents'].apply(lambda x: x['prefix'])
    df['Title'] = df['NameComponents'].apply(lambda x: x['title'])
    df = df.drop('NameComponents', axis=1)
    df['TitleGroup'] = df['Title'].apply(categorize_title)
    plotByGroupAndRate(df, "TitleGroup")