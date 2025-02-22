import spacy
import pandas as pd

""" WARNING !
If the error `OSError: [E050] Can't find model 'en_core_web_sm' It doesn't seem to be a Python package or a valid path to a data directory.`
is raised. That's because the en_core_web_sm model is not installed on your system. 
To resolve this, install it by running this command:

$ python -m spacy download en_core_web_sm

"""

def extract_gpe_entities(comment):
    """
    Extracts Geopolitical Entity (GPE) named entities from a given text comment using spaCy's Named Entity Recognition (NER).
    Parameters:
        comment (str): The text comment to extract GPE entities from.
    Returns:
        str: A comma-separated string of GPE entities found in the comment.
    """
    doc = nlp(comment)
    gpe_entities = {ent.text for ent in doc.ents if ent.label_=="GPE"} #A
    return ", ".join(sorted(gpe_entities))  

if __name__ == "__main__":
    df = pd.read_csv("../data/restaurants/restaurants.csv", encoding='UTF8')
    nlp = spacy.load("en_core_web_sm") 
    df['GPE_Entities'] = df['Comment'].apply(extract_gpe_entities) 
    df['GPE_Entities'].value_counts()
    print(df['GPE_Entities'].value_counts())
