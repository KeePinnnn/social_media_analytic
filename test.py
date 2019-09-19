from data_source import data

if __name__ == "__main__":
	d = data.process_data()
	counter = 1
	while counter < 5:
		d.read_file(f'./data_source/after_drop_data/combined_data_{counter}.csv')	
		content = d.df['content']

		print(f"file number is {counter}")
		d.clean_data(content)
		print(f"file number is {counter}")
		d.save_data("content")
		
	

