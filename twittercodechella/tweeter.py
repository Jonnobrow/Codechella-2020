import sys
import tweepy
import json
 
#Autenticações
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# Where On Earth ID for Brazil is 23424768.
USA_WOE_ID = 2487956
 
brazil_trends = api.trends_place(USA_WOE_ID)
 
trends = json.loads(json.dumps(brazil_trends, indent=1))
 
for trend in trends[0]["trends"]:
	print (trend["name"])