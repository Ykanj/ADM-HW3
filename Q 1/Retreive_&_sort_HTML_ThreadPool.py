import requests
from bs4 import BeautifulSoup 
from tqdm import tqdm
import os
import concurrent.futures

# First lets create a folder for each page to store its degree HTML 
for i in range(1,401):
    path_page = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(i) 
    if not os.path.exists(path_page): 
        os.makedirs(path_page)

def parser(url, degree_path):
    try:
        page = requests.get(url.strip())
        soup = BeautifulSoup(page.content, "html.parser")
        with open(degree_path,"w",encoding = 'utf-8') as html:
            html.write(str(soup.prettify()))
    except requests.exceptions.Timeout:
        print('The request timed out at: ', count)   

page_number = 1
degree_number = 1
count = 0

degree_urls = r"C:\Users\youse\Desktop\ADM Hw3\Each Degree URL.txt"
page_path = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(page_number)

             
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    with open(degree_urls, "r", encoding = 'utf-8') as file:
        for line in tqdm(file):
            count+=1
            degree_path = page_path + "\degree " + str(degree_number)  +".txt"
            if not os.path.exists(degree_path): 
                parser(line, degree_path)

            if count % 15 == 0:
                page_number += 1
                page_path = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(page_number) 
                

            degree_number +=1
            
