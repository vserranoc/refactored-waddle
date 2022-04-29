import tweepy
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq




def set_api(bbb):
	# Creating the authentication object
	auth = tweepy.OAuth2BearerHandler(bbb)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth, wait_on_rate_limit=True)#,wait_on_rate_limit_notify=True)
	return api


def get_write_tweets(bearer,project_id,database,table,search):
	api = set_api(bearer)
	query = '@'+search+' -filter:retweets'
	searchQuery = query
	sinceId = None
	tweetsPerQry = 100

	user = []
	text = []
	followers = []
	location = []
	verified = []
	tweet_id = []
	created_at=[]

	df = pd.DataFrame(columns=['user','text','followers','location','verified'])

	max_id = -1
	##however many you want to limit your collection to.  how much storage space do you have?
	maxTweets = 100

	tweetCount = 0
	while tweetCount < maxTweets:
	    try:
	        if (max_id <= 0):
	            if (not sinceId):
	                new_tweets = api.search_tweets(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended')
	            else:
	                new_tweets = api.search_tweets(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        since_id=sinceId)
	        else:
	            if (not sinceId):
	                new_tweets = api.search_tweets(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        max_id=str(max_id - 1))
	            else:
	                new_tweets = api.search_tweets(q=searchQuery, count=tweetsPerQry, lang='en',tweet_mode='extended',
	                                        max_id=str(max_id - 1),
	                                        since_id=sinceId)
	        if not new_tweets:
	            break
	        for tweet in new_tweets:
	          #print(tweet)
	          user.append(tweet.user.screen_name)
	          text.append(tweet.full_text)
	          tweet_id.append(tweet.id)
	          created_at.append(tweet.created_at)
	          followers.append(tweet.user.followers_count)
	          location.append(tweet.user.location)
	          verified.append(tweet.user.verified)
	        tweetCount += len(new_tweets)
	        max_id = new_tweets[-1].id
	    except tweepy.TweepError as e:
	        # Just exit if any error
	        break
	df['tweet_id'] = tweet_id
	df['created_at'] = created_at
	df['user'] = user
	df['text'] = text
	df['followers'] = followers
	df['location'] = location
	df['verified'] = verified


	#write to bq
	credentials = service_account.Credentials.from_service_account_info({},)
	destination = database + '.' +table
	pandas_gbq.to_gbq(df,destination_table = destination,project_id = project_id,credentials=credentials,if_exists='append')


