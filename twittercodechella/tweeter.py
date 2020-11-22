import sys
import tweepy
import json
 
#Autenticações
consumer_key = 'e1Ia7xomgdP0RjgcFctPg3JYF'
consumer_secret = 'IbakqM9mUBKuBUDi3lY9yQfcVMS6mZm4TuVXeQdPqdfKgt90St'
access_token = '1039977391836278784-63Q8XNrMazn1LA4sEXkSZAlNO3QjyZ'
access_token_secret = 'qt1fs9XkvxL4zaorxY4ENucuOhEFyJt1UXStvvKIYigxA'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# Where On Earth ID for Brazil is 23424768.
def trends():
    USA_WOE_ID = 2487956
 
    us_trends = api.trends_place(USA_WOE_ID)
 
    trends = json.loads(json.dumps(us_trends, indent=1))
    return trends

