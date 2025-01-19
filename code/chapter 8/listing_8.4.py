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
                3. Return the updated data for the dataset provided in a JSON format (each row as a node).
                Please only provide the result of task 3
                """
    return prompt

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Generate prompts for each chunk
    prompts = []
    for chunk in chunks:
        metadata = collect_metadata(chunk)
        prompt = build_prompt(chunk, metadata)
        prompts.append(prompt)
        
    response = C.get_gemini_response(prompt)
    print(f"Prompt {prompts[0]}")
    print(f"Response for Chunk {0}:\n{response}\n")