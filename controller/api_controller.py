from functools import reduce

from google.api import GoogleInfor


class GoogleController():
    '''
        gather the information from google and make sense out of the data
    '''

    def __init__(self, text:str):
        '''
            this function is to remove all the singlish that google will not be able to analyse 
            in addition, change the format of the data to make better sense of it 
        '''
        self.singlish = [" la", " hor", " eh", " liao", " ah"]
        text = reduce(lambda a,b: a.replace(b, ''), self.singlish, text)

        self.api = GoogleInfor(text)

    def get_score(self):
        sentiment_result = self.api.analyze_sentiment()
        entity_sentiment_result = self.api.analyze_entity_sentiment()
        

        print(sentiment_result)
        print(entity_sentiment_result)