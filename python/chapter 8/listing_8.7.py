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

def build_feature_engineering_prompt(dataset_chunk, 
                                        metadata, 
                                        targetvariable, 
                                        task_type="classification"):
    prompt = f"""
                You are an advanced data scientist specializing in feature engineering to improve machine learning models. 
                The dataset you are working with is structured as follows:
                - Columns: {metadata['columns']}
                - Metadata:
                    - Columns name: {metadata['columns']}
                    - Columns data types: {metadata['data_types']}
                    - Summary statistics: {metadata['summary_stats']}
                    - Number of missing values: {metadata['missing_counts']}
                    - Target variable: {targetvariable}
                    - Machine learning task type: {task_type}
                Here is the dataset:
                {dataset_chunk.head(5).to_string(index=False)}

                ### Your Task:
                1. **Feature Suggestions**:
                - Based on the provided dataset, suggest new features that could improve the model's predictive power.
                - Focus on transformations, interactions, and aggregations.
                    - Transformations: Log, square root, or normalization for numerical data.
                    - Interactions: Multiplying, dividing, or combining existing features (e.g., feature ratios or polynomial features).
                    - Aggregations: Group by key columns and calculate aggregates (e.g., mean, max, sum).
                    - Text features: Extract keywords, sentiment scores, or embeddings if text columns exist.
                - Ensure the new features are interpretable and relevant to the task type.

                2. **Feature Encoding**:
                - Identify columns requiring encoding (e.g., categorical variables).
                - Suggest encoding strategies (e.g., one-hot encoding, ordinal encoding, or target encoding) based on their suitability for the dataset.

                3. **Feature Selection**:
                - Identify low-variance or redundant features that might not contribute to the model's performance.
                - Suggest dropping or modifying such features.

                4. **Explainability**:
                - Provide a brief explanation for each feature suggestion, focusing on how it might improve model performance.

                Output your recommendations in the following format:
                - Suggested Features: A list of new features with their transformations/definitions.
                - Feature Encoding: A description of encoding strategies for categorical variables.
                - Feature Selection: A list of features to consider dropping with reasons.
                """
    return prompt


if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Get medatata
    metadata = collect_metadata(chunks[0])
    print(metadata)
    
    prompt = build_feature_engineering_prompt(chunks[0], metadata, "Survived")
    print(f"Prompt {prompt}")
    
    response = C.get_gemini_response(prompt)
    print(f"Response for Chunk {0}:\n{response}\n")