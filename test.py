from source_data import model, twit

from functools import reduce

if __name__ == "__main__":
	print("start")
	embedding_model = model.embedding_model("./source_data/author_dataset.csv")
	embedding_model.feature_input()
	embedding_model.embedding_feature()
	embedding_model.model_setup()
	embedding_model.train_model()

	counter = 1
	user_cred = {}
	authors = embedding_model.df.copy()
	authors.dropna(inplace=True)
	embedding_model.df['user_credibility'] = embedding_model.df['username']
	authors = authors['username'].unique().tolist()
	for author in authors:
		cred_list = []
		tweets = twit.user_tweet(author)
		if tweets is not None:
			result = embedding_model.predict_model(tweets)
			for each in result:
				if int(each['classes'][0], 2) == 1:
					cred_list.append(each['probabilities'][0])
				else:
					cred_list.append(-each['probabilities'][0])

			user_cred[author] = reduce(lambda a, b: a + b, cred_list) / len(cred_list)	
		else:
			user_cred[author] = -5	
	
	print(user_cred)
	embedding_model.df.replace({"user_credibility":user_cred}, inplace=True)
	embedding_model.df['user_credibility'].fillna(-0.5, inplace=True)
	embedding_model.df.to_csv('./source_data/complete_dataset.csv', index=False)
	print("done")

	# print("start")
	# d = data.process_data()
	# d.read_file('./twitter/preprocess_data.csv')
	# score = d.df['average_vector'].tolist()

	# normalised_data = d.scale_data(score)
	# print(normalised_data)

	# d.update_data("average_vector", normalised_data)
	# d.save_file('./twitter/preprocess_data.csv')


	# print("start")
	# d = data.process_data()
	# d.read_file('./twitter/preprocess_data.csv')
	# tweets = d.df['tweet'].tolist()
	
	# corpus_df = d.df.loc[:, ['tweet', 'search']]

	# gmodel = text_analysis.text_vector(tweets)
	# print("done reading")

	# tf_idf_score = []
	# for index, row in corpus_df.iterrows():
	# 	print(f"inside {index}")
	# 	tf_idf_score.append(d.vector_feature(row))


	# sentence_vector = []
	# for index, twit in enumerate(tweets):
	# 	vector_list = []
	# 	print(f"currently finding {index}")
	# 	twit = twit.split()
	# 	words = [word for word in twit if word in gmodel.model.vocab]
	# 	for idx, word in enumerate(words):
	# 		vector = gmodel.model[word]
	# 		vector_list.append(vector)

	# 	sentence_vector.append((np.average(vector_list) * tf_idf_score[index]))

	# d.df['average_vector'] = sentence_vector
	# d.save_file('./twitter/preprocess_data.csv')
		


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

