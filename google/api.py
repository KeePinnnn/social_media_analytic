import json

import requests

from config import API_KEY, GOOGLE_URL, GOOGLE_VARIANT


class GoogleInfor():
	def __init__(self, text:str):
		self.text = text

	def set_text(self, text:str):
		self.text = text

	def get_text(self):
		return self.text

	def analyze_sentiment(self) -> json:
		'''
		able to analyse the given input and allow user to understand the semantics of the given text
		return a json of analysed result with magnitude and score
			magnitude represents the emotion of the sentence
			score is the total value of magnitude from the sentence
		'''

		url = GOOGLE_URL + GOOGLE_VARIANT['sentiment']
		key = API_KEY

		data = {
				"document":
					{
						"type": "PLAIN_TEXT",
						"content": self.text
					}
				}
		
		r = requests.post(url + "?key=" + API_KEY, headers={"Content-Type": "application/json"}, data=json.dumps(data))
		return json.loads(r.text)
	
	def analyze_entity_sentiment(self) -> json:
		'''
		able to analyse the given content and return the context of the given information
		return a json of analyse result with salience
			salience represent the relevant of the entity to the entire given information
		'''

		url = GOOGLE_URL + GOOGLE_VARIANT['entityS']
		key = API_KEY

		data = {
				"document":
					{
						"type": "PLAIN_TEXT",
						"content": self.text
					}
				}
		
		r = requests.post(url + "?key=" + API_KEY, headers={"Content-Type": "application/json"}, data=json.dumps(data))
		return json.loads(r.text)
