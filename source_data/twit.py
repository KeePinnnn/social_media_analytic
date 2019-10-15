from source_data import preprocess_data

import pandas as pd
import numpy as np

import twint

def verified_score():
    data = pd.read_csv('./author_dataset.csv')
    df = pd.DataFrame(data)
    df['username'] = df['username'].str.strip()
    df_keep = df.copy()
    df_keep['verified'] = df_keep['username']
    df.dropna(inplace=True)

    list_author = df['username'].unique().tolist()
    dict_author = {}

    for each in list_author:
        c = twint.Config()
        c.Username = each
        c.Pandas = True
        twint.run.Lookup(c)

        tweets_df = twint.output.panda.User_df

    tweets_df = tweets_df.drop_duplicates(subset='username', keep='last')
    dict_author = pd.Series(tweets_df.verified.values, index=tweets_df.username).to_dict()
    df_keep.replace({"verified":dict_author}, inplace=True)
    df_keep['verified'].fillna(0, inplace=True)

    df_keep.to_csv('./author_dataset.csv', index=False)

def user_tweet(username:str):
    try:
        c = twint.Config()
        c.Limit = 100
        c.Username = username
        c.Pandas = True
        twint.run.Search(c)

        tweets_df = twint.storage.panda.Tweets_df
        if len(tweets_df) > 50:
            list_tweets = tweets_df['tweet'].sample(n=50, random_state=42).tolist()
        else:
            list_tweets = tweets_df['tweet'].tolist()

        c = preprocess_data.clean_col()
        tlist = []
        for tweet in list_tweets:
            tlist.append(c.remove_emoji(tweet))
        return np.array(tlist)
    except:
        return 