import pandas as pd
from sklearn.impute import KNNImputer

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Create a KNNImputer instance with n_neighbors set to 3
    imputer = KNNImputer(n_neighbors=3)
    # Impute missing values in the 'Age' column
    df['Age'] = imputer.fit_transform(df[['Age']])
    print (df[df["PassengerId"] == 889])