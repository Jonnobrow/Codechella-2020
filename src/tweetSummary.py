#!/usr/bin/env python

import nltk
import re
import heapq
from typing import List

nltk.download('stopwords')
nltk.download('punkt')

class TweetSummariser:
    """
    Provides the necessary tool to summarise a set of tweets using
    natural language processing techniques.
    """

    def __init__(self, tweets: List[str]):
        self.tweets = tweets
        self.clean_tweets = {}
        self.stopwords = nltk.corpus.stopwords.words('english')

    def _preProcess(self):
        """
        Processes all tweets and removes anything that won't be useful (URLs, Emoji)
        """
        regex_pattern = re.compile(pattern = "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                                "]+", flags = re.UNICODE)
        for tweet in self.tweets:
            new_tweet = regex_pattern.sub(r'', tweet)
            new_tweet = re.sub(r'http\S+', '', new_tweet, flags=re.MULTILINE)
            new_tweet = new_tweet.replace('#', '')
            new_tweet = new_tweet.replace('RT', '')
            new_tweet = new_tweet.replace('@', '')
            self.clean_tweets[tweet] = new_tweet

    def _joinedTweets(self):
        """
        Combines preProcessed tweets together
        """
        return " ".join(self.clean_tweets.values())

    def _wordFrequencies(self):
        """
        Calculates the frequency of each word in the combined tweets
        """
        word_freq = {}
        for word in nltk.word_tokenize(self._joinedTweets()):
            if word not in self.stopwords:
                if word not in word_freq.keys():
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1

        max_freq = max(word_freq.values())

        # Scaling frequencies
        word_freq = {word: (word_freq[word]/max_freq) for word in word_freq.keys()}

        return word_freq

    def _tweetScores(self, word_frequencies):
        """
        Calculates a score for each tweet based on the words it contains
        """
        tweet_scores = {}
        for tweet in self.tweets:
            for word in nltk.word_tokenize(self.clean_tweets[tweet].lower()):
                if word in word_frequencies.keys():
                    if tweet not in tweet_scores.keys():
                        tweet_scores[tweet] = word_frequencies[word]
                    else:
                        tweet_scores[tweet] += word_frequencies[word]
        return tweet_scores

    def run_simple(self, summary_tweets: int):
        """
        Runs the processing and summary pipeline
        Returns a number of tweets that best represent the set provided
        """
        self._preProcess()
        freq = self._wordFrequencies()
        score = self._tweetScores(freq)
        return heapq.nlargest(summary_tweets, score, key=score.get)
