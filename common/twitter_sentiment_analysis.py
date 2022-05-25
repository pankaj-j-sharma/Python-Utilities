# Import the libraries
import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler
import re
import pprint
import random

# importing TextBlob. It has build-in sentiment property
from textblob import TextBlob
# The sentiment property returns a named tuple of the form 
# Sentiment(polarity,subjectivity). The polarity score is a float 
# within the range [-1.0, 1.0]. 
# The subjectivity is a float within the range [0.0, 1.0] 
# where 0.0 is very objective and 1.0 is very subjective.

# -----------------------------------------------------------------------
def connect_to_twitter():
	# credentials  --> put your credentials here
	consumer_key = "mGbZJsHQGcy7I1FeNREVK6vtd"
	consumer_secret = "WrirjyTUQaReug3MqijfgNa4cGVyX9iTAvK1Q3RNNKjC9a9z5M"
	access_token = "137723722-E15RwdQBe2sPBPMwtOME80lNUNtnySj2Wh0Vg6Kd"
	access_token_secret = "a4y63Dnx9O1sWPgGvfgBZ4mBUO212yQS6lcP62szTDrsf"

	# calling API
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)	
	return api
#--------------------------------------------------------------------------

# Next, lets define a function as follows which will read 1000 tweets 100 at a time				 
def stream(data, file_name):
	i = 0
	for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():
		print(i, end='\r')
		df.loc[i, 'Tweets'] = tweet.text
		df.loc[i, 'User'] = tweet.user.name
		df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count  # indicates the no. of times the user as tweeted 
		df.loc[i, 'user_followers'] = tweet.user.followers_count
		df.loc[i, 'User_location'] = tweet.user.location
		df.loc[i, 'User_verified'] = tweet.user.verified
		df.loc[i, 'fav_count'] = tweet.favorite_count
		df.loc[i, 'rt_count'] = tweet.retweet_count
		df.loc[i, 'tweet_date'] = tweet.created_at
		#df.to_excel('{}.xlsx'.format(file_name))
		i+=1
		if i == 1000:
			break
		else:
			pass

# Method clean the tweet data i.e remove special characters and url and get only the context
def clean_tweet(tweet):
	return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())

# Let's also write our sentiment analyzer function:
def analyze_sentiment(tweet):
	analysis = TextBlob(tweet)
	if analysis.sentiment.polarity > 0:
		return 'Positive'
	elif analysis.sentiment.polarity ==0:
		return 'Neutral'
	else:
		return 'Negative'

if __name__=='__main__':		

	# Provide the query you want to pull the data.
	#query = "Capgemini Mumbai"
	query = input('Please enter the query to search for > \n')
	if not query:
		print('Please try again with valid input for query search')
		exit

	# Fetching sample 10 tweets
	api = connect_to_twitter()
	# Tweets = api.search(query, count = 10, lang='en', exclude='retweets',tweet_mode='extended')

	# for tweet in Tweets:
		# pprint.pprint(tweet)
		# print("-"*100)

	# The query above will pull the top 10 tweets when the term provided in query 
	# is searched. The API will pull English tweets since the language 
	# given is ‘en’ and it will exclude retweets.

	# start by creating an empty DataFrame with the columns we'll need
	df = pd.DataFrame(columns = ['Tweets', 'User', 'User_statuses_count', 
								 'user_followers', 'User_location', 'User_verified',
								 'fav_count', 'rt_count', 'tweet_date'])


	# calling the stream function to stream the tweet data 
	stream(data = [query], file_name = 'my_tweets')


	# view first 5 records
	df.head()
	print(df.shape)
	if(df.shape[0]==0):
		exit

	# Now let's create our new columns:
	df['clean_tweet'] = df['Tweets'].apply(lambda x: clean_tweet(x))
	df['Sentiment'] = df['clean_tweet'].apply(lambda x: analyze_sentiment(x))

	# Random row data from the tweet
	n=random.randrange(1,df.shape[0],1)
	print('\n'+'-'*100)
	print('Original tweet:\n'+ df['Tweets'][n]+'\n')
	print('Clean tweet:\n'+df['clean_tweet'][n] + '\n')
	print('Sentiment:\n'+df['Sentiment'][n] + '\n')
	print('-'*100)
	#df[df['Sentiment']=='Negative']

	# Print sentiment analysis data 
	positive = df[df.Sentiment=='Positive'].shape[0]
	neutral = df[df.Sentiment=='Neutral'].shape[0]
	negative = df[df.Sentiment=='Negative'].shape[0]
	print('positive ->',positive)
	print('neutral  ->',neutral)
	print('negative ->',negative)