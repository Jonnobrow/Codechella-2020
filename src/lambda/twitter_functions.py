import tweepy

class TwitterFunctions():
    def __init__(self):
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def getTweetsFromUser(self, username):
        user = self.api.get_user(username)
        latest_tweets = [status.text for status in self.api.user_timeline(screen_name=user.screen_name, count=5)]
        return latest_tweets