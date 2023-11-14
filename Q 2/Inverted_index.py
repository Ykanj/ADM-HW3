import pandas as pd
from tqdm import tqdm
import pickle
import re

vocab = pd.read_csv(r"C:\Users\youse\Desktop\ADM Hw3\Vocabulary.csv")
vocab = vocab.drop(columns=["Unnamed: 0"])

degrees = pd.read_csv(r"C:\Users\youse\Desktop\ADM Hw3\Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

inverted_index = {}

for i in tqdm(range(len(vocab))):
    word = vocab["term"][i] 
    word = str(word)
    term_id = vocab["term_id"][i]
    degrees["cleaned description"].fillna("", inplace=True)
    documents = degrees[degrees["cleaned description"].str.contains(re.escape(word), case=False)].index.tolist()
    documents = documents
    inverted_index[term_id] = documents

print(inverted_index)

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)