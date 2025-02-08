import os
import google.generativeai as genai

task = "Explain the difference between supervised and unsupervised learning."
details = "Supervised learning uses labeled data to train models, while unsupervised learning deals with unlabeled data."
prompt = f"Task: {task}\nDetails: {details}\nResponse:"   
print(prompt)

# Get the Gemini Key
GoogleGeminiKey = os.getenv('GEMINI_KEY', "")
if (GoogleGeminiKey == ""):
    raise Exception(f"Google Gemini Key does not exist, please get a key (https://aistudio.google.com/prompts/new_chat) and set the env variable GEMINI_KEY accordingly")
# Configure the API
genai.configure(api_key=GoogleGeminiKey)
# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash-002") # or gemini-1.5-flash-002 or gemini-1.5-flash-8b

response = model.generate_content(prompt)
print(response.text)