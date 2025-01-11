import pandas as pd

if __name__ == "__main__":
    chunksize = 10
    for chunk in pd.read_csv('../vgames/games_about.csv', chunksize=chunksize):
        print(chunk.head())