from pprint import pprint
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from textblob import Word,TextBlob

stop = stopwords.words('english')

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity ==0:
        return 'Neutral'
    else:
        return 'Negative'

def preprocess_text(text):
	text = " ".join(text.lower() for text in text.split())
	text = text.replace('[^\w\s]','')
	text = " ".join(text for text in text.split() if text not in stop)
	text = " ".join([Word(word).lemmatize() for word in text.split()])
	return text
	
df = pd.read_csv('Scraping Product reviews.csv')
df['Review Text'] = df['Review Text'].apply(lambda x: preprocess_text(x))
df['Sentiment'] = df['Review Text'].apply(lambda x: analyze_sentiment(x))

df=df[['Id','Title','Review Text','Sentiment']]
print(df['Sentiment'].value_counts())
df.to_csv('Sentiment Analysis.csv',index=False)