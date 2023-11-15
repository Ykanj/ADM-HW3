import pandas as pd
from tqdm import tqdm
import pickle
import re

vocab = pd.read_csv(r"Databases\Vocabulary.csv")
vocab = vocab.drop(columns=["Unnamed: 0"])

degrees = pd.read_csv(r"Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

inverted_index = {}

# we create a dictionary which corellates for each unique term id, all documents in our corpus where the term was found 
for i in tqdm(range(len(vocab))):
    word = vocab["term"][i] 
    word = str(word)
    term_id = vocab["term_id"][i]
    degrees["cleaned description"].fillna("", inplace=True)
    documents = degrees[degrees["cleaned description"].str.contains(re.escape(word), case=False)].index.tolist()
    inverted_index[term_id] = documents 

print(inverted_index)

# we saved the dictionary using the python pickle library in order to access it later when needed
with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)