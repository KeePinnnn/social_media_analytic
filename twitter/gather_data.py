import pandas as pd
import twint 

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
