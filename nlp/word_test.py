from gensim.models import KeyedVectors

if __name__ == "__main__":
    gmodel = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    t_vectors = [gmodel[x] for x in "this is just for testing purpose only".split(' ')]

    print(t_vectors)
