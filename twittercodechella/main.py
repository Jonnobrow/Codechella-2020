import datetime
import re
import azure.cognitiveservices.speech as speechsdk
import tweeter
import tweepy as tw
import url_parser

speech_key, service_region = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

def speak(text):
    result = speech_synthesizer.speak_text_async(text).get()
    return None


def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        grt = "Good Morning"
        print("Good Morning")
    elif hour >= 12 and hour < 18 :
        grt = "Good Afternoon"
        print("Good Afternoon")   
    else:
        grt = "Good Evening"
        print("Good Evening")
    text = (f'Hello {grt}! I am Dora, your twitter digest assistant. what can i help you with?')

    result = speech_synthesizer.speak_text_async(text).get()
    return None


def take_command():
    
    try:
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        print("speak to your microphone")
        result = speech_recognizer.recognize_once_async().get()
    except Exception as e:
        ex = f'pardon me! i can\'t hear that can you say it again'
        exc = speech_synthesizer.speak_text_async(ex).get()

    return result.text

def hashtagmanipulation(statement):
    i = 0
    while i < len(statement):
        if statement[i] == "#":
            i+=1
            new_str = statement[i:]
            break
        i += 1       
    res = new_str
    return res

def twitter_strings(sentence):
    sentence = sentence.replace(".", "")
    sentence = sentence.replace("?", "")
    sentence = sentence.replace("\"", "")
    sentence = sentence.replace("\'", "")
    sentence = sentence.replace(",", "")

    sentence = sentence.replace("symbol dot", ".")
    sentence = sentence.replace("symbol underscore", "_")
    sentence = sentence.replace("symbol dash", "-")
    sentence = sentence.replace("symbol open bracket", "(")
    sentence = sentence.replace("symbol close bracket", ")")
    sentence = sentence.replace("symbol open curly brace", "{")
    sentence = sentence.replace("symbol close curly brace", "}")
    sentence = sentence.replace("symbol and", "&")
    sentence = sentence.replace("symbol star", "*")

    sentence = sentence.replace(" ", "")
    return sentence

def sanitize(mystring):
  for word in mystring.split(" "):
    if url_parser.valid_url(word):
      mystring = mystring.replace(word, url_parser.get_title(word))
  return mystring
greet()   

if __name__ == "__main__":
    while True:
        statement = take_command().lower()
        print(statement)
        if "bye" in statement or "goodbye" in statement or "stop" in statement:
            speak("ok bye! nice to find you here.")
            break

        elif "hashtag" in statement or "#" in statement :
            my_string = statement
            if "hashtag" in statement:
                keyword = "hashtag"
                before, keyword, after = my_string.partition(keyword)
                result = after 
                speak(f'okay i will gonna grab you the hashtag tweets of {result}')
                new = twitter_strings(result)
                print(f'#{new}')
            else:
                result = hashtagmanipulation(statement)
                speak(f'okay i will gonna grab you the hashtag tweets of {result}')
                new = twitter_strings(result)
                print(f'#{new}')

        elif "tweets of" in statement or "twits of" in statement:
            my_string = statement
            keyword = "tweets of"
            before, keyword, after = my_string.partition(keyword)
            handle = twitter_strings(after)
            speak("how many?")
            res = take_command()
            res = twitter_strings(res)
            i = int(res)
            print(f'@{handle}')
            speak(f'okay i will get you the tweets of {after}')
            print(f'okay i will get you the tweets of {after}')
            user = api.get_user(handle)
            tweets = api.user_timeline(screen_name = handle)
            
            if len(tweets) == 0:
                speak("the user have no tweets")
                print("the user have no tweets")
            if len(tweets) < i:
                i = len(tweets)
            for status in api.user_timeline(screen_name = handle):
                if i < 1:
                    break
                speak(f'@{handle} tweets {status.text}')
                print(f'@{handle} tweets {status.text}')
                i -= 1    

            

        elif "follow" in statement:
            my_string = statement
            keyword = "follow"
            before, keyword, after = my_string.partition(keyword)
            handle = twitter_strings(after)
            print(f'@{handle}')

            speak(f'you are following {after} now.')
            print(f'you are following {after} now.')


        elif  "trending topics" in statement:
            speak(f'the top trending topics are ')
            print(f'the top trending topics are ')
            i = 0
            for trend in tweeter.trends()[0]["trends"]:
                if i > 5:
                    break
                speak((trend["name"]))
                print((trend["name"]))
                i+=1

        elif "shuffle tweets" in statement or "shuffle twits" in statement:
            speak("how many?")
            print("how many?")
            res = take_command()
            res = twitter_strings(res)
            tweets = api.home_timeline()
            i = int(res)
            for tweet in tweets:
                if i < 1:
                    break 
                speak(f'{tweet.author.name} said {tweet.text}')
                print(f'{tweet.author.name} said {tweet.text}')
                i -= 1

        elif "my tweets" in statement or "my twits" in statement:
            speak("how many?")
            res = take_command()
            res = twitter_strings(res)
            i = int(res)
            my_tweets = api.user_timeline()
            if len(my_tweets) == 0:
                speak("you have no tweets")
                print("you have no tweets")
            if len(my_tweets) < i:
                i = len(my_tweets)
            for t in my_tweets:
                if i < 1:
                    break
                speak(t.text)
                print(t.text)
                i -= 1
