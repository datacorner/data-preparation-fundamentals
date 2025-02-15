import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Imputing with the age mean
    mean_age = df['Age'].mean()
    df['Age'].fillna(mean_age, inplace=True)
    print (df[df["PassengerId"] == 889])