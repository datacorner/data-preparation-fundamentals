import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "bikerental/rental_train.csv", encoding='UTF8')
    cols_categ = ['season', 'workingday', 'weather']
    thres = 10  # Par exemple, les colonnes avec moins de 10 valeurs uniques sont considérées comme catégorielles
    cols_categ = [col for col in df.columns if df[col].nunique() < thres and df[col].dtype == 'object']
    cols_non_categ = [col for col in df.columns if df[col].nunique() >= thres and df[col].dtype == 'object' or df[col].dtype != 'object']
    df_train_non_categ = df[ cols_non_categ ]
    df_train_categ = df[ cols_categ ]

    encoder = OneHotEncoder(sparse_output=False)
    # Fit and transform the data
    onehot_encoded = encoder.fit_transform(df_train_categ[cols_categ])
    # Get feature names (optional)
    feature_names = encoder.get_feature_names_out(cols_categ)
    # Convert the result to a DataFrame for better readability
    df_onehot_encoded = pd.DataFrame(onehot_encoded, columns=feature_names)
    # Concatenate the encoded DataFrame with the remaining non-categorical columns:
    df_final = pd.concat([df_train_non_categ, df_onehot_encoded], axis=1)
    
    print (df_final.head())

