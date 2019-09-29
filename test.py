import numpy as np

from data_source import data
from nlp import text_analysis


if __name__ == "__main__":
	d = data.process_data()
	counter = 1
	# while counter < 5:
	d.read_file(f'./data_source/after_drop_data/sample_data.csv')	
	content = d.df['content']

	print(f"file number is {counter}")
	d.clean_data(content)
	print(f"file number is {counter}")
	d.save_data("content", './data_source_after_drop_data/token_data.csv')

		# t = text_analysis.scikit(content)

		# x = []
		# for doc in content:
		# 	x.append(t.document_vector(doc))

		# z = np.array(x)
		# t.t_sne(z)
		# t.scatter_plot()

