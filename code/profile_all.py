import pandas as pd
from ydata_profiling import ProfileReport

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def eda(inputfile, outputfile, encoding='UTF8'):
    """ Build out the YData-Profiling report (HTML)
    Args:
        _df (dataframe): dataset to analyze
    """
    df = pd.read_csv(C.DATASET_FOLDER + inputfile, encoding=encoding)
    # Generate the profile report
    profile = ProfileReport(df, title=f"Profiling report for {inputfile}")
    # Build the report
    profile.to_file(C.PROFILE_FOLDER + outputfile)
    
if __name__ == "__main__":
    files = [   { "input" : "titanic/train.csv",  "output": "titanic_report.html" },
                { "input" : "bbcnews/bbc_news_light.csv",  "output": "bbcnews_report.html" },
                { "input" : "bikerental/rental_train.csv",  "output": "bikerental_report.html" },
                { "input" : "superstore/samplesuperstore.csv",  "output": "superstore_report.html" },
                { "input" : "vgames/games_about.csv",  "output": "vgames_about_report.html" }]
    for prof in  files:
        eda(prof["input"], prof["output"])
