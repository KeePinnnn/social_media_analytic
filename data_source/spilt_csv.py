from sklearn.model_selection import ShuffleSplit
import pandas as pd
import numpy as np
import random
import os
import re 

file = './news_cleaned_2018_02_13.csv'
raw_data = './raw_data/data_set_'
shuffle_data = './shuffled_data/shuffled_data_'
chunksize = 10 ** 4
counter = 500
 
print("start")
start_file = pd.read_csv('./after_drop_data/after_drop_data_499.csv', engine='python', encoding='utf-8', error_bad_lines=False)
while counter < 665:
    next_file = pd.read_csv(f'./after_drop_data/after_drop_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    combine_data = pd.concat([start_file, next_file])
    start_file = combine_data 
    combine_data = ""
    os.remove(f'./after_drop_data/after_drop_data_{counter}.csv')
    counter += 1
    print(counter)

print("start shuffling")
combine_data = start_file.sample(frac=1).reset_index()
print("end shuffling") 
combine_data.to_csv('./after_drop_data/combined_data_4.csv', encoding=False, index=False)
print("done")

# print("start")
# for chunk in pd.read_csv(file, engine='python', encoding='utf-8', chunksize=chunksize):
#     chunk.to_csv(shuffle_data + str(counter) + '.csv', encoding='utf-8')
#     counter += 1

# print("done")

# print("start")
# data = pd.read_csv('./news_cleaned_2018_02_13.csv', engine='python', encoding='utf-8', error_bad_lines=False)
# print("read data")
# shuffle_data = data.sample(frac=1).reset_index(drop=True)
# print("done shuffle")
# shuffle_data.to_csv('./shuffled_data.csv', encoding='utf-8', index=False)
# print("write to csv")

# list_file = [f for f in os.listdir('./shuffle_raw_data/')]
# str_file = ''.join(list_file)
# regex = re.compile('\d+')
# file_num = regex.findall(str_file)
# while file_num and len(file_num) > 1:
#     first = random.choice(file_num)
#     file_num.remove(first)
#     second = random.choice(file_num)

#     first_data = pd.read_csv('./shuffle_raw_data/shuffle_data_' + first + '.csv', engine='python', encoding='utf-8', error_bad_lines=False)
#     second_data = pd.read_csv('./shuffle_raw_data/shuffle_data_' + second + '.csv', engine='python', encoding='utf-8', error_bad_lines=False)
#     combine_data = pd.concat([first_data, second_data])
#     combine_data = combine_data.sample(frac=1).reset_index(drop=True)

#     combine_data.to_csv('./shuffle_raw_data/shuffle_data_' + second + '.csv', encoding='utf-8', index=False)
#     if os.path.exists('./shuffle_raw_data/shuffle_data_' + first + '.csv'):
#         os.remove('./shuffle_raw_data/shuffle_data_' + first + '.csv')
#         print("remove shuffle_data_" + first + ".csv")
#     else:
#         print("unable to remove remove shuffle_data_" + first + ".csv - probably due to pathing")

#     print(second)

# print("done combining all the data")


# first round of spilting the data
# while counter < 665:
#     data = pd.read_csv(raw_data + str(counter) + '.csv', engine='python', encoding='utf-8', error_bad_lines=False)
#     data = data.sample(frac=1).reset_index(drop=True)
#     print("shuffle done")
#     data.to_csv('./shuffle_raw_data/shuffle_data_' + str(counter) + '.csv', encoding='utf-8')
#     counter += 1

# data = pd.read_csv(file, engine='python', encoding='utf-8', error_bad_lines=False)
# data = data.sample(frac=1).reset_index(drop=True)
# print("shuffle done")
# data.to_csv('shuffle_raw_data.csv', encoding='utf-8')
# for chunk in pd.read_csv(file, engine='python', encoding='utf-8', chunksize=chunksize, skiprows=6670000, error_bad_lines=False, warn_bad_lines=True):
#     chunk.to_csv('./raw_data/data_set_' + str(counter) + '.csv', encoding='utf-8')
#     counter += 1  

# sdata = ShuffleSplit(test_size=0.25)
# for train_index, test_index in sdata.split(data):
#     train_index.to_csv('training_data_' + str(counter) + '.csv', encoding='utf-8')
#     test_index.to_csv('testing_data_' + str(counter) + '.csv', encoding='utf-8')
#     counter += 1

