# Import common constants and functions
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import get_gemini_response

def create_prompt(task, details):    
    """
    Generates a formatted prompt string based on the provided task and details.
    This function combines the given task and details into a structured prompt format, which can be used to request responses from AI models or other systems.
    Parameters:
        task (str): A description of the task to be performed.
        details (str): Additional details or context related to the task.
    Returns:
        str: A formatted prompt string combining the task and details, ready for use.
    """
    prompt = f"Task: {task}\nDetails: {details}\nResponse:"   
    return prompt    

if __name__ == "__main__":
    task = "Explain the difference between supervised and unsupervised learning."
    details = "Supervised learning uses labeled data to train models, while unsupervised learning deals with unlabeled data."

    prompt = create_prompt(task, details) 
    print(get_gemini_response(prompt))