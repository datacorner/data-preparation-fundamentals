import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/bikerental/rental_train.csv", encoding='UTF8')
    cols_non_numeric = df.select_dtypes(exclude=['number']).columns
    print(f"Not numeric columns : {cols_non_numeric}")

