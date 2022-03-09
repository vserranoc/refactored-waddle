#!pip install tweepy
#!pip install pandas-gbq

import tweepy
import pandas as pd
import yaml
from google.cloud import bigquery

with open("src/config.yaml", "r") as config:
    config = yaml.safe_load(config)

# Credentials
consumer_key = config['consumer_key']
consumer_secret =  config['consumer_secret']
access_token =  config['access_token']
access_token_secret =  config['access_token_secret']

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 


user = []
text = []
followers = []
location = []
verified = []
df = pd.DataFrame(columns=['user','text','followers','location','verified'])


# Extract
themes = ['travel','booking','hotel','trivago','airbnb','travel agency','travelling','vacation','instatravel','tourism','traveller','trip','journey','tour','tourist']

#Transform
for theme in themes:
	# The search term
	query = '{} -filter:retweets'.format(theme)
	# Language code (follows ISO 639-1 standards)
	language = "en"
	# Calling the api
	results = api.search_tweets(q=query, lang=language, count=100)
	# Features
	for tweet in results:
		user.append(tweet.user.screen_name)
		text.append(tweet.text)
		followers.append(tweet.user.followers_count)
		location.append(tweet.user.location)
		verified.append(tweet.user.verified)
df['user'] = user
df['text'] = text
df['followers'] = followers
df['location'] = location
df['verified'] = verified

#Load
#To BigQuery
bigquery_client = bigquery.Client(project=config['project'])
#Tweets (text)
df[['user','text']].to_gbq(destination_table = 'tweets.text',project_id = config['project'],if_exists='replace')
#Users
df.drop(columns='text').to_gbq(destination_table = 'tweets.users',project_id = config['project'],if_exists='replace')