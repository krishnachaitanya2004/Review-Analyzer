
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import demoji  
from scrapper import store_reviews

link = input("Enter the Amazon product link: ")
store_reviews(link)

data = pd.read_csv('reviews.csv')
query = data['Reviews']

# Ensure that the values are strings before applying demoji.replace
query = query.apply(lambda x: demoji.replace(str(x), ''))

analyser = SentimentIntensityAnalyzer()
sentiment = analyser.polarity_scores(query)

# Positive, Negative, Neutral results
if sentiment['compound'] >= 0.05:
    print("Positive. Definitely recommended buy this product")
elif sentiment['compound'] <= -0.05:
    print("Negative. Don't buy this product")
elif -0.05 < sentiment['compound'] < 0.05:
    print("Neutral. Depends on your choice to buy or not")
