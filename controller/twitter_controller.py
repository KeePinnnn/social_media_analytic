from twitter.twitter_info import twitter

class twit_controller():
    def __init__(self, username:str, limit:int):
        self.twitter = twitter(username, limit)

    def get_info(self):
        tweets = self.twitter.get_tweets()
        followers = self.twitter.get_followers()
        following = self.twitter.get_following()