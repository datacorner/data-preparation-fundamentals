import pandas as pd
import json
import sqlite3

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe

    Returns:
        dataframe: dataset read
    """
    # read the CSV file
    df_csv = pd.read_csv('../vgames/games_about.csv', delimiter=",")
    # read the JSON file
    with open('../vgames/games_genres_valve.json', 'r',  encoding='utf-8-sig') as file:
        data = json.load(file) #A
        df_json = pd.DataFrame(data) 
    # read the Excel file
    df_excel = pd.read_excel('../vgames/games_reviews.xlsx')
    # read the data in the DB
    conn = sqlite3.connect('../vgames/games_db.sqlite') #A
    query = "select games.name, games.publisher, games.year, genres.genre "
    query += "from games, genres "
    query += "where games.genre = genres.ID" #B
    df_sq = pd.read_sql_query(query, conn) 
    conn.close() 
    return df_csv, df_json, df_excel, df_sq

if __name__ == "__main__":
    df_csv, df_json, df_excel, df_sq = initialize()
    df_json["Genre"] = df_json["Genre"].replace('Multi Player', 'Multiplayer')
    df_sq_filtered = df_sq[df_sq['Genre'] == 'Multiplayer']
    df_json_filtered = df_json[df_json['Genre'] == 'Multiplayer']
    print(f"JSON Filtered: {df_json_filtered.shape}")
    print(f"DB Filtered: {df_sq_filtered.shape}")
    df_union = pd.concat([df_sq_filtered, df_json_filtered], ignore_index=True)
    df_union = df_union.drop('Genre', axis=1)
    print(f"Union: {df_union.shape}")
    print (df_union.head())