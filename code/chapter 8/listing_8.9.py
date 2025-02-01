# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C
import pandas as pd

def collect_metadata(data):
    """
    Collects comprehensive metadata from a given dataset.
    This function extracts detailed metadata from a dataset, including column names, data types, counts of missing values, 
    means, medians, modes, and summary statistics. It provides an overview of the dataset, useful for quick inspection and analysis.
    Parameters:
        data (DataFrame): A pandas DataFrame dataset to collect metadata from.
    Returns:
        dict: A dictionary containing the following metadata:
            - 'columns': List of column names.
            - 'data_types': Dictionary of column names and their respective data types.
            - 'missing_counts': Dictionary with the count of missing values per column.
            - 'column_means': Dictionary with the mean of each numeric column.
            - 'column_medians': Dictionary with the median of each numeric column.
            - 'column_modes': Dictionary with the mode (most frequent value) of each column.
            - 'summary_stats': Dictionary containing summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for each numeric column.
    """
    metadata = {
        "columns": data.columns.tolist(),
        "data_types": data.dtypes.to_dict(),
        "missing_counts": data.isna().sum().to_dict(),
        "column_means": data.mean(numeric_only=True).to_dict(),
        "column_medians": data.median(numeric_only=True).to_dict(),
        "column_modes": data.mode(dropna=True).iloc[0].to_dict(),
        "summary_stats": data.describe(include=[float, int]).to_dict()
    }
    return metadata

def generate_normalization_prompt(dataset_overview, target_columns=None, scaling_techniques=None):
    """
    Generates a prompt for normalizing and scaling a dataset for machine learning.
    This function creates a detailed prompt for an expert in data preprocessing and feature engineering, focusing on normalizing 
    and scaling numerical data. It provides context about the dataset and allows for customization of the columns to scale and the 
    specific scaling techniques to apply. The prompt outlines the steps required for analyzing the dataset, recommending scaling methods, 
    and addressing any preprocessing needs such as outliers or missing values.
    Parameters:
        dataset_overview (str): A brief description of the dataset, including its purpose and relevant features.
        target_columns (list, optional): A list of specific columns to focus on for normalization and scaling. Defaults to None, in which case all numeric columns are analyzed.
        scaling_techniques (list, optional): A list of preferred scaling techniques to suggest (e.g., min-max scaling, z-score normalization). Defaults to None, in which case the function recommends suitable methods based on the dataset's characteristics.
    Returns:
        str: A prompt to guide the normalization and scaling process, including recommendations for handling missing values, outliers, and the appropriate techniques to use for each column.
    """
    prompt = (
        "You are an expert in data preprocessing and feature engineering. I need your help in normalizing and scaling "
        "data from a dataset used for machine learning.\n\n"
        "Dataset Context:\n"
        f"{dataset_overview}\n\n"
    )

    if target_columns:
        prompt += (
            f"Focus specifically on the following columns for normalization and scaling: {', '.join(target_columns)}.\n"
        )
    else:
        prompt += "Analyze all numeric columns in the dataset for potential scaling.\n"

    if scaling_techniques:
        prompt += (
            f"Preferably suggest one or more of the following scaling techniques: {', '.join(scaling_techniques)}.\n"
        )
    else:
        prompt += (
            "Recommend suitable scaling methods such as min-max scaling, z-score normalization, or log transformations "
            "based on the data characteristics.\n"
        )

    prompt += (
        "Include the following in your response:\n"
        "- A summary of the dataset's scaling needs based on its metadata.\n"
        "- Specific scaling or normalization methods for each column and why you suggest them.\n"
        "- Any additional preprocessing steps needed to handle outliers or anomalies before scaling.\n\n"
        "If the dataset includes categorical columns or missing values, explain how to handle these issues.\n"
        "Provide a concise yet detailed explanation of your recommendations."
    )

    return prompt


if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    metadata = collect_metadata(chunks[0])
    print(metadata)
    
    # Example usage:
    dataset_overview = """
    The Titanic dataset includes the following columns:
    - PassengerId (integer): Unique identifier for each passenger.
    - Age (float): Passenger's age, with some missing values.
    - Fare (float): Ticket price paid by the passenger.
    - Embarked (categorical): Port of embarkation (C, Q, S).
    - Survived (binary): Target column indicating survival (0 or 1).
    """

    prompt = generate_normalization_prompt(dataset_overview, target_columns=["Age", "Fare"], scaling_techniques=["z-score"])
    print(prompt)
    
    response = C.get_gemini_response(prompt)
    print(f"Response for Chunk {0}:\n{response}\n")