# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C
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

def build_anomaly_outlier_prompt(chunk, metadata):
    """
    Generates a formatted prompt string based on the provided task and details.
    Parameters:
        chunk (str): chunk data
        metadata (list): Additional details (metadata) for building out the prompt
    Returns:
        str: A formatted prompt string combining the task and details, ready for use.
    """
    prompt = f"""
            You are a data expert helping to clean a dataset by detecting and treating anomalies and outliers. The dataset is structured as follows:
            Columns: {metadata['columns']}
            Metadata about the columns:
            - Missing value counts: {metadata['missing_counts']}
            - Column means: {metadata['column_means']}
            - Column medians: {metadata['column_medians']}
            - Column modes: {metadata['column_modes']}

            Here is the dataset, including potential anomalies or outliers:
            {chunk.head(5).to_string(index=False)}

            ### Your task:
            1. **Anomaly Detection**:
            - Identify any anomalies or outliers in the dataset. These may include:
                - Extreme values (e.g., values significantly larger or smaller than the rest).
                - Unexpected patterns in the data (e.g., missing values in key columns or unusual distributions).
                - Use techniques like z-scores, IQR (Interquartile Range), or visual inspection of statistical distributions to detect these anomalies.

            2. **Outlier Treatment**:
            - For each identified outlier or anomaly:
                - Determine if the value should be capped or transformed (e.g., winsorizing or log transformation).
                - Decide if the anomaly should be removed or replaced with a more plausible value (e.g., using the median or mean).
                - Ensure the final dataset is clean and consistent.

            Please provide the cleaned and updated values after applying these treatments.
            """
    return prompt

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Get metadata
    metadata = collect_metadata(chunks[0])
    prompt = build_anomaly_outlier_prompt(chunks[0], metadata)
        
    response = C.get_gemini_response(prompt)
    print(f"Prompt {prompt}")
    print(f"Response for Chunk {0}:\n{response}\n")