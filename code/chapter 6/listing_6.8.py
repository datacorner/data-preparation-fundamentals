import pandas as pd

if __name__ == "__main__":
    df_train = pd.read_csv("../data/bikerental/rental_train.csv", encoding='UTF8')

    # Define the bin edges and labels
    bins = [0, 15, 30, 50]  # Example bin edges for 'Cold', 'Moderate', 'Hot'
    labels = ['Cold', 'Moderate', 'Hot']

    # Apply discretization to the 'temp' column
    df_train['temp_binned'] = pd.cut(df_train['temp'], bins=bins, labels=labels, right=True)

    # Show the resulting dataframe
    print(df_train.head())