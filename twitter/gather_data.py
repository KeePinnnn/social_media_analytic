from langdetect import detect

import pandas as pd
import goslate
import twint 
import re

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]

def gather_data():
    df_list = pd.DataFrame({})
    search_list = ["fake news", "politics", "world news", "cnn", "bbc", "gun laws", "brexit", "election", "impeachment", "south china sea", "missile", "real news", "rumors", "conspiracy", "policy"]

    for issues in search_list:
        c = twint.Config()

        c.Search = issues
        c.Limit = 1000
        c.Pandas = True

        twint.run.Search(c)
        df_pd = twint_to_pandas(["date", "username", "tweet", "hashtags", "nlikes", "link", "nreplies", "nretweets", "retweet", "search"])
        print(df_pd)
        if df_list.empty:
            df_list = df_pd
        else:
            df_list = df_list.append(df_pd, ignore_index=True)

    print(df_list)
    df_list.to_csv('./twitter_data.csv', encoding='utf-8', index=False)

def remove_dup():
    data = pd.read_csv('./twitter_data.csv', engine='python', encoding='utf-8')
    df = pd.DataFrame(data)

    df = df.drop_duplicates(subset='tweet', keep='last')
    df.to_csv('./twitter_data.csv', encoding='utf-8', index=False)

def read_file(file_path:str):
    data = pd.read_csv(file_path, engine='python', encoding='utf-8')
    return pd.DataFrame(data)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def clear_emoji():
    df = read_file('./twitter_data.csv')
    gs = goslate.Goslate()


    content_list = []
    content = df['tweet']
    counter = 1
    for each in content:
        print(f"currently inside {counter}")
        clean_tweet = remove_emoji(each)
        content_list.append(clean_tweet)

        counter += 1

    df.update(pd.DataFrame({'tweet': content_list}))
    df.to_csv('./twitter_data.csv', encoding='utf-8', index=False)


def split_en_data():
    df = read_file('./twitter_data.csv')

    en_list = []
    others_list = []

    for index, row in df.iterrows():
        print(f"currently inside {index}")
        try:
            if detect(row['tweet']) == "en":
                values = row.tolist()
                dict = {"date":[values[1]], "username":[values[2]], "tweet":[values[3]], "hashtags":[values[4]], "nlikes":[values[5]], "link":[values[6]], "nreplies":[values[7]], "nretweets":[values[8]], "retweet":[values[9]], "search":[values[10]]}
                en_list.append(pd.DataFrame.from_dict(dict))
            else:
                values = row.tolist()
                dict = {"date":[values[1]], "username":[values[2]], "tweet":[values[3]], "hashtags":[values[4]], "nlikes":[values[5]], "link":[values[6]], "nreplies":[values[7]], "nretweets":[values[8]], "retweet":[values[9]], "search":[values[10]]}
                others_list.append(pd.DataFrame.from_dict(dict))

        except:
            df = df.drop([index])
            print("drop")

    en_result = pd.concat(en_list, axis=0, ignore_index=True)
    others_result = pd.concat(others_list, axis=0, ignore_index=True)

    en_result.to_csv('./en_twitter_data.csv', encoding='utf-8', index=False)
    others_result.to_csv('./others_twitter_data.csv', encoding='utf-8', index=False)


df = read_file('./en_twitter_data.csv')
following_list = []
follower_list = []
likes_list = []

for index, row in df.iterrows():
    print(f"currently inside {index}")
    c = twint.Config()
    c.Username = row['username']
    c.Pandas = True

    twint.run.Lookup(c)

    user_df = twint.storage.panda.User_df

    print(user_df['following'])
    print(user_df['followers'])
    print(user_df['likes'])

    follower_list.append(user_df['followers'])
    following_list.append(user_df['following'])
    likes_list.append(user_df['likes'])

    twint.storage.panda.clean()

