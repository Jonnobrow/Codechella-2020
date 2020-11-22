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
        latest_tweets = [status.full_text for status in self.api.user_timeline(screen_name=user.screen_name, count=5, tweet_mode='extended')]
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
        topic.replace('hashtag', '#').strip()
        if topic[0] == '#':
            return [status.full_text for status in self.api.search(topic, tweet_mode='extended', count=300)]
        else:
            return [status.full_text for status in self.api.search('#' + topic, tweet_mode='extended', count=300)]

if __name__=="__main__":
    fun = TwitterFunctions()
    print(fun.getTrendingTopics())
