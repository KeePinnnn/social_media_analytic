import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)

from config import *
import requests
import json

'''
	able to analyse the given input and allow user to understand the semantics of the given text
	return a json of analysed result with magnitude and score
		magnitude represents the emotion of the sentence
		score is the total value of magnitude from the sentence
'''
def analyze_sentiment(text:str) -> json:
	url = google_url + google_variants['sentiment']
	key = API_KEY

	data = {
			"document":
				{
					"type": "PLAIN_TEXT",
					"content": text
				}
			}
	
	print("starting here")
	r = requests.post(url + "?key=" + API_KEY, headers={"Content-Type": "application/json"}, data=json.dumps(data))
	return r.text

'''
	able to analyse the given content and return the context of the given information
	return a json of analyse result with salience
		salience represent the relevant of the entity to the entire given information
'''
def analyze_entity_sentiment(text:str) -> json:
	url = google_url + google_variants['entityS']
	key = API_KEY

	data = {
			"document":
				{
					"type": "PLAIN_TEXT",
					"content": text
				}
			}
	
	print("starting here")
	print("\n\n\n\n")
	r = requests.post(url + "?key=" + API_KEY, headers={"Content-Type": "application/json"}, data=json.dumps(data))
	return r.text

if __name__ == "__main__":
	text = "Leading companies rely on our container platform to build, manage and secure all their applications from traditional applications to cutting-edge microservices — and deploy them anywhere."

	print(json.loads(analyze_sentiment(text)))
	print(json.loads(analyze_entity_sentiment(text)))
