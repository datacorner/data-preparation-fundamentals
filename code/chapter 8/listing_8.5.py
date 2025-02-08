# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import get_gemini_response, clean_gemini_response, DATASET_FOLDER

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

def build_prompt(chunk, metadata):
    """
    Generates a formatted prompt string based on the provided task and details.
    Parameters:
        chunk (str): chunk data
        metadata (list): Additional details (metadata) for building out the prompt
    Returns:
        str: A formatted prompt string combining the task and details, ready for use.
    """
    prompt = f"""
                You are a data expert helping to clean a dataset. The dataset is structured as follows:
                Columns: {metadata['columns']}
                Metadata about the columns:
                - Missing value counts: {metadata['missing_counts']}
                - Column means: {metadata['column_means']}
                - Column medians: {metadata['column_medians']}
                - Column modes: {metadata['column_modes']}

                Here is the dataset with missing values (NaN):
                {chunk.to_string(index=False)}

                Your task:
                1. Identify columns with missing values.
                2. Impute missing values using the most appropriate statistical method based on metadata (e.g., mean, median, or mode).
                3. Return the updated data for the dataset provided in a JSON format (each row as a node) without any prefix or decoration. 
                I should be able to leverage the response directly by using a programming language (like python), by just importing the result as is.
                Please only provide the result of task 3
                """
    return prompt

if __name__ == "__main__":
    df = pd.read_csv(DATASET_FOLDER + "titanic/train.csv")
    # Collect metadata for all the dataset
    metadata = collect_metadata(df)
    # Chunks the dataset
    chunk_size = 10
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

    # Let's focus only on the first chunk
    prompt = build_prompt(chunks[0], metadata)
    
    # Send the prompt
    print(f"Prompt {prompt}")
    response = clean_gemini_response(get_gemini_response(prompt))
    
    # Let's focus on passenger 6 and his age before updating (NaN)
    print(f"BEFORE -> Passenger 6 Age (Moran, Mr. James): {chunks[0][chunks[0]["PassengerId"] == 6]["Age"]}")
    # Now let's see how the passenger 6 age has been updated
    new_df = pd.DataFrame(response)
    print(f"AFTER  -> Passenger 6 Age (Moran, Mr. James): {new_df[new_df["PassengerId"] == 6]["Age"]}")