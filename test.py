import numpy as np

from data_source import data
from nlp import text_analysis


if __name__ == "__main__":
	print("start")
	d = data.process_data()
	d.read_file('./twitter/preprocess_data.csv')
	tweets = d.df['tweet'].tolist()
	
	corpus_df = d.df.loc[:, ['tweet', 'search']]

	tf_idf_score = []
	for index, row in corpus_df.iterrows():
		print(f"inside {index}")
		tf_idf_score.append(d.vector_feature(row))

	gmodel = text_analysis.text_vector(tweets)
	print("done reading")

	vector_list = []
	for twit in tweets:
		twit = twit.split()
		words = [word for word in twit if word in gmodel.model.vocab]
		twit = ' '.join(words)
		vector = gmodel.model[twit]
		vector_list.append(vector)

	sentence_vector = []
	for x in range(len(vector_list)):
		sentence_vector.append(np.average(vector_list[x] * tf_idf_score[x]))
		print(sentence_vector)



	# normalize_corpus = np.vectorize(d.normalize_document)
	# norm_corpus = normalize_corpus(tweets)
	# print(len(norm_corpus))


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

