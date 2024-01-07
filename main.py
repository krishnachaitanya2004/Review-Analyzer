
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import demoji  
from scrapper import get_reviews, extract_asin
import csv

amazon_url = input("Enter the Amazon URL: ")
asin = extract_asin(amazon_url)
reviews = get_reviews(asin)

csv_file_path = 'reviews.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Reviews'])
    for review_text in reviews:
        csv_writer.writerow([review_text])
print(f"Reviews have been saved to {csv_file_path}.")

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
