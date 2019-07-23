import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from config import FILE_PATH

class psychic():
    def __init__(self, file_path:str):
        self.file = FILE_PATH + file_path
        self.data = pd.read_csv(self.file, engine='python', encoding='utf-8', error_bad_lines=False)
        self.target = self.data['type']
        self.data.drop(['type'], inplace=True, axis=1)
        self.data_train, self.data_test, self.target_train, self.target_test = train_test_split(self.data, self.target)

    def naive_bay(self):
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
        print ("KNeighbors accuracy score : ", accuracy_score(self.target_test, pred))