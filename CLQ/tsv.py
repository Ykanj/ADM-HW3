import os
import pandas as pd
from tqdm import tqdm

source_directory = r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Each row tsv"
destination_directory = r"C:\Users\youse\Desktop\GitHub\adm-hw3\Databases\Each_row_tsv_updated"

#  while saving each row as tsv in the first question, rows were saved as a column on tsv. we quickly write a code 
#  to transpose and save each tsv file in an updated folder

for filename in tqdm(os.listdir(source_directory)):
    print(filename)
    if filename.endswith(".tsv"):
        
        file_path = os.path.join(source_directory, filename)
        
        df = pd.read_csv(file_path, sep='\t')
        df_transposed = df.transpose()
        
        save_path = os.path.join(destination_directory, f"transposed_{filename}")
        df_transposed.to_csv(save_path, sep='\t', index=False )
