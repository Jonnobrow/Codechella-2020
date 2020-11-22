import sys
import tweepy
import json
 
#Autenticações
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# Where On Earth ID for Brazil is 23424768.
def trends():
    USA_WOE_ID = 2487956
 
    us_trends = api.trends_place(USA_WOE_ID)
 
    trends = json.loads(json.dumps(us_trends, indent=1))
    return trends

