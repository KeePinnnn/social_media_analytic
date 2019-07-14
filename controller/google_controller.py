from google.google_api import GoogleInfor

class GoogleController():
    '''
        gather the information from google and make sense out of the data
    '''

    def __init__(self):
        self.api = GoogleInfor()

    def get_score(self, text:str):
        self.api.set_text(text)
        sentiment_result = self.api.analyze_sentiment()
        entity_sentiment_result = self.api.analyze_entity_sentiment()
        

        print(sentiment_result)
        print("entity")
        print(entity_sentiment_result)

        return entity_sentiment_result, sentiment_result