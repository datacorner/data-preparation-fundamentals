import pandas as pd
import json
import sqlite3
import matplotlib.pyplot as plt

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

def initialize():
    """ Read the source file (Titanic disaster) and provide a dataframe
    Returns:
        dataframe: dataset read
    """
    # read the CSV file
    df_csv = pd.read_csv(C.DATASET_FOLDER + 'vgames/games_about.csv', delimiter=",")
    # read the JSON file
    with open(C.DATASET_FOLDER + 'vgames/games_genres_valve.json', 'r',  encoding='utf-8-sig') as file:
        data = json.load(file) #A
        df_json = pd.DataFrame(data) 
    # read the Excel file
    df_excel = pd.read_excel(C.DATASET_FOLDER + 'vgames/games_reviews.xlsx')
    # read the data in the DB
    conn = sqlite3.connect(C.DATASET_FOLDER + 'vgames/games_db.sqlite') #A
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
    # Join all the results with the master dataset
    df_allreviews = pd.merge(df_csv, 
                        df_excel, 
                        how='inner', 
                        left_on='RecordID', 
                        right_on='RecordID')
    # Final aggregation
    df_allreviews['Year'] = df_allreviews['Year'].astype(str)
    df_valve_mp = pd.merge(df_allreviews, 
                        df_union, 
                        how='inner', 
                        left_on=["name", "Publisher", "Year"], 
                        right_on=["name", "Publisher", "Year"])
    df_agg = df_valve_mp.groupby([ "Year"])["totalreviews"].sum().reset_index()
    # Plot the result
    df_pivot = df_agg.pivot_table(index='Year', 
                                    values='totalreviews', 
                                    aggfunc='sum') 
    df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Total Reviews by Year')
    plt.xlabel('Year')
    plt.ylabel('Total Reviews')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
