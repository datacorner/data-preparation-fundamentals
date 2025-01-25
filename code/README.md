# README
In this folder you'll find all the book's listings.  
**Note: Each python file follows the book naming convention (meaning listing_3.4.py refers to the listing 3.4 you can find in the chapter 3).**

# Creating the Python environment
To leverage the resources provided in this repository it's first recommended to create a python virtual environment. 

## Why Use Virtual Python Environments?
Using a virtual environment is crucial for managing dependencies in Python projects. It helps to:
- **Avoid Conflicts**: Different projects may require different versions of the same package. Virtual environments keep dependencies isolated.
- **Ensure Reproducibility**: When sharing your project, others can install the same versions of dependencies you used.
- **Maintain a Clean Global Environment**: Prevent clutter in your global Python installation by installing packages only in the virtual environment.

## Different Ways to Create Virtual Environments
There are several ways to create and manage virtual environments in Python:

1. **Using `venv` (Native Python)**: Lightweight and included in Python 3.3 and later.  
   - Documentation: [Python venv](https://docs.python.org/3/library/venv.html)

2. **Using `virtualenv`**: A widely-used external tool, compatible with Python 2 and older versions of Python 3.  
   - Documentation: [Virtualenv](https://virtualenv.pypa.io/en/latest/)

3. **Using `conda`**: An environment manager provided by Anaconda. Suitable for managing Python and non-Python dependencies.  
   - Documentation: [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

4. **Using `pipenv`**: Combines `pip` and `virtualenv` for better dependency management.  
   - Documentation: [Pipenv](https://pipenv.pypa.io/en/latest/)

## Step-by-Step Guide: Using the Native Python Way (`venv`)

### Prerequisites

- Ensure Python 3.3 or later is installed on your system.

### Steps

1. **Navigate to Your Project Directory**  
   Open a terminal and navigate to the folder where your project is located:  
   ```bash
   cd /path/to/your/project
2. **Create a Virtual Environment**
    Run the following command to create a virtual environment named env:
    ```bash
    python3 -m venv env
    ```
    This will create a directory called env containing the virtual environment files.

3. **Activate the Virtual Environment**
    On Windows:
    ```bash
    .\env\Scripts\activate
     ```
    On macOS/Linux:
    ```bash
    source env/bin/activate
     ```
    After activation, your terminal prompt will show (env) indicating the virtual environment is active.

    4. **Install Dependencies**
    Use the requirements.txt that is available at the root of the repository and install all the needed libraries like this:
    ```bash
    pip install -r requirements.txt
    ```
# Specific libraries for chapter 5

## Spacy model download
In chapter 5 (listings 5.5 and 5.6) we leverage the spacy library, but to make it work properly we need first to download the en_core_web_sm model. Please run the command below
```
python -m spacy download en_core_web_sm
```
## Installing Tesseract
We leverage Tesseract on the listing 5.10 and 5.11, but this library must also be installed beforehand.

* Windows
  * Download: Download the installer from the official [Tesseract website](https://github.com/UB-Mannheim/tesseract/wiki)
  * Installation:
      * Run the installer.
      * Choose the installation directory (e.g., C:\Program Files\Tesseract-OCR).
      * Select the desired language data to install (e.g., English, German, etc.).
      * Complete the installation.
  * Environment Variable:
      * Add the installation directory (e.g., C:\Program Files\Tesseract-OCR) to your system's PATH environment variable. This allows you to run Tesseract commands from any command prompt.
* Mac
  * Install Homebrew (if not already installed) by running in a terminal:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  * Install Tesseract with Homebrew:
    ```
    brew install tesseract
    ```
  * Install language data:
    ```
    brew install tesseract-lang/data/eng
    ```
* Linux
  * Update package lists in a terminal: 
      ```
      sudo apt update
      ```
   * Install Tesseract and language data: 
      ```
      sudo apt install tesseract-ocr tesseract-ocr-eng 
      ```
**Note:** Verify Installation by Opening a terminal or command prompt and running:
```
tesseract --version
```
# Leveraging Google AI
In **chapter 8** we'll use Google AI in the code to illustrate the book's topics.
These are the steps to get ready:
* Obtaining a Google Key
* Creating the GEMINI_KEY environment variable
## Obtaining a Google AI Studio API Key
1. Access to [Google AI Studio](https://aistudio.google.com/)
2. Sign in by using your Google Account
3. Create an API Key: 
   * Navigate to API Keys: Locate the section for API keys or credentials within Google AI Studio. As of today it's a simple button avaialbe on the top left.
   * Create a New Key: Follow the provided instructions to generate a new API key.
   * Restrict the Key (Optional): Enhance security by restricting key usage:
        * Application Restrictions: Specify the allowed websites or applications.
        * IP Address Restrictions: Limit usage to specific IP addresses or ranges.
4. Copy the Key: Carefully copy the generated API key. Treat it like a password!

*Important Notes*
* Security: 
   * Never hardcode the API key directly in your code. Utilize secure storage methods like environment variables or secrets management.
   * Regularly rotate API keys to minimize the risk of compromise.
* Usage Limits: Be aware of any usage limits or quotas associated with your API key.
**Disclaimer: This information is for general guidance. Always refer to the [official Google AI Studio documentation](https://ai.google.dev/gemini-api/docs/api-key) for the most up-to-date and accurate instructions.**

## Creating the GEMINI_KEY environment variable
1. Access System Properties:
    * Windows: Search for "Environment Variables" in the Start Menu.
        Right-click "This PC" or "My Computer" and select "Properties". Go to "Advanced system settings" and click "Environment Variables".
    * macOS/Linux: Open your terminal.
2. Create a New Variable:
    * Windows: In the "System variables" section, click "New".
        * Enter the Variable name: GEMINI_KEY.
        * Enter the Variable value (your actual API key you've created beforehand).
        * Click "OK" to save.
    * macOS/Linux:
        Use the following command in the terminal:
         ```
         export GEMINI_KEY="your_actual_api_key" 
         ```

This sets the variable for the current terminal session. To make it persistent, add this line to your shell's configuration file (e.g., .bashrc, .zshrc).

# Installing Alteryx
Fortunately, Alteryx offers a free trial version, [available for download here](https://www.alteryx.com/designer-trial/free-trial-alteryx/designer-trial-form). The trial lasts for 30 days, providing ample time to explore its capabilities and evaluate its potential for data preparation and analysis. As of today, the Alteryx trial version installation process is straightforward and user-friendly, allowing us to get up and running quickly. 
1.	**Download the Installer:** Start by visiting the Alteryx Designer Trial page. Fill out the registration form with basic details to access the download link for the trial version.
2.	**Run the Installation:** Once the installer file is downloaded, we can launch it and follow the guided setup process. The installer will prompt us to accept the license agreement and choose a destination folder for the installation.
3.	**Initial Setup and Activation:** After the installation completes, open Alteryx Designer. We will be prompted to activate the 30-day trial by signing in with our Alteryx account (created during the download process).
4.	**Access Sample Workflows:** Upon activation, Alteryx Designer provides access to sample workflows and built-in tutorials to help you get started quickly. These resources are useful for understanding key functionalities like data input, blending, and transformation.

SYSTEM REQUIREMENTS Alteryx Designer requires a Windows operating system, with recommended specifications including at least 8GB of RAM and adequate disk space for processing large datasets.
The entire process is designed to take only a few minutes, ensuring you can begin exploring Alteryx’s features right away without needing any advanced technical setup.

*Note: the exports provided in this repository have been created with Alteryx v2024.1.1.93  Patch: 3*