# README
In this folder you'll find all the book's listings.  
**Note: Each python file follows the book naming convention (meaning listing_3.4.py refers to the listing 3.4 you can find in the chapter 3).**

# Python environment creation
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

# Profiling
The datasets used in this book have already been profiled. The outcome can be found in the /profiles folder.