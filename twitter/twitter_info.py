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