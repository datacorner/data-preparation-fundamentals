import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def manage_datetime(df):
    """
    Converts the 'datetime' column in the DataFrame to a datetime object and extracts the hour.
    Parameters:
        df (pandas.DataFrame): The input DataFrame containing a 'datetime' column.
    Returns:
        pandas.DataFrame: The DataFrame with 'datetime' converted and an additional 'hour' column.
    """
    df['datetime'] = pd.to_datetime(df['datetime'])
    # Extract the hour from the datetime column
    df['hour'] = df['datetime'].dt.hour
    return df.drop(columns=['datetime'])

def onehot(df):
    """ Apply the one hot encoding technique to a dataset
    Args:
        df (dataframe): initial dataset
    Returns:
        dataframe: encoded dataset
    """
    thres = 10 
    cols_categ = [col for col in df.columns if df[col].nunique() < thres and df[col].dtype == 'object']
    cols_non_categ = [col for col in df.columns if df[col].nunique() >= thres and df[col].dtype == 'object' or df[col].dtype != 'object']
    df_train_non_categ = df[ cols_non_categ ]
    df_train_non_categ = manage_datetime(df_train_non_categ) 
    df_train_categ = df[ cols_categ ]

    encoder = OneHotEncoder(sparse_output=False) #A
    onehot_encoded = encoder.fit_transform(df_train_categ[cols_categ])
    feature_names = encoder.get_feature_names_out(cols_categ) #B
    df_onehot_encoded = pd.DataFrame(onehot_encoded, columns=feature_names) #C
    return pd.concat([df_train_non_categ, df_onehot_encoded], axis=1) #D

if __name__ == "__main__":
    df = pd.read_csv("../data/bikerental/rental_train.csv", encoding='UTF8')
    df_oh = onehot(df)
    print (df_oh.head())

