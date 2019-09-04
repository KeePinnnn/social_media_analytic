# from gensim.models import KeyedVectors

from textblob import TextBlob
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
        # df.dropna(inplace=True)
        # print("drop done")
        # print(df.shape)

        for index, row in df.iterrows():
            if type(row['content']) is not str:
                print(row)
                df.drop(index)
                print(index)

        print(f"counter is {counter}")
            

        content = df['content'].tolist()
        polarity_list = []
        subjectivity_list = []
        for each in content:
            t = TextBlob(str(each))
            polarity_list.append(t.sentiment.polarity)
            subjectivity_list.append(t.sentiment.subjectivity)

        print(f"polarity list is {len(polarity_list)} length")
        print(f"subjectivity list is {len(subjectivity_list)} length")

        df['polarity_score'] = polarity_list
        df['subjectivity_score'] = subjectivity_list
        print(f"df is {df.shape}")
        df.to_csv(f'../data_source/after_drop_data/combined_data_{counter}.csv', encoding=False, index=False)
        print(f"written into combined_data_{counter}.csv")
        counter += 1
        # print(counter)

    print("done")