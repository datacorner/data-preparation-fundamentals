# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import get_gemini_response, clean_gemini_response, DATASET_FOLDER
import pandas as pd

def build_normalization_prompt(chunk):
    """
    Generates a formatted prompt string based on the provided task and details.
    Parameters:
        chunk (str): chunk data
    Returns:
        str: A formatted prompt string combining the task and details, ready for use.
    """
    prompt = f"""
                You are a data expert helping to clean a dataset by performing noise reduction and normalization. 

                Here is the dataset (including some noisy values or outliers) for analysis:
                {chunk.to_string(index=False)}

                ### Your tasks:
                1. Normalize numerical features to ensure they are on a similar scale. You can apply one or more of the following methods:
                    - **Min-Max Scaling**: Scale values between 0 and 1.
                    - **Standardization (Z-Score Normalization)**: Adjust the dataset to have a mean of 0 and a standard deviation of 1.
                    - **Robust Scaling**: Normalize using median and IQR to handle outliers.

                2. Return the updated data for the dataset provided in a JSON format (each row as a node) without any prefix or decoration. 
                I should be able to leverage the response directly by using a programming language (like python), by just importing the result as is.
                Please only provide the result of task 2
                """
    return prompt

if __name__ == "__main__":
    df = pd.read_csv(DATASET_FOLDER + "titanic/train.csv")
    # Only get the first 10 rows
    chunk0 = df.head(10)
    # Build the prompt
    prompt = build_normalization_prompt(chunk0)
    # Send the prompt to the LLM and gets the response back
    response = clean_gemini_response(get_gemini_response(prompt))
    new_df = pd.DataFrame(response)
    print(f"Prompt: {prompt}")
    print(f"Response:\n{new_df}\n")