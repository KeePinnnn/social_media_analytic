from twitter.twitter_info import twitter
from controller.google_controller import GoogleController

class twit_controller():
    def __init__(self, username:str, limit:int):
        self.google = GoogleController()

    def get_followings(self):
        following = self.twitter.get_following()
        print(following)

    def get_followers(self):
        followers = self.twitter.get_followers()
        print(followers)

    def get_twit_info(self):
        tweets = self.twitter.get_tweets()
        print(tweets)
        for each_twit in tweets['details']:
            socre = self.google.get_score(each_twit.twit)

