import numpy as np
import pandas as pd

file = './testing2.csv'

df = pd.read_csv(file, engine='python')
to_drop = ['Unnamed: 0', 'Unnamed: 0.1', 'scraped_at', 'inserted_at', 'updated_at']
df.drop(to_drop, inplace=True, axis=1)
df.to_csv('clean2.csv')

# class clean_data(self):
#     self.file = './testing1.csv'
#     self.to_drop = ['Unnamed: 0', 'Unnamed: 0.1', 'scraped_at', 'inserted_at', 'updated_at']

#     def cleanup(self):
#         df = pd.read_csv(self.file, engine='python')
#         df.drop(self.to_drop, inplace=True, axis=1)

