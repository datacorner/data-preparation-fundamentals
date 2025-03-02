import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    print (chunks)