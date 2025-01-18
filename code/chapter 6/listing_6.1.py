import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def display_missing_values(df):
    # Calculate the percentage of missing values in each column
    missing_percentage = df.isnull().sum() / len(df) * 100
    print("% of Missing values per column:")
    print(missing_percentage.apply(lambda x: f"{x:.1f} %"))
    print("Rows: {} | Columns: {}".format(df.shape[0], df.shape[1]))

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "bikerental/rental_train.csv", encoding='UTF8')
    display_missing_values(df)
