import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    missing_percentage = df.isnull().sum() / len(df) * 100
    print(missing_percentage.apply(lambda x: f"{x:.1f}"))
