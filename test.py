from source_data import model, twit

from functools import reduce

def get_user_credibility_score():
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
	
	embedding_model.df.replace({"user_credibility":user_cred}, inplace=True)
	embedding_model.df['user_credibility'].fillna(-0.5, inplace=True)
	embedding_model.df.to_csv('./source_data/complete_dataset.csv', index=False)



if __name__ == "__main__":
	get_user_credibility_score()

