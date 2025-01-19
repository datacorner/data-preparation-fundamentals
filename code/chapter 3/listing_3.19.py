import pandas as pd

if __name__ == "__main__":
    data = {
        'Name': ['John doe', 'John doe', 'Alice Johnson', 'Alice jonson', 'Bob Smith', 'Bob Smith'],
        'Email': ['john@example.com', 'john@example.com', 'alice@domain.com', 'alice@domain2.com', 'bob@website.com', 'bob@website.com'],
        'Date_of_Birth': ['1990-01-01', '1990-01-01', '1985-05-12', '1985-05-12', '1970-08-22', '1970-08-22'],
    }
    
    df = pd.DataFrame(data)
    df_exact = df.drop_duplicates() 

    print("Updated Data:")
    print(df)