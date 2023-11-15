import string
import pandas
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer as ps
from nltk.stem import WordNetLemmatizer

# I wrote a function to clean the description from any stopwords and punctuation, from there i wanted to
# choose whether stemming of lemmatization is more suitable for processing the descriptions, and while
# stemming removes all prefixes and suffixes, lemmatization uses context to get a base word such as 
# better -> good and therefore preserves context better than stemming, which could be more useful in a 
# query search engine where the goal is to match  searches to results. One thing to note is that lemmatization 
# is more computationally costly than stemming.

def clean(text: str):
    
    # I removed stopwords and punctuation and transformed the entire description to lowercase
    tokens = nltk.word_tokenize(text.lower())
    trash = set(stopwords.words("english") + list(string.punctuation) + list("’"))
    tokens = [token for token in tokens if token not in trash]
    stemmed = []
    lemmatized = []

    # I stemmed and lemmatized the multiple descriptions to compare results and reach a choice between the 2 methods
    # After viewing the results i decided to continue with lemmatization as it gave more generalized results and served 
    # the same purpose as stemming

    #for token in tokens:
    #    stemmed_token = ps().stem(token)
    #    if stemmed_token not in stemmed:
    #        stemmed.append(stemmed_token)
    for token in tokens:
        lemma = WordNetLemmatizer().lemmatize(token)
        if lemma not in lemmatized:
            lemmatized.append(lemma)
    lemmatized = " ".join(lemmatized)        
    return lemmatized