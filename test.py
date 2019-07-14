from controller.google_controller import GoogleController
from controller.twitter_controller import twit_controller
from controller.text_controller import text_controller
from controller.file_controller import file_controller

if __name__ == "__main__":
	f = file_controller()
	f.set_file("clean1.csv")
	raw_data = f.retrieve_info()

	for index, row in raw_data.iterrows():
		t = text_controller()
		t.create_blob(row['content'])



	# G = GoogleController()
	# text = "Fielded questions on China, trade tensions, the global economic outlook, the next GE & more at a ‘fireside chat’ at the Business China Awards 2019 event last night. Congratulations to all the award winners!"

	# print(G.get_score(text))

	# twit = twit_controller("leehsienloong", 10)
	# twit.get_twit_info()
