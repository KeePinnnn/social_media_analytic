from controller.api_controller import GoogleController
from controller.twitter_controller import twit_controller

if __name__ == "__main__":
	# G = GoogleController()
	# text = "Investing is a tool for building wealth ah, but it is not only for the wealthy la. Anyone can get started on an investing program, and various vehicles make it easy to begin with small amounts and add to a portfolio periodically. "

	# print(G.get_score(text))

	twit = twit_controller("johnculberson", 10)
	twit.get_info()
