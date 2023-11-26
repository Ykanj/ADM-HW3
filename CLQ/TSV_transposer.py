import os
import pandas as pd
from tqdm import tqdm

degrees = pd.read_csv(r"Databases\Parsed_database.csv")
degrees = degrees.drop(columns=["Unnamed: 0"])

destination_directory = r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Each_row_tsv_updated"
output_directory = os.path.join(destination_directory, "Each row tsv")

# Check if the output directory exists, create it if not
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

#  while saving each row as tsv in the first question, rows were saved as a column on tsv. we quickly write a code 
#  to transpose and save each tsv file in an updated folder

for i in tqdm(range(len(degrees))):               
    row = degrees[["courseName", "universityName" ,"duration", "city", "country"]].iloc[i]
    row.to_csv(os.path.join(output_directory, f"row_{i}.tsv"), sep="\t", index= False, header = False)
