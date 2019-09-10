import pandas as pd

filename = './news_cleaned_2018_02_13.csv'
chunksize = 10 ** 3
counter = 1

for chunk in pd.read_csv(filename, chunksize=chunksize, encoding='utf-8', engine='python'):
    print(chunk['type'])
    
        
    # df = pd.DataFrame(chunk, columns = ['id', 'domain', 'type', 'url', 'content', 'scraped_at', 'inserted_at', 'updated_at', 'title', 'authors', 
    # 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary', 'source'])
    # df.to_csv('testing_' + str(counter) + '.csv')
    # counter += 1