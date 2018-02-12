import tweepy
from time import sleep
from creds import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Change #hashtag to suite your search criteria
for tweet in tweepy.Cursor(api.search, q='#hashtag').items():
    try:
        # Add \n escape character to print() to organize tweets
        # Prints out the twitter name of most recent hashtag use
        print('\nTweet by: @' + tweet.user.screen_name)

        #Retweets as found
        tweet.retweet()
        print('Retweeted the tweet')
        
        # Based on seconds, currently set at 1 hour
        sleep(3600)

    except tweepy.TweepError as e:
        print(e.reason)
