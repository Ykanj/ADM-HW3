# adm-hw3
## Code:
### Q1 (Yousef)
- Get_URL.py parses through the first 400 pages to retreive all URLs
- Retreive_&_sort_HTML_asyncio.py attempts to reteive the htmls of the 6000 URLs we got, using asynchronous scheduling, but the website was blocking us for 4 out of every 5 requests due to sending out ~8 requests a second.
- Retreive_&_sort_HTML_ThreadPool.py, sent out one request at a time, but used a library to split all work between all cores of the cpu.
- Datafram_builder.py reads every html we have saved, retreives the data we need from it, and builds a pandas dataframe while saving every row as a tsv file. It then calls the cleaning function we wrote in NLTK_cleaning to add a cleaned column

### Q2 (Yousef)
- NLTK_cleaning has a function written to clean, tokenize, strip and lemmatize a given text.
- Currency_Format.py converts the "fees" columns to a "cleaned fee (EUR)" column using regex and a convert_currency library.
- Vocuabulary_generator.py parses over all words in each cleaned description and creates a dataframe of all unique words with their term IDs.
- Inverted_index.py creates a simple inverted index for all unique words found.
- first_search_engine.ipynb is a simple search engine that simply looks for words from our query in our degrees and returns matches.
- TF-IDF.py generates an inverted index dictionary where for each term_id as key, we have a list of tuples of documents it is found in, and it's relative TF-IDF score.

### Q3 (Renato)

### Q4 (Renato)

### Q5 (Amir)

### CLQ (Paolo)

### AQ (Paolo)
- Algorithm.py is an algorithm that solves our Algorithm question in the homework.
- ChatGPT_conversation.md is a markdown file that contains our chatGPT conversation regarding the algorithm question.
  
## Data: 
### Q1
- Each_Degree_URL.txt has the url of each of the 6000 degrees on each line.
- each_row_tsv.zip has the tsv file of every row in our data frame.
- Parsed_database.csv is a csv file of our entire dataset.
- Degrees_by_page.zip is a zip file of 400 folders each with the HTMLs of the 15 degrees found per page. It was too large to upload to github.

### Q2
- Vocabulary.csv is a saved csv file of our unique vocabulary list.
- saved_dictionary.pkl is our inverted index dictionary saved with the python library pickle.
- saved_dictionary_tfidf.pkl is our inverted index dictionary including TF-IDF scores saved with the python library pickle.
