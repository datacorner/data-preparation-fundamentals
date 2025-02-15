import pandas as pd
import re 

def parse_name(name):
    """ This function parses a name string into its components, extracting the 
        individual names, any title (e.g., Mr., Dr.), and any prefix 
        (e.g., van, de). The function is designed to handle names with punctuation 
        and parentheses gracefully, removing irrelevant elements before processing.
    Parameters:
        name (str): The input name string to parse. It may include titles, prefixes, 
                    parentheses, and punctuation.
    Returns:
        dict: A dictionary containing the parsed components:
            - 'names' (list): A list of individual name components (excluding titles and prefixes).
            - 'prefix' (str or None): The identified prefix (if any).
            - 'title' (str or None): The identified title (if any).
    """
    name_without_parentheses = re.sub(r'\([^)]*\)', '', name).strip()
    words = re.findall(r'\b\w+\b|\.|,', name_without_parentheses)
    names = []
    prefix = None
    title = None
    for word in words:
        if word.lower() in ['mr', 'mrs', 'miss', 
                            'master', 'dr', 'rev', 
                            'col', 'major', 'capt']:
            title = word
        elif word.lower() in ['van', 'de', 'der', 
                                'du', 'di', 'la', 'le']:
            prefix = word
        elif word not in [',', '.']:
            names.append(word)

    return {
        'names': names,
        'prefix': prefix,
        'title': title
    }

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    df['NameComponents'] = df['Name'].apply(parse_name)
    df['NameList'] = df['NameComponents'].apply(lambda x: x['names'])
    df['Prefix'] = df['NameComponents'].apply(lambda x: x['prefix'])
    df['Title'] = df['NameComponents'].apply(lambda x: x['title'])
    df = df.drop('NameComponents', axis=1)
    print (df)