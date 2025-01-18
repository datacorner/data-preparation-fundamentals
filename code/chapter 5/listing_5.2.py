import nltk
from nltk.wsd import lesk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    df["vader_Sentiment"].value_counts().plot(kind='barh', 
                                                color=sns.palettes.mpl_palette('Dark2'))
    plt.gca().spines[['top', 'right',]].set_visible(False)
    plt.show()