import twint 

class twitter():
    def __init__(self, username:str):
        self.username = username

    def get_tweets(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = 1
        c.Store_object = True

        twint.run.Search(c)
        tweets = twint.output.tweets_object
        return tweets

    def get_followers(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = 1
        c.Store_object = True

        twint.run.Followers(c)
        followers = twint.output.follow_object
        return followers

    def get_following(self) -> list:
        c = twint.Config()
        c.Username = self.username
        c.Limit = 1
        c.Store_object = True
        c.User_full = True

        twint.run.Followers(c)
        users = twint.output.user_object
        return users