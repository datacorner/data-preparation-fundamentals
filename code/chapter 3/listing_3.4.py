import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    missing_percentage = df.isnull().sum() / len(df) * 100
    columns_to_drop = missing_percentage[missing_percentage > 50].index #A
    titanic_reduced = df.drop(columns=columns_to_drop) 

    # Combining row and column dropping together
    titanic_final = titanic_reduced.dropna() 
    print("Final number of rows:", len(titanic_final))
    print("Final number of columns:", len(titanic_final.columns))