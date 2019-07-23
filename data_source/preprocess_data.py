from sklearn import preprocessing
import pandas as pd
import numpy as np

class process_data():
    def __init__(self):
        self.le = preprocessing.LabelEncoder()

    def transform_data(self, data:object):
        data = data.replace(np.nan, '', regex=True)
        data['domain'] = self.le.fit_transform(data['domain'])
        data['url'] = self.le.fit_transform(data['url'])
        data['authors'] = self.le.fit_transform(data['authors'])
        data['type'] = self.le.fit_transform(data['type'])
        return data
