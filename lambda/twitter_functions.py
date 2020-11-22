# TwitterFunctions class contains twitter API related functions
# Called by request handlers of intents in lambda_function

import tweepy
import os

class TwitterFunctions():
    def __init__(self):
        auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"))
        auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
        self.api = tweepy.API(auth)

    def getTweetsFromUser(self, username):
        user = self.api.get_user(username)
        latest_tweets = [status.text for status in self.api.user_timeline(screen_name=user.screen_name, count=5)]
        return latest_tweets

    def getTrendingTopics(self):
        # WID 1 for global trends
        trends = self.api.trends_place(id=1)
        result = []
        for value in trends:
            for trend in value['trends']:
                result.append(trend['name'])
                
        return result

    def getTopicTweets(self, topic):
        topic.replace('hashtag', '#')
        if topic[0] == '#':
            return [status.text for status in self.api.search(topic)]
        else:
            return [status.text for status in self.api.search('#' + topic)]

    def followUser(self, username):
        try:
            user = self.api.get_user(username)
            user.create_friendship(screen_name=user.screen_name)
            return True
        except Exception as e:
            return False
