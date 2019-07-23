from data_source.preprocess_data import process_data
from data_source.normalise import normalise
from data_source.scikit import psychic

class data_controller():
    def __init__(self):
        self.process_data = process_data()
        self.normalise = normalise("processed_data.csv", ['domain', 'url', 'authors'])

    def format_data(self, data:object):
        self.data = self.process_data.transform_data(data)
        return self.data

    def normal_min(self, data:object):
        self.normalise_data = self.normalise.max_min(data)
        return self.normalise_data

    def testing_normal(self):
        self.raw_normalise_data = self.normalise.read_file()
        self.normalise_data = self.normalise.max_min(self.raw_normalise_data)
        return self.normalise_data

    def psychic_algo(self, file_path:str):
        self.psychic = psychic(file_path)
        self.psychic.svc(3)

