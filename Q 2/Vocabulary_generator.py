import pandas as pd
from tqdm import tqdm

vocab = pd.DataFrame(columns=["term", "term_id"])

degrees = pd.read_csv(r"C:\Users\youse\Desktop\ADM Hw3\Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

term_count = 100000
for i in tqdm(range(len(degrees))):
    text = degrees["cleaned description"][i]
    text = str(text)
    text = text.split(" ")
    for n in text:
        if (not n.isdigit()) and (n not in vocab["term"].unique()):
            vocab.loc[len(vocab)] = [n , term_count]
            term_count += 1            

vocab.to_csv(r"c:\Users\youse\Desktop\ADM Hw3\Vocabulary_1.csv")


