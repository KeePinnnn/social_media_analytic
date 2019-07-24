import pandas as pd
import numpy as np

from sklearn.preprocessing import normalize
from sklearn.preprocessing import minmax_scale

from config import FILE_PATH

class normalise():
    def __init__(self, file:str, header:list):
        self.file_path = FILE_PATH + file
        self.header = header

    def read_file(self):
        raw_data = pd.read_csv(self.file_path, engine='python', encoding='utf-8', error_bad_lines=False)
        return raw_data
        

    def max_min(self, data:object):
        new_df = {}
        for each_header in self.header:
            result = minmax_scale(np.array(data[each_header].tolist()))
            new_df[each_header] = result

        data.update(new_df)
        return data

    def max_normalise(self, data:object):
        new_df = {}
        for each_header in self.header:
            result = normalize(np.array(data[each_header].tolist()).reshape(1, -1), norm="max")[0]
            print(result)
            new_df[each_header] = result

        data.update(new_df)
        return data

    def least_absolute(self, data:object):
        new_df = {}
        for each_header in self.header:
            result = normalize(np.array(data[each_header].tolist()).reshape(1, -1), norm="l1")[0]
            print(result)
            new_df[each_header] = result

        data.update(new_df)
        return data

    def least_square(self, data:object):
        new_df = {}
        for each_header in self.header:
            result = normalize(np.array(data[each_header].tolist()).reshape(1, -1), norm="l2")[0]
            print(result)
            new_df[each_header] = result

        data.update(new_df)
        return data
            