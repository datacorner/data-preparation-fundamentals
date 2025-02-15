import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Imputing by using Forward and backforward techniques
    print("Original 'Age' column with missing values:\n", df['Age']) #A
    df['age_ffill'] = df['Age'].fillna(method='ffill') #B
    df['age_bfill'] = df['Age'].fillna(method='bfill') #C
    print (df[df["PassengerId"] == 889])