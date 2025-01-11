import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: titanic dataset
    """
    # read the CSV file
    df = pd.read_csv("../Titanic disaster/train.csv")
    # survived=0 means the passenger died, survived=1 means he survived, let's make it more clear in the dataset:
    df['SurvivedProba'] = df['Survived']
    df['SurvivedLabel'] = df['Survived'].map({1: 'alive' , 0: 'dead'})
    return df

def analyzeSurvivalRateByGenderAge(titanic_data):
    """Analyze the Survival Rates by Gender and Age

    Args:
        _df (dataframe): titanic dataset
    """
    # Define age bins and labels
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    age_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']

    # Create a new 'AgeGroup' column based on the bins
    titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_bins, labels=age_labels, right=False)
    # Group by 'Sex', 'AgeGroup', and 'Survived', then count the number of occurrences
    survival_by_gender_age = titanic_data.groupby(['Sex', 'AgeGroup', 'Survived']).size().unstack(fill_value=0)
    # Calculate survival rates by dividing the number of survivors by the total number of passengers in each group
    survival_by_gender_age['SurvivalRate'] = survival_by_gender_age[1] / (survival_by_gender_age[0] + survival_by_gender_age[1])
    # Separate data for male and female
    male_survival = survival_by_gender_age.loc['male']['SurvivalRate']
    female_survival = survival_by_gender_age.loc['female']['SurvivalRate']

    # Plot the data
    plt.figure(figsize=(10, 6))
    # Bar width
    bar_width = 0.35
    # X-axis positions for male and female bars
    x = np.arange(len(age_labels))
    # Plot male survival rates
    plt.bar(x - bar_width / 2, male_survival, width=bar_width, color='blue', label='Male')
    # Plot female survival rates
    plt.bar(x + bar_width / 2, female_survival, width=bar_width, color='pink', label='Female')
    # Set the title and labels
    plt.title('Survival Rates by Age and Gender on the Titanic')
    plt.xlabel('Age Group')
    plt.ylabel('Survival Rate')
    plt.xticks(x, age_labels)
    plt.ylim(0, 1)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    df = initialize()
    analyzeSurvivalRateByGenderAge(df)