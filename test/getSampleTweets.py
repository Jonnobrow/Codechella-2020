#!/usr/bin/env python

import tweepy
import os
import sys
from src.tweetSummary import TweetSummariser


api_key = os.getenv("API_KEY", "")
api_secret = os.getenv("API_SECRET", "")
access_token = os.getenv("ACCESS_TOKEN", "")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET", "")

print(api_key)
if (api_key == "" or
    api_secret == "" or
    access_token == "" or
    access_token_secret == ""):
    print("Check your secrets, something isn't right!")
    sys.exit(1)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search("#Codechella", result_type="mixed", count="250", include_entities=False)
tweets = []
for tweet in results:
    tweets.append(tweet.text)

summariser = TweetSummariser(tweets)
result = summariser.run()
for tweet in result:
    print(tweet)
