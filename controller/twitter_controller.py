from twitter.twitter_info import twitter

class twit_controller():
    def __init__(self, username:str, limit:int):
        self.twitter = twitter(username, limit)

    def get_followings(self):
        following = self.twitter.get_following()
        print(following)

    def get_followers(self):
        followers = self.twitter.get_followers()
        print(followers)

    def get_twit_info(self):
        tweets = self.twitter.get_tweets()
        print(tweets)
        for twit in tweets['details']:

