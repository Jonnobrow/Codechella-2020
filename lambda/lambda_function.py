# -*- coding: utf-8 -*-

# Lambda function file for our CodeChella project Twitter Digest.
# Contains all the request handlers for the intent
# TweetsFromUserIntentHandler : Handles the getting of tweet from the user
# TrendingTopicsIntentHandler : Handles the getting of trending topics

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from twitter_functions import TwitterFunctions
from tweet_summary import TweetSummariser

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to twitter digest"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class TweetsFromUserIntentHandler(AbstractRequestHandler):
    """Handler for Tweets From User Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TweetsFromUserIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        twitterUsername = handler_input.request_envelope.request.intent.slots['username'].value
        twitterFuncs = TwitterFunctions()
        latest_tweets = twitterFuncs.getTweetsFromUser(twitterUsername)
        speak_output = "Printing latest tweets from {}\n".format(twitterUsername)
        for tweet in latest_tweets:
            speak_output = speak_output + tweet + '\n'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class TrendingTopicsIntentHandler(AbstractRequestHandler):
    """Handler for Trending Topics Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TrendingTopicsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        twitterFuncs = TwitterFunctions()
        trending_topics = twitterFuncs.getTrendingTopics()
        speak_output = "Current trending topics :"
        for topic in trending_topics:
            speak_output = speak_output + ' ' + topic

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class TweetSummarizationIntentHandler(AbstractRequestHandler):
    """Handler for tweet summarization intent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TweetSummarizationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        topic = handler_input.request_envelope.request.intent.slots['topic'].value
        twitterFuncs = TwitterFunctions()
        topicTweets = twitterFuncs.getTopicTweets(topic)
        tweetSummariser = TweetSummariser(topicTweets)
        summarizedTweets = tweetSummariser.run_simple(3)
        speak_output = "Summary of tweets for {}\n".format(topic)
        for tweet in summarizedTweets:
            speak_output = speak_output + tweet + '\n'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FollowUserIntentHandler(AbstractRequestHandler):
    """Handler for Tweets From User Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FollowUserIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        twitterUsername = handler_input.request_envelope.request.intent.slots['username'].value
        twitterFuncs = TwitterFunctions()
        follow_user = twitterFuncs.followUser(twitterUsername)
        speak_output = "Following {}".format(twitterUsername)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TweetsFromUserIntentHandler())
sb.add_request_handler(TrendingTopicsIntentHandler())
sb.add_request_handler(TweetSummarizationIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
