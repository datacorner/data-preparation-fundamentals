# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C
import pandas as pd

def collect_metadata(chunk):
    metadata = {
        "columns": chunk.columns.tolist(),
        "data_types": chunk.dtypes.to_dict(),
        "missing_counts": chunk.isna().sum().to_dict(),
        "column_means": chunk.mean(numeric_only=True).to_dict(),
        "column_medians": chunk.median(numeric_only=True).to_dict(),
        "column_modes": chunk.mode(dropna=True).iloc[0].to_dict(),
        "summary_stats": chunk.describe(include=[float, int]).to_dict()
    }
    return metadata

def generate_normalization_prompt(dataset_overview, target_columns=None, scaling_techniques=None):
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