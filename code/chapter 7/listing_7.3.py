import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def handle_slowly_changing_dimension(df):
    """ SCD Type 2 implementation
    Args:
        df (pandas.DataFrame): input dataset
    Returns:
        pandas.DataFrame: output dataset
    """
    # Make a copy to avoid modifying the original DataFrame
    working_df = df.copy()
    # Add timestamp
    working_df['Change_Timestamp'] = pd.Timestamp.now()
    # Create a temporary ID to ensure we maintain row order
    working_df['temp_order'] = range(len(working_df))
    # Sort and deduplicate first, then group
    result = (
        working_df
        .sort_values(['Customer ID', 'Change_Timestamp', 'temp_order'])
        .drop_duplicates(['Customer ID', 'Segment'], keep='last')
        .drop('temp_order', axis=1)
    )
    return result

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')
    df_scd = handle_slowly_changing_dimension(df)
    print(df_scd.shape)