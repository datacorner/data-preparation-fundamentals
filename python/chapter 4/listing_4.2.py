import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    chunksize = 10
    for chunk in pd.read_csv(C.DATASET_FOLDER + 'vgames/games_about.csv', chunksize=chunksize):
        print(chunk.head())