import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def display_missing_values(df):
    missing_percentage = df.isnull().sum() / len(df) * 100
    print("% of Missing values per column:")
    print(missing_percentage.apply(lambda x: f"{x:.1f} %"))
    print("Rows: {} | Columns: {}".format(df.shape[0], df.shape[1]))

if __name__ == "__main__":
    df_train = pd.read_csv("../data/bikerental/rental_train.csv", 
                            encoding='UTF8')
    df_test = pd.read_csv("../data/bikerental/rental_test.csv", 
                            encoding='UTF8')
    display_missing_values(df_test)
    
    cols_categ = ['season', 'workingday', 'weather']
    thres = 10 
    cols_categ = [col for col in df_train.columns if 
                    df_train[col].nunique() < thres and 
                    df_train[col].dtype == 'object']
    cols_non_categ = [col for col in df_train.columns if 
                    df_train[col].nunique() >= thres and 
                    df_train[col].dtype == 'object' or 
                    df_train[col].dtype != 'object']
    df_train_non_categ = df_train[ cols_non_categ ]
    df_train_categ = df_train[ cols_categ ]
    
    # Preprocess test data: Replace infrequent or unseen categories with "Unknown"
    for col in cols_categ:
        df_test[col] = df_test[col].fillna("Unknown")
        df_test[col] = df_test[col].where(df_test[col].isin(df_train[col].unique()), "Unknown")
    print (f"Weather Values with frequency: {df_test["weather"].value_counts()}")

    # Convert any unseen values during encoding to "Unknown"
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    # Fit and transform the data for training & test
    onehot_encoded_train = encoder.fit_transform(df_train[cols_categ])
    onehot_encoded_test = encoder.transform(df_test[cols_categ])
    # Get feature names, including "Unknown"
    
    feature_names = encoder.get_feature_names_out(cols_categ)
    # Convert the result to a DataFrame for better readability
    df_onehot_encoded_train = pd.DataFrame(onehot_encoded_train, columns=feature_names)
    df_onehot_encoded_test = pd.DataFrame(onehot_encoded_test, columns=feature_names)
    
    print (f"Test feature set: {df_onehot_encoded_test.head()}")
