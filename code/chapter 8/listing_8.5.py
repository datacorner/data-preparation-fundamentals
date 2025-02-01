# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import get_gemini_response, clean_gemini_response, DATASET_FOLDER
import pandas as pd
import json

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

def build_normalization_prompt(chunk, metadata):
    """
    Generates a formatted prompt string based on the provided task and details.
    Parameters:
        chunk (str): chunk data
        metadata (list): Additional details (metadata) for building out the prompt
    Returns:
        str: A formatted prompt string combining the task and details, ready for use.
    """
    prompt = f"""
                You are a data expert helping to clean a dataset by performing noise reduction and normalization. The dataset is structured as follows:
                Columns: {metadata['columns']}
                Metadata about the columns:
                - Missing value counts: {metadata['missing_counts']}
                - Column means: {metadata['column_means']}
                - Column medians: {metadata['column_medians']}
                - Column modes: {metadata['column_modes']}

                Here is the dataset (including some noisy values or outliers) for analysis:
                {chunk.to_string(index=False)}

                ### Your task:
                1. **Noise Reduction**:
                - Identify any columns that have noisy data (e.g., outliers, spikes, extreme values).
                - Apply an appropriate technique to reduce noise, such as:
                    - Using a rolling average or median for smoothing.
                    - Identifying and handling outliers (e.g., via z-scores or IQR).
                    - Handling missing values (e.g., forward filling or imputation with statistical values).

                2. **Normalization**:
                - Normalize numerical features to ensure they are on a similar scale. You can apply one or more of the following methods:
                    - **Min-Max Scaling**: Scale values between 0 and 1.
                    - **Standardization (Z-Score Normalization)**: Adjust the dataset to have a mean of 0 and a standard deviation of 1.
                    - **Robust Scaling**: Normalize using median and IQR to handle outliers.

                3. Return the updated data for the dataset provided in a JSON format (each row as a node) without any prefix or decoration. 
                I should be able to leverage the response directly by using a programming language (like python), by just importing the result as is.
                Please only provide the result of task 3
                """
    return prompt

if __name__ == "__main__":
    df = pd.read_csv(DATASET_FOLDER + "titanic/train.csv")
    # Only get the first 10 rows
    chunk0 = df.head(10)
    # Get metadata from the whole dataset
    metadata = collect_metadata(df)
    # Build the prompt
    prompt = build_normalization_prompt(chunk0, metadata)
    # Send the prompt to the LLM and gets the response back
    response = clean_gemini_response(get_gemini_response(prompt))
    new_df = pd.DataFrame(json.loads(response))
    print(f"Prompt {prompt}")
    print(f"Response for Chunk {0}:\n{response}\n")