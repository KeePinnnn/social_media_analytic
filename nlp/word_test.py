from gensim.models import KeyedVectors

from text_analysis import text_blob
import pandas as pd

if __name__ == "__main__":
    # gmodel = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    # t_vectors = [gmodel[x] for x in "this is just for testing purpose only".split(' ')]

    # print(t_vectors)

    print("start")
    counter = 1
    while counter < 5:
        data = pd.read_csv(f'../data_source/after_drop_data/combined_data_{counter}.csv', engine='python', encoding='utf-8', error_bad_lines=False)
        df = pd.DataFrame(data=data)
        content = df['content']
        sentiment_list = []
        for each in content:
            t = text_blob(each)
            sentiment_list.append(t.get_sentiment())

        df['semantic_score'] = sentiment_list
        pd.to_csv(f'../data_source/after_drop_data/combined_data_{counter}.csv', encoding=False, index=False)
        counter += 1
        print(counter)

    print("done")