# Importing packages

import os
import tweepy as tw
import pandas as pd

# Twitter API keys

CONSUMER_KEY = "0S2DFi9Sk5JXPYSFXJnWnRIq1"
CONSUMER_SECRET = "faBTAtMKluJzXV2cocuswK48T1HwLpJbHh2emOS1czrHKHOguP"
ACCESS_TOKEN = "1090100931713216515-Ho1UMeX8cgH0jT47ruU89Ulm5XhTcW"
ACCESS_SECRET = "FYcqabspVmqanZwJ6SnT1ezIBUzxiimQaydQAEUNcsdf3"

# Authentication 

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

# Data to collect

users = ["Mercadolibre", "ML_Argentina", "ML_Mexico", "ML_Venezuela", "ML_Ayuda"]

# Collecting tweets

for userID in users:

    tweets = api.user_timeline(screen_name=userID,
                            count=200,
                            include_rts=False,
                            exclude_replies=True,
                            tweet_mode="extended"
                            )

    # Features

    for info in tweets[0:3]:
        print(info.user.screen_name)
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")

    # Max tweets possible to collect

    all_tweets = []
    all_tweets.extend(tweets)
    oldest_id = tweets[-1].id
    while True:
        tweets = api.user_timeline(screen_name=userID, 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            max_id = oldest_id - 1,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)
        print('N of tweets downloaded till now {}'.format(len(all_tweets)))

    # Saving tweets as CSV file

    from pandas import DataFrame
    outtweets = [[tweet.id_str, 
                tweet.created_at, 
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(all_tweets)]
    df = DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
    df.to_csv('%s_tweets.csv' % userID,index=False)
