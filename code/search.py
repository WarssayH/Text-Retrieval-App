from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
import re


def query_process(query):
    query = query.lower()
    query = query.strip()

    stopwords_english = stopwords.words('english')
    # create the Porter Stemmer
    stemmer = PorterStemmer()

    query_tokens = word_tokenize(query)
    clean_tokens = []

    for word in query_tokens:
        if word not in string.punctuation and word not in stopwords_english:
            # stem the tokens
            stem_word = stemmer.stem(word)
            clean_tokens.append(stem_word)

    return clean_tokens