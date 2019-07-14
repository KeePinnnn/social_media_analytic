from functools import reduce
import json

import requests

from config import API_KEY, GOOGLE_URL, GOOGLE_VARIANT


class GoogleInfor():
	def __init__(self):
		self.key = API_KEY
		self.url = GOOGLE_URL
		self.singlish = [" la", " hor", " eh", " liao", " ah"]

	def set_text(self, text:str):
		text = reduce(lambda a,b: a.replace(b, ''), self.singlish, text)
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

		url = self.url + GOOGLE_VARIANT['sentiment']
		key = self.key

		data = {
				"document":
					{
						"type": "PLAIN_TEXT",
						"content": self.text
					}
				}
		
		r = requests.post(url + "?key=" + self.key, headers={"Content-Type": "application/json"}, data=json.dumps(data))
		return json.loads(r.text)
	
	def analyze_entity_sentiment(self) -> json:
		'''
		able to analyse the given content and return the context of the given information
		return a json of analyse result with salience
			salience represent the relevant of the entity to the entire given information
		'''

		url = self.url + GOOGLE_VARIANT['entityS']
		key = self.key

		data = {
				"document":
					{
						"type": "PLAIN_TEXT",
						"content": self.text
					}
				}
		
		r = requests.post(url + "?key=" + self.key, headers={"Content-Type": "application/json"}, data=json.dumps(data))
		return json.loads(r.text)
