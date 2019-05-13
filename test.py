from google import api

if __name__ == "__main__":
	text = "Investing is a tool for building wealth, but it is not only for the wealthy. Anyone can get started on an investing program, and various vehicles make it easy to begin with small amounts and add to a portfolio periodically. "

	print(api.analyze_entity_sentiment(text))