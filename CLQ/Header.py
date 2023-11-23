import pandas as pd

# we write a code to save the dataframe header as a csv file so that we wont have to deal with it for each indvidual file

degrees = pd.read_csv(r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Parsed_database.csv", nrows= 0)
degrees = degrees.drop(columns=["Unnamed: 0", "cleaned description", "corrected fee (EUR)"])
degrees.to_csv(r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Each_row_tsv_updated\header.tsv", sep='\t', index=False, header=True)
