# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def create_prompt(task, details):    
    # Template for the prompt    
    prompt = f"Task: {task}\nDetails: {details}\nResponse:"   
    return prompt    

if __name__ == "__main__":
    task = "Explain the difference between supervised and unsupervised learning."
    details = "Supervised learning uses labeled data to train models, while unsupervised learning deals with unlabeled data."

    prompt = create_prompt(task, details) 
    print(C.get_gemini_response(prompt))