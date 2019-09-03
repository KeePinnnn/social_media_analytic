import numpy as np
import pandas as pd

file = './after_drop_data/'
counter = 1

print("start")
# while counter < 665:
#     df = pd.read_csv(f'./shuffled_data/shuffled_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
#     to_drop = ['Unnamed: 0', 'Unnamed: 0.1', 'id', 'scraped_at', 'inserted_at', 'updated_at', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary', 'source']
#     df.drop(to_drop, inplace=True, axis=1)
#     df.to_csv(f'./after_drop_data/after_drop_data_{counter}.csv')
#     counter += 1
#     print(counter)

while counter < 5:
    df = pd.read_csv(file + f'combined_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    to_drop = ['Unnamed: 0']
    df.drop(to_drop, inplace=True, axis=1)
    df.to_csv(file + f'combined_data_{counter}.csv', index=False)
    counter += 1
    print(counter)

print("done")