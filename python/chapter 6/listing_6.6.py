import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def manage_datetime(df):
    """Convert the column to a datetime object (if not already in datetime format)
    Args:
        df (dataframe): dataset 
    Returns:
        dataframe: dataset with the column datetime converted
    """
    df['datetime'] = pd.to_datetime(df['datetime'])
    # Extract the hour from the datetime column
    df['hour'] = df['datetime'].dt.hour
    df = df.drop(columns=['datetime'])
    return df

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "bikerental/rental_train.csv", encoding='UTF8')

    thres = 10 
    cols_categ = [col for col in df.columns if df[col].nunique() < thres and df[col].dtype == 'object']
    cols_non_categ = [col for col in df.columns if df[col].nunique() >= thres and df[col].dtype == 'object' or df[col].dtype != 'object']
    df_train_non_categ = df[ cols_non_categ ]
    df_train_non_categ = manage_datetime(df_train_non_categ) # We need to convert the column to a datetime object (if not already in datetime format)
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

    # Scaling data
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(df_final)
    # Convert the scaled array back to a DataFrame with the same column names
    df_scaled = pd.DataFrame(scaled_array, columns=df_final.columns, index=df_final.index)
    
    # Display the scaled DataFrame
    print (df_scaled.head())

