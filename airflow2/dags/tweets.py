import tweepy
import pandas as pd
from google.cloud import bigquery



def get_write_tweets(consumer_key,consumer_secret,access_token,access_token_secret,project_id,database,table,search):
	# Creating the authentication object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	# Setting your access token and secret
	auth.set_access_token(access_token, access_token_secret)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth)

	query = '@'+search+' -filter:retweets'
	searchQuery = query
	sinceId = None
	tweetsPerQry = 100

	user = []
	text = []
	followers = []
	location = []
	verified = []
	df = pd.DataFrame(columns=['user','text','followers','location','verified'])

	max_id = -1
	##however many you want to limit your collection to.  how much storage space do you have?
	maxTweets = 10000

	tweetCount = 0
	while tweetCount < maxTweets:
	    try:
	        if (max_id <= 0):
	            if (not sinceId):
	                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended')
	            else:
	                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        since_id=sinceId)
	        else:
	            if (not sinceId):
	                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        max_id=str(max_id - 1))
	            else:
	                new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        max_id=str(max_id - 1),
	                                        since_id=sinceId)
	        if not new_tweets:
	            break
	        for tweet in new_tweets:
	          #print(tweet)
	          user.append(tweet.user.screen_name)
	          text.append(tweet.full_text)
	          followers.append(tweet.user.followers_count)
	          location.append(tweet.user.location)
	          verified.append(tweet.user.verified)
	        tweetCount += len(new_tweets)
	        max_id = new_tweets[-1].id
	    except tweepy.TweepError as e:
	        # Just exit if any error
	        break
	df['user'] = user
	df['text'] = text
	df['followers'] = followers
	df['location'] = location
	df['verified'] = verified

	client = bigquery.Client(project=project_id)
	destination = database + '.' +table
	df.to_gbq(destination_table = destination,project_id = project_id)
