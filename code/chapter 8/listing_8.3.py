# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C
import pandas as pd

def collect_metadata(chunk):
    """
    Collects basic metadata from a given data chunk.
    This function extracts key statistics and metadata from a chunk of data, including column names, counts of missing values, means, medians, 
    and modes of the columns. It is useful for summarizing and understanding the basic characteristics of a dataset.
    Parameters:
        chunk (DataFrame): A pandas DataFrame chunk to collect metadata from.
    Returns:
        dict: A dictionary containing the following metadata:
            - 'columns': List of column names.
            - 'missing_counts': Dictionary with the count of missing values per column.
            - 'column_means': Dictionary with the mean of each column.
            - 'column_medians': Dictionary with the median of each column.
            - 'column_modes': Dictionary with the mode (most frequent value) of each column.
    """
    metadata = {
        "columns": chunk.columns.tolist(),
        "missing_counts": chunk.isna().sum().to_dict(),
        "column_means": chunk.mean(numeric_only=True).to_dict(),
        "column_medians": chunk.median(numeric_only=True).to_dict(),
        "column_modes": chunk.mode(dropna=True).iloc[0].to_dict()
    }
    return metadata

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Collect metadata
    print(collect_metadata(chunks[0]))