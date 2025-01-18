import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "bikerental/rental_train.csv", encoding='UTF8')
    thres = 10  # Par exemple, les colonnes avec moins de 10 valeurs uniques sont considérées comme catégorielles
    cols_categ = [col for col in df.columns if df[col].nunique() < thres and df[col].dtype == 'object']
    cols_non_categ = [col for col in df.columns if df[col].nunique() >= thres and df[col].dtype == 'object' or df[col].dtype != 'object']
    print("Categorical columns :", cols_categ)
    print("Non Categorical columns (Objects only):", cols_non_categ)

