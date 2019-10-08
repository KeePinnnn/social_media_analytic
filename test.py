import numpy as np

from data_source import data
from nlp import text_analysis


if __name__ == "__main__":
	


	# d = data.process_data()
	# modal = text_analysis.text_modality()
	# d.read_file('./twitter/clean_en_data.csv')
	# d.df.dropna(subset=['tweet'], inplace=True)
	# content = d.df['tweet'].tolist()
	# counter = 1

	# modality_list = []
	# polarity_list = []
	# subjectivity_list = []

	# for twit in content:
	# 	t = text_analysis.text_blob(twit)
	# 	score = t.get_sentiment()
	# 	polarity_list.append(score[0])
	# 	subjectivity_list.append(score[1])
	# 	modality_list.append(modal.get_score(twit))
	# 	print(f"counter is at {counter}")
	# 	counter += 1
	
	# d.df['polarity_score'] = polarity_list
	# d.df['subjectivity_score'] = subjectivity_list
	# d.df['modality_score'] = modality_list

	# d.save_file('./twitter/preprocess_data.csv')
	# print("done")
		


	# d = data.process_data()
	# counter = 1
	# d.read_file('./twitter/en_twitter_data.csv')	
	# content = d.df['tweet']

	# print(f"file number is {counter}")
	# d.clean_data(content)
	# print(f"file number is {counter}")
	# d.save_data("tweet", './twitter/clean_en_data.csv')

