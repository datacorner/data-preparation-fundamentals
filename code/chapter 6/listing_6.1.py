import pandas as pd

def display_missing_values(df):
    """
    Displays the percentage of missing values for each column in a DataFrame and prints the shape of the DataFrame.
    Parameters:
        df (pandas.DataFrame): The DataFrame to analyze for missing values.
    Returns:
        None: This function prints the missing value percentages and DataFrame shape.
    """
    missing_percentage = df.isnull().sum() / len(df) * 100
    print("% of Missing values per column:")
    print(missing_percentage.apply(lambda x: f"{x:.1f} %"))
    print("Rows: {} | Columns: {}".format(df.shape[0], df.shape[1]))

if __name__ == "__main__":
    df = pd.read_csv("../data/bikerental/rental_train.csv", encoding='UTF8')
    display_missing_values(df)
