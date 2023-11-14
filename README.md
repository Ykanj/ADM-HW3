# adm-hw3
Code:
- Get_URL.py parses through the first 400 pages to retreive all URLs
- Retreive_&_sort_HTML_asyncio.py attempts to reteive the htmls of the 6000 URLs we got, using asynchronous scheduling, but the website was blocking us for 4 out of every 5 requests due to sending out ~8 requests a second.
- Retreive_&_sort_HTML_ThreadPool.py, sent out one request at a time, but used a library to split all work between all cores of the cpu.
- Datafram_builder.py reads every html we have saved, retreives the data we need from it, and builds a pandas dataframe while saving every row as a tsv file. It then calls the cleaning function we wrote in NLTK_cleaning to add a cleaned column
- NLTK_cleaning has a function written to clean, tokenize, strip and lemmatize a given text.
- Currency_Format.py converts the "fees" columns to a "cleaned fee (EUR)" column using regex and a convert_currency library.
- Vocuabulary_generator.py parses over all words in each cleaned description and creates a dataframe of all unique words with their term IDs.
- Inverted_index.py creates a simple inverted index for all unique words found.
  
Data: 
- Each_Degree_URL.txt has the url of each of the 6000 degrees on each line.
- each_row_tsv.zip has the tsv file of every row in our data frame.
- Parsed_database.csv is a csv file of our entire dataset.
