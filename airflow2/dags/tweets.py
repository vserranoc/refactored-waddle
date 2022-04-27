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

	credentials = service_account.Credentials.from_service_account_info({
  "type": "service_account",
  "project_id": "refactored-waddle",
  "private_key_id": "e1e941dcac05add6d34a0fe8247ca73c547b7e04",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCJ/i6IChYz6luo\ncrSGTP9l80hz25sYq1S82Y0eGqf+0nDWYOflqpzgcLJ44VMdzl1iFoTuxHISDjVz\nsfw5Mel504ZlIZ93Xjzpkwki3mlFTNO1iHv4ZE88tKSFaqrdP5+AYB3ewKNE2MZg\nx393t6yekm/AVHi8ruvGPXUia0yHO5Var+dM0FEPFhzYoWuJHRfZ1ZJpvr1BhKTA\nEtcG6+UWvVERgS2+GKHzq8z8iQhomh6lDDCPKFrPQXaOyhDwjfwb7SuWDdqN9HR7\nBYRqpdGRANxt7NsHLxWGT1YqF2q3Liu9LpVO36G/e9N/syKEHegnJoExLpTnf01+\npoLLlbV/AgMBAAECggEAIceaRm0JsF2/YEXsETBKGP/sDYiFuA1A6hXraKIn28ZS\nHviL6/nO+1Y7KkImYZaB36AZnIV0Ux0tUowQbUPdnpf8P0dyzPrBuH/o7aM6a995\nt+eYSV7s0rR5zbsl5pFLj1Z4GW5YyWKzdT+A4aKR3COGvbMv9yhuyRGEWg+gJT5B\ns4gQl0WKQaBtgkKbSlS/Dp8s/Xn1/7F4h7mFNrCtAs3pzsFeh6Hrn7yiBtbPhZ0G\nVsiBBhPAsVkkcDvBWc49DKx4dvPRHEQgqjCE6lxH2v2Xg2FOrEydzZbDV4sGkIY0\n5l23B/VaYATDyIM6RlhVf82eclMZhL0ui4ef01U5iQKBgQC+PV5vKrJlc6tdaB6m\n0oFRf3SeBpLoNLW5SiIDIhIBCmrfkKdTNCbm6C0CWpX+Bg7hvJIOwAAPlSysbZyx\neuIUKbYX4ujoJ1ws6KBs0Lnw40LaITZa+OBMa45IY/M6V6z/b+bhFREDaqiokt+O\nWvNbWh4QcACPFSRxdvlzBfkqCwKBgQC5sWdsn3Ek7CITsrL3UHdnAN8eJxftFkNr\nSj/VFl4qAy4JEb0gVdI2FGlE54p72WZUcqsPRhLJjsjB36+nRg/hMpwZZ9qqXngI\nBos2SejHTXMpfaPoyekzcH+ljZ2KhaE5YKh+WAYUgPnZ050zRqlEl8ASKWcm1uxm\nWdIPfEF+3QKBgAje87hbVVZFvofsgwFkb4NNXjLAO7l4O8EYI93hiNVjlvg11pea\npvW9fdvOPZBK2AbOtEDb0yTm395qfhQIluI5z7PtcM7ihvnRHynz0bfZ4RQq2E4F\nrO/jVA8sGftuezKuFSYJxXFTV+oEb0hEFXT9DsnVbzE82yYvVhJ3BNdhAoGBAJZf\n47FDLQ0JbE8nV2aP8yGmwwhYADgu30nzRt34zyiWiqEtjEqzNRg2T0lNeAfzdbrN\nYVltFanDxy+5RTXgtttXcLHiOGHfPrTBF9tO3wMG5UukQygw2nidkcEvfXS/4l/k\nto4aGlJgX/TWOWdcwZaajSAoBzCcu7Pm6QVBSojBAoGAYVExGWRjFKqbTUDksBL0\n9NP1Ln3+OeM+9BMFp0xTOtnIHXKSz3mvjwZ6ZJ+MtW7zEF8xj4+Xiv+dSYShUT/q\nfXHf2zE/y2AJxtkhFII+hZGVallF/606n2/1Qkpyqu6N5NxkGre1Jee1HX6eOLuD\nL2mG1UNxxJvJlfs33x9FJHc=\n-----END PRIVATE KEY-----\n",
  "client_email": "bigquery@refactored-waddle.iam.gserviceaccount.com",
  "client_id": "102290051536479478430",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bigquery%40refactored-waddle.iam.gserviceaccount.com"
},)
	client = bigquery.Client(project=project_id,credentials=credentials)
	destination = database + '.' +table
	pandas_gbq.to_gbq(df,destination_table = destination,project_id = project_id,credentials=credentials,if_exists='append')

#get_write_tweets('refactored_waddle','tweets','JetBlue','JetBlue')
#get_write_tweets('refactored_waddle','tweets','SouthwestAir','SouthwestAir')
