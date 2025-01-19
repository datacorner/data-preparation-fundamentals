import pandas as pd

if __name__ == "__main__":
    data = { #A
        'Name': [' John ', 'DOE', 'Alice', ' bob '],
        'Date_of_Birth': ['12/05/1990', '12-05-1990', 
                        '1990.05.12', '1990/12/05'],
        'Height(cm)': [180, 5.9, 170, 5.7], 
        'Category': ['Yes', 'Y', 'No', 'N'],
        'ref_id': [1, 1, 2, 3],
    } 

    refdata = { 'ref_id': [1, 2, 3], 
            'Reference': ['Ref1', 'Ref2', 'Ref3']}

    df = pd.DataFrame(data)
    df_ref = pd.DataFrame(refdata)
    
    print("Original Data:")
    print(df)
    
    df['std_Name'] = df['Name'].str.strip().str.lower()
    def parse_date(date_str):
        date_formats = ['%d/%m/%Y', '%m-%d-%Y', '%Y.%m.%d', '%Y/%m/%d']
        for fmt in date_formats:
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                continue
        return pd.NaT
    df['std_Date_of_Birth'] = df['Date_of_Birth'].apply(parse_date)

    df['std_Height(cm)'] = df['Height(cm)'].apply(lambda x: x * 30.48 if x < 100 else x) #D
    df['std_Category'] = df['Category'].replace({'Y': 'Yes', 'N': 'No'}) #E
    df = pd.merge(df, df_ref, on='ref_id', how='left') #F
    
    print("Updated Data:")
    print(df)


