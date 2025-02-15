import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Using linear interpolation to impute values (MICE)
    imputer = IterativeImputer()
    # Selecting relevant columns for imputation
    # It's a good practice to include other numeric columns for a better imputation
    columns_for_imputation = ['Age', 'SibSp', 'Parch', 'Fare']
    df_subset = df[columns_for_imputation]
    # Perform imputation
    df_imputed = imputer.fit_transform(df_subset)
    # Replace the original columns with imputed values
    df[columns_for_imputation] = df_imputed
    print (df[df["PassengerId"] == 889])