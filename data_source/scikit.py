import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

file = './processed_data.csv'
# file_test = './clean2.csv'

data = pd.read_csv(file, engine='python', encoding='utf-8', error_bad_lines=False)
# testing_data = pd.read_csv(file_test, engine='python', encoding='utf-8', error_bad_lines=False)
target = data['type']
data.drop(['type'], inplace=True, axis=1)

data_train, data_test, target_train, target_test = train_test_split(data,target)
gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))