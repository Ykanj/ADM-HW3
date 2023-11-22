import pandas as pd
from tqdm import tqdm
import pickle
import math

vocab = pd.read_csv(r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Vocabulary.csv")
vocab = vocab.drop(columns=["Unnamed: 0"])

degrees = pd.read_csv(r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

inverted_index = {}
# we define a function to calculate term frequencies, by counting the number of occurances of each word in a text
# normalized for longer texts by dividing by the length of the text
def tf(term, text):
    term_count = text.count(term)
    total_words = len(text.split())
    return term_count / total_words    

# we define a function to calculate inverse document frequency, which is the logarithm of the total number of docs
# is our corpus divided by the number of occurances of each term in each corpus
def idf(term, df):
    count = df["cleaned description"].apply(lambda x: term in x).sum()
    return math.log((len(df))/(count))        

# the dictionary was created in the same approach to the inverted index, with the addition of a for loop to calculate tf-idf 
# values for each term in each document we know its found in. Each document and the term tf-idf was saved as a tuple in a list as a value
for i in tqdm(range(len(vocab))):
    word = vocab["term"][i] 
    word = str(word)
    term_id = vocab["term_id"][i]
    degrees["cleaned description"].fillna("", inplace=True)
    documents = degrees[degrees["cleaned description"].str.contains(word, case=False)].index.tolist()
    idf_value = idf(word, degrees)
    results = []
    for document in documents:
        tf_value = tf(word, degrees["cleaned description"].iloc[document])
        tfidf = tf_value * idf_value
        pair = (document, tfidf)
        results.append(pair)
    
    inverted_index[term_id] = results
    if i ==0:
        print(inverted_index[term_id])
    


print(inverted_index)

# the dictionary was saved for later use using the pickle library
with open('saved_dictionary_tfidf.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)