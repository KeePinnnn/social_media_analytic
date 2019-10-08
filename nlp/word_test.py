from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import strip_punctuation
from gensim.models import KeyedVectors

from textblob import TextBlob
import pandas as pd
import numpy as np

from pattern.en import parse, Sentence, modality

if __name__ == "__main__":
    gmodel = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    print(dir(gmodel))

    # data = pd.read_csv('../data_source/after_drop_data/combined_data_1.csv', engine='python', encoding='utf-8')
    # df = pd.DataFrame(data)
    # content = remove_stopwords(strip_punctuation(df['content'][1]))
    content = "this is just for testing"
    print(gmodel.score(content.split()))
    # array = []

    # for word in content.split():
    #     try:
    #         vector = gmodel[word]
    #         array.append(np.average(vector))
    #     except:
    #         print(f'word not found {word}')
    #         pass

    # print(array)

    # t_vectors = [gmodel[x] for x in "this is just for testing purpose only".split(' ')]

    # print(t_vectors)

    # print("start")
    # counter = 1
    # while counter < 5:
    #     data = pd.read_csv(f'../data_source/after_drop_data/combined_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
    #     df = pd.DataFrame(data=data)
    #     # df.dropna(inplace=True)
    #     # print("drop done")
    #     # print(df.shape)

    #     print("done reading")
    #     content = df['content'].tolist()
    #     modality_list = []
    #     sub_counter = 0
    #     for each in content:
    #         sent = parse(each, lemmata=True)
    #         sent = Sentence(sent)
    #         print(f'inside the loop, the counter is f{sub_counter}, file is combined_data_f{counter}')
    #         modality_list.append(modality(sent))
    #         sub_counter += 1

    #     print(f"modality list is {len(modality_list)} length")

    #     df['modality_score'] = modality_list
    #     print(f"df is {df.shape}")
    #     df.to_csv(f'../data_source/after_drop_data/combined_data_{counter}.csv', encoding=False, index=False)
    #     print(f"written into combined_data_{counter}.csv")
    #     counter += 1
    #     # print(counter)

    # print("done")

