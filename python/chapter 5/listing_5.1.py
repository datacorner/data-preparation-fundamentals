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
    print(df[['Comment', 'vader_Sentiment']].head() )
