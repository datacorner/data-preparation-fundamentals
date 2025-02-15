import pandas as pd
import re 

def name_to_word_pattern(name):
    """
        This function takes a name string as input and generates a word pattern
        based on its components. It identifies titles, prefixes, punctuation, and
        names, and returns a formatted pattern string representing the structure 
        of the name.
    Parameters:
        name (str): The input name string, which may include titles, prefixes,
                    punctuation, or parentheses.
    Returns:
        str: A word pattern string where:
            - 'TITLE' represents titles (e.g., 'Mr', 'Mrs', 'Dr').
            - 'PREFIX' represents prefixes (e.g., 'van', 'de', 'der').
            - 'NAME' represents other name components.
            - ',' and '.' represent punctuation.
    """
    name_without_parentheses = re.sub(r'\([^)]*\)', '', name).strip()
    words = re.findall(r'\b\w+\b|\.|,', name_without_parentheses)
    pattern = []
    for word in words:
        if word in [',', '.']:
            pattern.append(word)
        elif word.lower() in ['mr', 'mrs', 'miss', 
                                'master', 'dr', 'rev', 
                                'col', 'major', 'capt']:
            pattern.append('TITLE')
        elif word.lower() in ['van', 'de', 'der', 'du', 
                                'di', 'la', 'le']:
            pattern.append('PREFIX')
        else:
            if not pattern or pattern[-1] != 'NAME':
                pattern.append('NAME')
    return ' '.join(pattern)

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    df['NamePattern'] = df['Name'].apply(name_to_word_pattern)
    print(df['NamePattern'].value_counts())