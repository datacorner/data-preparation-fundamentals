import pandas as pd
import sqlite3

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: dataset
    """
    # read the data in the DB
    conn = sqlite3.connect('../vgames/games_db.sqlite') #A
    query = "select games.name, games.publisher, games.year, genres.genre "
    query += "from games, genres "
    query += "where games.genre = genres.ID" #B
    df_sq = pd.read_sql_query(query, conn) 
    conn.close() 
    return df_sq

if __name__ == "__main__":
    df_sq = initialize()
    print(df_sq.head())