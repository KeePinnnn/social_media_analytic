from twitter.twitter_info import twitter

class twit_controller():
    def __init__(self, username:str, limit:int):
        self.twitter = twitter(username, limit)

    def get_info(self):
        # tweets = self.twitter.get_tweets()
        # print(tweets)
        # tweets_information = self.twitter.tweet_details(tweets)
        # print(tweets_information)
        # followers = self.twitter.get_followers()
        following = self.twitter.get_following()
        print(following)
        following_information = self.twitter.following_details(following)
        print(following_information)