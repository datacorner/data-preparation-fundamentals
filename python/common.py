import os
import google.generativeai as genai
import time

DATASET_FOLDER = "../data/"

def get_gemini_response(prompt, max_retries=3, delay=1):
    """
    Get a response from Gemini AI for a given prompt
    Args:
        prompt (str): The prompt to send to Gemini
        api_key (str): Your Gemini API key
        model_name (str): Model to use (default: "gemini-pro")
        max_retries (int): Maximum number of retry attempts
        delay (int): Delay between retries in seconds
    Returns:
        str: The model's response text
    Raises:
        Exception: If all retry attempts fail
    """

    # Get the Gemini Key
    try:
        GoogleGeminiKey = os.environ['GEMINI_KEY']
    except:
        raise Exception(f"Google Gemini Key does not exist, please get a key (https://aistudio.google.com/prompts/new_chat) and set the env variable GEMINI_KEY accordingly")
    # Configure the API
    genai.configure(api_key=GoogleGeminiKey)
    # Initialize the model
    model = genai.GenerativeModel("gemini-pro") # or gemini-1.5-flash-002 or gemini-1.5-flash-8b
    
    # Retry logic
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(f"Failed to get response after {max_retries} attempts: {str(e)}")
            print(f"Attempt {attempt + 1} failed, retrying after {delay} seconds...")
            time.sleep(delay)