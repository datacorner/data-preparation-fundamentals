import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "bikerental/rental_train.csv", encoding='UTF8')
    cols_non_numeric = df.select_dtypes(exclude=['number']).columns
    print("Not numeric columns :", cols_non_numeric)

