# \#Codechella 2020

See more about Codechella [here (Twitter)](https://twitter.com/hashtag/codechella?lang=en) and [here (Devpost)](https://codechella.devpost.com/).

1. 😺 [The Team](#-the-team)
2. 📋 [About the Project](#-about-the-project)
3. 🔒 [Secrets (API Keys etc)](#-secrets-api-keys-etc)
4. 🏃 [Running the Project](#-running-the-project)

## 😺 The Team

- Jonathan Bartlett ([GitHub](https://github.com/Jonnobrow) | [Twitter](https://twitter.com/jonnobrow))
- Akhil Nair ([GitHub](https://github.com/Jedi18) | [Twitter]())
- Abel Fikreyohanes ([GitHub](https://github.com/bellajr) | [Twitter](https://twitter.com/AFikreyohanes))
- Shivam Soni ([GitHub](https://github.com/i-shivamsoni) | [Twitter](https://twitter.com/i_shivamsoni))
- Shreehari Vaasistha ([GitHub](https://github.com/ShreehariVaasishta) | [Twitter](https://twitter.com/Hary86389970))

## 📋 About the Project

After brainstorming ideas, we decided unanimously on a Smart Assistant application that would allow
users to interact with Twitter in a meaningful way. Current offerings for Twitter "skills" on Amazon
Alexa are limited in what they can do and are rated poorly on the store. 

Therefore we decide to create a skill, and the supporting API, to allow users to do the following:
- Get a summary of tweets in a Hashtag
- Get the latest tweets from a User
- Follow a user
- Get the topics trending in your area

### How it applied to '\#BuildWithTwitter'

We are using the [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/early-access) to:
- Get Tweets based on a Hashtag
- Get Tweets from a user
- Follow a user
- Get trending topics

### How it applies to 'Twitter for Everyone'

This smart assistant application will hopefully open up Twitter to a whole new demographic.
People with visual impairments may struggle when using Twitter on a conventional mobile app or website.
A smart assistant allows users to interact with Twitter purely through voice and we wanted to implement
features we feel are key to the Twitter experience.

### Project Structure

``` text
.
+-- .gitignore               # Ignore secrets, venv, lock files etc
+-- README.md
+-- requirements.txt         # Project Requirements
+-- lambda
|   +-- lambda-function.py   # Handler for lambda functions
|   +-- twitter_functions.py # Helper functions for interacting with twitter API
|   +-- tweet_summary.py     # Tweet summarizer
+-- interactionModels
|   +-- custom
|   |   +-- en-US.json       # Interaction model for the Alex Skill
```

### List of Required Secrets and Expected Names

| Name                | Value                                               |
|---------------------|-----------------------------------------------------|
| API_KEY             | The Twitter API Key for the project                 |
| API_SECRET          | The Twitter API Secret for the project              |
| ACCESS_TOKEN        | The Twitter App Access Token for the project        |
| ACESSS_TOKEN_SECRET | The Twitter App Access Token Secret for the project |

A sample environment file exists at `.env.sample` you should source this file
when running the serverless deployment.

## 🏃 Running the Project

### Alexa Skill

1. Create a new Alexa Skill from the Alexa Skills Dashboard
	- Make sure to choose the option to provision your own!
2. Copy the interactModel json in the json editor on the Alexa Skills Dashboard
3. Build the model

### Lambda Function

1. Source your environment file with the required environment variables
2. Make sure you have serverless installed and aws credentials configured
3. Run `npm install` to install serverless plugins
4. Run `serverless deploy` to deploy the lambda function

### Joining the dots

1. Copy the ARN for the twitter digest lambda function
2. Paste the ARN into the Endpoints field on the Alexa Skills Dashboard
3. Enjoy!





