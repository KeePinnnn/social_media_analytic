# -*- coding: utf-8 -*-

from source_data import model, twit
import matplotlib.pyplot as plt
import numpy as np

from functools import reduce

import sys

def demo(username:str, content:str):
	print("start")
	print(username)
	verified = twit.user_verified(username)
	embedding_model = model.embedding_model("./source_data/author_dataset.csv")
	embedding_model.embedding_feature()
	embedding_model.restore_saved_model()

	cred_list = []
	tweets = twit.user_tweet(username)
	if tweets is not None:
		result = embedding_model.predict_model(tweets)
		for each in result:
			if int(each['classes'][0], 2) == 1:
				cred_list.append(each['probabilities'][0])
			else:
				cred_list.append(-each['probabilities'][0])

	cred_score = reduce(lambda a, b: a + b, cred_list) / len(cred_list)	
	
	dnn_model = model.dnn_model("./source_data/complete_dataset.csv")
	dnn_model.embedding_feature()
	dnn_model.restore_saved_model()
	result = dnn_model.predict_model([content], [verified], [cred_score])
	for each in result:
		label = int(each['classes'][0], 2)
		proabilities = each['probabilities'][0]

	if label == 1:
		file = open('result.txt', 'w+')
		file.writelines([str(0.5 + (proabilities*0.5))])
	else:
		file = open('result.txt', 'w+')
		file.writelines([str(proabilities*0.5)])

def get_user_credibility_score():
	print("start")
	embedding_model = model.embedding_model("./source_data/author_dataset.csv")
	embedding_model.feature_input()
	embedding_model.embedding_feature()
	embedding_model.model_setup()
	embedding_model.train_model()

	counter = 1
	user_cred = {}
	plt_list = []
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
			plt_list.append(reduce(lambda a, b: a + b, cred_list) / len(cred_list))
		else:
			user_cred[author] = -0.5	
			plt_list.append(-0.5)

	
	plt.hist(plt_list, bins=0.2)
	
	# embedding_model.df.replace({"user_credibility":user_cred}, inplace=True)
	# embedding_model.df['user_credibility'].fillna(-0.5, inplace=True)
	# embedding_model.df.to_csv('./source_data/complete_dataset.csv', index=False)



if __name__ == "__main__":
	demo(sys.argv[1], sys.argv[2])
	# get_user_credibility_score()
	# print("start")
	# embedding_model = model.embedding_model("./source_data/complete_dataset.csv")
	# embedding_model.feature_input()
	# embedding_model.embedding_feature()
	# embedding_model.model_setup()
	# embedding_model.train_model()

	# dnn_model = model.dnn_model("./source_data/complete_dataset.csv")
	# dnn_model.feature_input()
	# dnn_model.embedding_feature()
	# dnn_model.model_setup()
	# dnn_model.train_model()
	# dnn_model.test_model()

	# user_cred = []
	# username = ['ChannelNewsAsia', 'STcom', 'benni1028', 'realDonaldTrump', 'axanner']
	# cred = [1.0, 1.0, 0.0, 1.0, 0.0]
	# content = [
	# 	"Nine killed in fresh firing across Kashmir border https://cna.asia/2Mx2rd1 ",
	# 	"How Catalan protest tactics are inspired by Hong Kong",
	# 	"What Republicans neglect to look at, is that the defense aid to Ukraine was already being held up when that phone call took place. It took place a week before the July 25th phone call. Now imagine you are a country that really needs that aid, are depending on that aid to defend",
	# 	"So now Crooked Hillary is at it again! She is calling Congresswoman Tulsi Gabbard “a Russian favorite,” and Jill Stein “a Russian asset.” As you may have heard, I was called a big Russia lover also (actually, I do like Russian people. I like all people!). Hillary’s gone Crazy!",
	# 	"According to MDN, the Isra & Mi’raj journey of the prophet is a folk story. They are rejecting something which is clearly mentioned in the Quran. @ShimranAb why are you still allowing this NGO to operate in Maldives? #BanMDN"
	# ]
	# print("hereeeeeeeeee")
	# for index, each in enumerate(username):
	# 	cred_list = []
	# 	tweets = twit.user_tweet(each)
	# 	if tweets is not None:
	# 		result = embedding_model.predict_model(tweets)
	# 		for each in result:
	# 			if int(each['classes'][0], 2) == 1:
	# 				cred_list.append(each['probabilities'][0])
	# 			else:
	# 				cred_list.append(-each['probabilities'][0])

	# 		user_cred.append(reduce(lambda a, b: a + b, cred_list) / len(cred_list))

	# result = dnn_model.predict_model(content, cred, user_cred)
	# for each in result:
	# 	print(each)

