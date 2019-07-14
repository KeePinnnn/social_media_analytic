import pandas as pd

from config import FILE_PATH


class file_controller():
    def __init__(self):
        self.init_path = FILE_PATH

    def set_file(self, file_name:str):
        self.file = self.init_path + file_name
        return self.file

    def retrieve_info(self):
        data = pd.read_csv(self.file, engine='python', encoding='utf-8', error_bad_lines=False)
        return data