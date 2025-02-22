from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

if __name__ == "__main__":
    dfnews = pd.read_csv("../data/bbcnews/bbc_news.csv", encoding='UTF8')
    
    # Combine title and description
    dfnews['text'] = dfnews['title'] + ' ' + dfnews['description']
    # Preprocess dataset
    vectorizer = CountVectorizer(stop_words="english", min_df=0.10, max_df=0.85)
    
    # Build a BERTopic model
    topic_model = BERTopic(vectorizer_model=vectorizer, min_topic_size=20)
    topics, probs = topic_model.fit_transform(dfnews['text'])
    dfnews['topic'] = topics 
    # Get the topic info
    topic_info = topic_model.get_topic_info()
    # Create a dictionary mapping topic numbers to topic names
    topic_dict = dict(zip(topic_info['Topic'], topic_info['Name']))
    # Add the 'topic_name' column to dfnews
    dfnews['topic_name'] = dfnews['topic'].map(topic_dict)
    print( dfnews['topic_name'].value_counts() )
    
    fig = topic_model.visualize_topics()
    fig.show()