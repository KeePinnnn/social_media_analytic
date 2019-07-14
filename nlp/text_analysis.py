from textblob import TextBlob
from textblob import Word

class text_blob():
    def __init__(self, text:str):
        self.text = text
        self.text_blob = TextBlob(self.text)

    def return_text(self):
        return self.text

    def get_sentiment(self):
        return self.text_blob.sentiment

    def get_sentences(self):
        return self.text_blob.get_sentences

    def get_words(self):
        return self.text_blob.words

    def correct_sentence(self, sentence:str):
        sen = TextBlob(sentence)
        return sen.correct()

    def check_spelling(self, text:str):
        word = Word(text)
        return word.spellcheck()

    def detect_lang(self, text:str):
        source = TextBlob(unicode(text))
        return source.detect_language()