import pandas as pd

def handle_slowly_changing_dimension(df):
    """ SCD Type 2 implementation
    Args:
        df (pandas.DataFrame): input dataset
    Returns:
        pandas.DataFrame: output dataset
    """
    # Make a copy to avoid modifying the original DataFrame
    working_df = df.copy() #A
    working_df['Change_Timestamp'] = pd.Timestamp.now() #B
    working_df['temp_order'] = range(len(working_df)) #C
    result = (
        working_df
        .sort_values(['Customer ID', 'Change_Timestamp', 'temp_order'])
        .drop_duplicates(['Customer ID', 'Segment'], keep='last')
        .drop('temp_order', axis=1)
    ) #D
    return result

if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')
    df_scd = handle_slowly_changing_dimension(df)
    print(df_scd.shape)