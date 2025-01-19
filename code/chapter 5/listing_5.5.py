import spacy
import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

# BE CAREFUL !
# If the error "OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory." happens ...
# That's because the en_core_web_sm model is not installed on your system. To resolve this, follow these steps and install it with this command:
# python -m spacy download en_core_web_sm

def extract_named_entities(comment): 
    """
    Extracts named entities from a given text comment using spaCy's Named Entity Recognition (NER).
    Parameters:
        comment (str): The text comment to extract named entities from.
    Returns:
        list of tuples: A list of named entities, where each entity is represented as a tuple (entity_text, entity_label).
    """
    doc = nlp(comment)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "restaurants/restaurants.csv", encoding='UTF8')
    nlp = spacy.load("en_core_web_sm") 
    df['Named_Entities'] = df['Comment'].apply(extract_named_entities) 
    print(df[["Comment", 'Named_Entities']].head())
