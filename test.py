from controller.google_controller import GoogleController
from controller.twitter_controller import twit_controller
from controller.text_controller import text_controller
from controller.file_controller import file_controller
from controller.data_controller import data_controller

if __name__ == "__main__":
	f = file_controller()
	d = data_controller()
	t = text_controller()
	f.set_file("clean1.csv")
	raw_data = f.retrieve_info()

	process_data = d.format_data(raw_data)

	for index, row in process_data.iterrows():
		content = t.create_blob(row['content'])
		title = t.create_blob(row['title'])
		process_data.loc[index, 'content'] = content[0]
		process_data.loc[index, 'title'] = title[0]

	print(process_data)
	process_data.to_csv('./data_source/processed_data.csv', encoding='utf-8', index=False)



	# G = GoogleController()
	# text = "Fielded questions on China, trade tensions, the global economic outlook, the next GE & more at a ‘fireside chat’ at the Business China Awards 2019 event last night. Congratulations to all the award winners!"

	# print(G.get_score(text))

	# twit = twit_controller("leehsienloong", 10)
	# twit.get_twit_info()
