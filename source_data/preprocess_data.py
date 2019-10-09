import pandas as pd

import re

class clean_col():
    def clean_url(self, use_csv:str, col:str, result_csv:str):
        df = read_data(use_csv)
        url = df[col]
        pattern = r'\/\/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b'

        new_link = []
        for each in url:
            link = re.search(pattern, each)
            if link:
                new_link.append(link.group(0)[:])
            else:
                new_link.append(each)

        df.update(pd.DataFrame({col: new_link}))
        df.to_csv(result_csv, index=False)

    def clean_author(self, use_csv:str, col:str, result_csv:str):
        df = read_data(use_csv)
        authors = df[col]

        new_author = []
        for each in authors:
            try:
                check = each[:2]
                if check == "By":
                    str_author = each[2:].lstrip().rstrip()
                    new_author.append(str_author)
                else:
                    new_author.append(each)
            except:
                new_author.append(each)

        df.update(pd.DataFrame({col: new_author}))
        df.to_csv(result_csv, index=False)

    def read_data(self, file_data:str):
        data = pd.read_csv(file_data)
        return pd.DataFrame(data)
    