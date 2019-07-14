import pandas as pd
import numpy as np

file = './news_cleaned_2018_02_13.csv'
chunksize = 10 ** 4
counter = 1

for chunk in pd.read_csv(file, engine='python', encoding='utf-8', chunksize=chunksize):
    chunk.to_csv('testing' + str(counter) + '.csv', encoding='utf-8')
    counter += 1    
