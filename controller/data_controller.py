from data_source.preprocess_data import process_data

class data_controller():
    def __init__(self):
        self.process_data = process_data()

    def format_data(self, data:object):
        self.data = self.process_data.transform_data(data)
        return self.data