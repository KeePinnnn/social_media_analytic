import numpy as np
import pandas as pd

file = './shuffled_data/combined_data_1.csv'
counter = 1

print("start")
while counter < 665:
    df = pd.read_csv(f'./shuffled_data/shuffled_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    to_drop = ['Unnamed: 0', 'Unnamed: 0.1', 'id', 'scraped_at', 'inserted_at', 'updated_at', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary', 'source']
    df.drop(to_drop, inplace=True, axis=1)
    df.to_csv(f'./after_drop_data/after_drop_data_{counter}.csv')
    counter += 1
    print(counter)

print("done")

# file = './processed_data.csv'

# df = pd.read_csv(file, engine='python')
# to_drop = ['id']
# df.drop(to_drop, inplace=True, axis=1)
# df.to_csv('processed_data.csv', index=False)

# class clean_data(self):
#     self.file = './testing1.csv'
#     self.to_drop = ['Unnamed: 0', 'Unnamed: 0.1', 'scraped_at', 'inserted_at', 'updated_at']

#     def cleanup(self):
#         df = pd.read_csv(self.file, engine='python')
#         df.drop(self.to_drop, inplace=True, axis=1)

