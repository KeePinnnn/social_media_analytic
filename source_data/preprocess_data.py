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

    def remove_emoji(self, text:str):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    