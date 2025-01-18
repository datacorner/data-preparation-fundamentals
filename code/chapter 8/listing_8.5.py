# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C
import pandas as pd

def collect_metadata(chunk):
    metadata = {
        "columns": chunk.columns.tolist(),
        "missing_counts": chunk.isna().sum().to_dict(),
        "column_means": chunk.mean(numeric_only=True).to_dict(),
        "column_medians": chunk.median(numeric_only=True).to_dict(),
        "column_modes": chunk.mode(dropna=True).iloc[0].to_dict()
    }
    return metadata

def build_normalization_prompt(chunk, metadata):
    prompt = f"""
                You are a data expert helping to clean a dataset by performing noise reduction and normalization. The dataset is structured as follows:
                Columns: {metadata['columns']}
                Metadata about the columns:
                - Missing value counts: {metadata['missing_counts']}
                - Column means: {metadata['column_means']}
                - Column medians: {metadata['column_medians']}
                - Column modes: {metadata['column_modes']}

                Here is a sample of the data (including some noisy values or outliers) for analysis:
                {chunk.head(5).to_string(index=False)}

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

                Provide the updated values after applying these techniques.
                """
    return prompt
if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "titanic/train.csv")
    # Chunks the dataset
    chunk_size = 100
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Get metadata
    metadata = collect_metadata(chunks[0])
    prompt = build_normalization_prompt(chunks[0], metadata)
        
    response = C.get_gemini_response(prompt)
    print(f"Prompt {prompt}")
    print(f"Response for Chunk {0}:\n{response}\n")