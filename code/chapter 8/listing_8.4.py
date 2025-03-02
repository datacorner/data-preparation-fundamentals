import pandas as pd

def collect_metadata(data):
    """
    Collects basic metadata from a given dataset.
    This function extracts key statistics and metadata from a dataset, including column names, counts of missing values, means, medians, 
    and modes of the columns. It is useful for summarizing and understanding the basic characteristics of a dataset.
    Parameters:
        data (DataFrame): A pandas DataFrame chunk to collect metadata from.
    Returns:
        dict: A dictionary containing the following metadata:
            - 'columns': List of column names.
            - 'missing_counts': Dictionary with the count of missing values per column.
            - 'column_means': Dictionary with the mean of each column.
            - 'column_medians': Dictionary with the median of each column.
            - 'column_modes': Dictionary with the mode (most frequent value) of each column.
    """
    metadata = {
        "columns": data.columns.tolist(),
        "missing_counts": data.isna().sum().to_dict(),
        "column_means": data.mean(numeric_only=True).to_dict(),
        "column_medians": data.median(numeric_only=True).to_dict(),
        "column_modes": data.mode(dropna=True).iloc[0].to_dict()
    }
    return metadata

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Collect metadata
    print(collect_metadata(chunks[0]))