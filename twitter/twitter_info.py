import json

import twint 

class twitter():
    def __init__(self, username:str, limit:int):
        self.username = username
        self.limit = limit

    def set_username(self, username:str):
        self.username = username

    def get_username(self) -> str:
        return self.username

    def set_limit(self, limit:int):
        self.limit = limit

    def get_limit(self):
        return self.limit

    def get_tweets(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = self.limit
        c.Store_object = True

        twint.run.Search(c)
        tweets = twint.output.tweets_object
        return tweets

    def get_followers(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = self.limit
        c.Store_object = True

        twint.run.Followers(c)
        followers = twint.output.follow_object
        return followers

    def get_following(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = self.limit
        c.Store_object = True
        c.User_full = True

        twint.run.Followers(c)
        users = twint.output.user_object
        return users

    def tweet_details(self, tweets:list) -> json:   
        tweet_info = {
            "username" : self.username,
            "details" : []
        }
        sub_tweet = {}

        for tweet in tweets:
            sub_tweet = {
                "id" : tweet.id,
                "twit" : tweet.tweet,
                "mention" : tweet.mentions,
                "num_likes" : tweet.likes_count,
                "num_retweet" : tweet.retweets_count,
                "url" : tweet.urls,
                "location" : tweet.location,
                "photo" : tweet.photos,
                "video" : tweet.video,
                "type" : tweet.type
            }
            tweet_info['details'].append(sub_tweet)
        
        return tweet_info

    def following_details(self, following:list) -> json:
        following_info = {
            "username": self.username,
            "details": []
        }
        sub_follow = {}

        for individual in following:
            sub_follow = {
                "id" : individual.id,
                "name" : individual.name,
                "username" : individual.username,
                "followers" : individual.followers,
                "following" : individual.following,
                "private" : True if individual.is_private else False,
                "verified" : True if individual.is_verified else False,
                "likes" : individual.likes,
                "location" : individual.location,
                "media_count" : individual.media_count,
                "num_tweets" : individual.tweets,
                "type" : individual.type,
                "url" : individual.url
            }
            following_info['details'].append(sub_follow)

        return following_info