from nlp.text_analysis import text_blob

class text_controller():
    def create_blob(self, text:str):
        # remove left and right white spaces
        sentence = text.lstrip().rstrip()
        self.blob = text_blob(sentence)
        print(self.blob.get_sentiment())
        