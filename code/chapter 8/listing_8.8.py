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
def build_feature_generation_prompt(dataset_sample, metadata, target=None, task_type="classification"):
    """
    Generate a prompt to guide a generative AI model in creating new features from existing data.

    Args:
        dataset_sample (pd.DataFrame): A small sample of the dataset (e.g., 5-10 rows).
        metadata (dict): Metadata about the dataset, including column types, missing values, etc.
        target (str): The target variable for prediction (optional).
        task_type (str): The type of machine learning task ('classification', 'regression', etc.).

    Returns:
        str: A formatted prompt for generative AI.
    """
    # Define the context and dataset description
    prompt = f"""
                You are an expert data scientist tasked with generating new features to improve a machine learning model's performance.
                The task type is '{task_type}' and the dataset is described below:

                ### Dataset Overview:
                - Columns: {metadata['columns']}
                - Data types: {metadata['data_types']}
                - Summary statistics: {metadata['summary_stats']}
                - Missing values per column: {metadata['missing_counts']}
                - Target variable: {target if target else "None"}

                Here is the dataset:
                {dataset_sample.to_string(index=False)}

                ### Instructions:
                1. **Propose New Features**:
                - Suggest new features based on transformations, interactions, and aggregations.
                - For numerical columns, consider transformations like log, square root, or scaling.
                - For categorical columns, propose feature interactions or encodings.
                - For time-based data, suggest temporal features like day of the week or seasonality.
                - Include domain-specific suggestions if applicable.

                2. **Feature Interactions**:
                - Identify potential feature interactions (e.g., ratios, differences, products).
                - Propose polynomial or combined features for numerical data.

                3. **Aggregations**:
                - For groupable columns (e.g., categorical or time-based), suggest aggregations like mean, max, min, or count.

                4. **Provide Explanations**:
                - Explain how each new feature could contribute to improving the model's performance.
                - Highlight which features might be most relevant for the target variable '{target}'.

                Return your recommendations in the following format:
                - Suggested Features: List of new feature definitions with explanations.
                """
    return prompt


if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Get metadata
    metadata = collect_metadata(chunks[0])
    print(metadata)
    
    prompt = build_feature_generation_prompt(chunks[0], metadata)
    print(f"Prompt {prompt}")
    
    response = C.get_gemini_response(prompt)
    print(f"Response for Chunk {0}:\n{response}\n")