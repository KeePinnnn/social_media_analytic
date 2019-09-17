import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.preprocessing import normalize
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

import random
import os
import re 

class csv_file():
    def chunk_data(self, file_name:str, chunk_size:int, re_path:str, save_file:str) -> bool:
        """
            this function is to chunk a large csv file into smaller files 
            so that it can be read into the ram 

            file_name is the target file to be cut into smaller files
            chunk_size is the size to cut the file 
            re_path is the relative path for the data to be save, e.g. './raw_data/'
            save_file is the name to save the data as without .csv as there 
            is a need to add counter to the file name to make it unique
        """
        self.file = file_name
        self.chunk = chunk_size
        self.path = re_path
        self.save_file = save_file
        self.counter = 1

        for chunk in pd.read_csv(self.file, engine='python', encoding='utf-8', chunksize=self.chunk, error_bad_lines=False)
            chunk.to_csv(self.path + self.save_file + f'{self.counter}.csv', encoding='utf-8')
            self.counter += 1

        if os.path.exists(self.path):
            return True
        else:
            return False

    def shuffle_data(self, list_file:list, save_file:str) -> bool:
        """

        """
        self.save_file = save_file

        self.combined_data = [x for x in pd.read_csv(list_file, engine='python', encoding='utf-8', error_bad_lines=False)]
        self.combined_data = self.combined_data.sample(frac=1).reset_index(drop=True)
        self.combined_data.to_csv(self.save_file, encoding='utf-8')

        if os.path.exists(self.save_file):
            return True
        else:
            return False

    def remove_col(self, drop_col:list, file_name:str, save_file:str) -> bool:
        self.to_drop = drop_col
        self.file = file_name

        self.data = pd.read_csv(self.file, engine='python', encoding='utf-8', error_bad_lines=False)
        self.data.drop(self.to_drop, inplace=True, axis=1)
        self.data.to_csv(self.file, encoding='utf-8', index=False)

        if os.path.exists(self.save_file):
            return True
        else:
            return False


class process_data():
    def __init__(self):
        self.label_encoder = preprocessing.LabelEncoder()

    def transform_data(self, data:object) -> object:
        self.data = data
        transform_dict = {}
        for each_col in self.data:
            transform_dict[each_col] = self.label_encoder.fit_transform(each_col)

        return transform_dict

    def read_file(self, file_path:str):
        self.file = pd.read_csv(file_path, engine='python', encoding='utf-8', error_bad_lines=False)
        return self.file

    def max_min(self, data:object, header:list):
        self.new_df = {}
        self.data = data

        for each_header in header:
            result = minmax_scale(np.array(self.data[each_header].tolist()))
            self.new_df[each_header] = result

        self.data.update(self.new_df)
        return self.data

    def max_normalise(self, data:object, header:list):
        self.new_df = {}
        self.data = data

        for each_header in header:
            result = normalize(np.array(self.data[each_header].tolist()).reshape(1, -1), norm="max")[0]
            self.new_df[each_header] = result

        self.data.update(self.new_df)
        return self.data

    def least_absolute(self, data:object, header:list):
        self.new_df = {}
        self.data = data

        for each_header in header:
            result = normalize(np.array(self.data[each_header].tolist()),reshape(1, -1), norm="l1")[0]
            self.new_df[each_header] = result

        self.data.update(self.new_df)
        return self.data

    def least_square(self, data:object, header:list):
        self.new_df = {}
        self.data = data

        for each_header in header:
            result = normalize(np.array(self.data[each_header].tolist()),reshape(1, -1), norm="l2")[0]
            self.new_df[each_header] = result

        self.data.update(self.new_df)
        return self.data

class scikit():
    def __init__(self, file_path:str):
        self.file = file_path
        self.data = pd.read_csv(self.file, engine='python', encoding='utf-8', error_bad_lines=False)
        self.target = self.data['type']
        self.data.drop(['type'], inplace=True, axis=1)
        self.data_train, self.data_test, self.target_train, self.target_test = train_test_split(self.data, self.target)

    def naive_bayes(self):
        gnb = GaussianNB()
        pred = gnb.fit(self.data_train, self.target_train).predict(self.data_test)
        print("Naive-Bayes accuracy : ", accuracy_score(self.target_test, pred, normalize=True))

    def svc(self, shuffle_data:int):
        svc_model = LinearSVC(random_state=shuffle_data)
        pred = svc_model.fit(self.data_train, self.target_train).predict(self.data_test)
        print("LinearSVC accuracy : ", accuracy_score(self.target_test, pred))

    def k_neighbors(self, neighbour:int):
        neigh = KNeighborsClassifier(n_neighbors=neighbour)
        pred = neigh.fit(self.data_train, self.target_train).predict(self.data_test)
        print("KNeighbors accuracy score : ", accuracy_score(self.target_test, pred))