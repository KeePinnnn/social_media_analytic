from sklearn import preprocessing
import pandas as pd
import numpy as np

le = preprocessing.LabelEncoder()
data = pd.read_csv('./clean1.csv', engine='python', encoding='utf-8', error_bad_lines=False)
data = data.replace(np.nan, '', regex=True)
data['domain'] = le.fit_transform(data['domain'])
data['url'] = le.fit_transform(data['url'])
data['authors'] = le.fit_transform(data['authors'])
data['type'] = le.fit_transform(data['type'])
print(data)

