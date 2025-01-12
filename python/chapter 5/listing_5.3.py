import nltk
from nltk.wsd import lesk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "restaurants/restaurants.csv", encoding='UTF8')
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer() 

    def analyze_sentiment(comment): 
        scores = sia.polarity_scores(comment)
        if scores['compound'] >= 0.05:
            return "Positive"
        elif scores['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df['vader_Sentiment'] = df['Comment'].apply(analyze_sentiment) 
    # Define the mapping between ratings and sentiment values
    rating_sentiment_map = {
        1: 'Negative',
        2: 'Negative',
        3: 'Neutral',
        4: 'Positive',
        5: 'Positive'
    }
    # Round the StarRating to the nearest whole number
    df['RoundedRating'] = df['StarRating'].round()
    # Map the sentiments to the ratings based on the predefined mapping
    df['MappedSentiment'] = df['RoundedRating'].map(rating_sentiment_map)
    print(df[['MappedSentiment', 'StarRating']].head())