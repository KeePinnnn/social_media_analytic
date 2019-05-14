from controller.api_controller import GoogleController
from twitter.profile_information import twitter

if __name__ == "__main__":
	# G = GoogleController()
	# text = "Investing is a tool for building wealth ah, but it is not only for the wealthy la. Anyone can get started on an investing program, and various vehicles make it easy to begin with small amounts and add to a portfolio periodically. "

	# print(G.get_score(text))

	t = twitter("johnculberson")
	# t.get_tweets()
	# t.get_followers()
	t.get_following()
