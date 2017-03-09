import tweepy
from tweepy import OAuthHandler
import pandas as pd
import os

def read_credentials():
    path = os.path.expanduser('~/Google Drive/Credentials/Twitter.pkl')
    secrets_pickle = pd.read_pickle(path)
    secrets = secrets_pickle.to_dict()

    auth = OAuthHandler(consumer_key=secrets['consumer_key'], consumer_secret=secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])

    api = tweepy.API(auth)

    return api

api = read_credentials()

def read_tweets(api):
    account_tweets = api.user_timeline('realdonaldtrump', count=200)

    source = {}
    content = {}
    time = {}
    for i, tweet in enumerate(account_tweets):
        source[i] = tweet.source
        content[i] = tweet.text
        time[i] = tweet.created_at


    df = pd.DataFrame({'Source': pd.Series(source),
                       'Content': pd.Series(content),
                       'DateTime' : pd.Series(time)})

    return df

read_tweets(api)