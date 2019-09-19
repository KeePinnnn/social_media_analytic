from gensim.models import KeyedVectors
from adjustText import adjust_text
from sklearn.manifold import TSNE
from textblob import TextBlob
from textblob import Word

import gensim

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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

class text_vector():
    def __init__(self, list_content:list): 
        self.model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
        self.list_content = list_content
        self.corpus = []

    def document_vector(self, doc:str):
        doc = [word for word in doc if word in self.model.vocab]
        self.average_vector = np.mean(self.model[doc], axis=0)
        return self.average_vector

    def has_vector_representation(self, doc:str):
        return not all(word not in self.model.vocab for word in doc)

    def filter_docs(self, condition_on_doc:bool):
        num_docs = len(corpus)

        if self.list_content is not None:
            self.list_content = [text for (text, doc) in zip(self.list_content, self.corpus) if condition_on_doc(doc)]

        self.corpus = [doc for doc in self.corpus if condition_on_doc(doc)]

        print(f"{number_of_docs - len(corpus)} docs removed")

        return (self.corpus, self.list_content)

    def t_sne(self, arr:object):
        self.tsne = TSNE(n_components = 2, init = 'random', random_state = 10, perplexity = 100)
        self.tsne_df = self.tsne.fit_transform(arr)
        return self.tsne_df

    def scatter_plot(self):
        sns.set()

        fig, ax = plt.subplots(figsize = (11.7, 8.27))
        sns.scatterplot(self.tsne_df[:, 0], self.tsne_df[:, 1], alpha = 0.5)

        contents = []
        content_to_plot = list(np.arange(0, len(self.list_content), 1000))

        for content in content_to_plot:
            contents.append(plt.text(self.tsne_df[content, 0], self.tsne_df[content, 1], self.list_content[content], fontsize = 14))

        adjust_text(contents, force_points = 0.4, force_text = 0.4, expand_points = (2,1), expand_text = (1,2),
                    arrowprops = dict(arrowstyle = "-", color = 'black', lw = 0.5))

        plt.show()
        
        

    