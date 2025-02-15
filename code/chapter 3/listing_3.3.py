import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Dropping column instead of rows (column-wide deletion)
    missing_percentage = df.isnull().sum() / len(df) * 100
    columns_to_drop = missing_percentage[missing_percentage > 50].index #A
    titanic_reduced = df.drop(columns=columns_to_drop) #B
    print ("columns dropped:", columns_to_drop)

