import numpy as np

from data_source import data
from nlp import text_analysis


if __name__ == "__main__":
	d = data.process_data()
	counter = 1
	# while counter < 5:
	d.read_file('./twitter/en_twitter_data.csv')	
	content = d.df['tweet']

	print(f"file number is {counter}")
	d.clean_data(content)
	print(f"file number is {counter}")
	d.save_data("tweet", './twitter/clean_en_data.csv')

		# t = text_analysis.scikit(content)

		# x = []
		# for doc in content:
		# 	x.append(t.document_vector(doc))

		# z = np.array(x)
		# t.t_sne(z)
		# t.scatter_plot()

