import nltk
from nltk.wsd import lesk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sentiment(comment): 
    """
    Analyzes the sentiment of a given comment using the VADER sentiment analysis tool.  
    The function classifies the sentiment as 'Positive', 'Negative', or 'Neutral' based on the compound score.
    Parameters:
        comment (str): The text comment to analyze.
    Returns:
        str: The sentiment classification ('Positive', 'Negative', or 'Neutral').
    """
    scores = sia.polarity_scores(comment)
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"
    
if __name__ == "__main__":
    df = pd.read_csv("../data/restaurants/restaurants.csv", encoding='UTF8')
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer() 

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
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
    # Plot histogram for vader_Sentiment
    sns.histplot(data=df, x='vader_Sentiment', hue='vader_Sentiment', multiple='stack', palette='Dark2', ax=ax[0])
    ax[0].set_title('Distribution of VADER Sentiment')
    ax[0].set_xlabel('Sentiment')
    ax[0].set_ylabel('Count')

    # Plot histogram for MappedSentiment
    sns.histplot(data=df, x='MappedSentiment', hue='MappedSentiment', multiple='stack', palette='Dark2', ax=ax[1])
    ax[1].set_title('Distribution of Sentiment from Ratings')
    ax[1].set_xlabel('Sentiment')
    ax[1].set_ylabel('Count')

    plt.tight_layout()
    plt.show()
