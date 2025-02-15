import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Using linear interpolation to impute values
    df['Age'].interpolate(method='linear', inplace=True)
    print (df[df["PassengerId"] == 889])