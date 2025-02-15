import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    titanic_clean = df.dropna()
    print("Number of rows after listwise deletion:", len(titanic_clean))
