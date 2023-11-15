import requests
from bs4 import BeautifulSoup 
from tqdm import tqdm

# for each page, we identified the class for which the link to each degree belongs, 
# in this python file we will collect all these urls and save them to a text file

url = "https://www.findamasters.com/masters-degrees/msc-degrees/"
file = r"Databases\Each Degree URL.txt"
page_number = 1


for a in tqdm(range(400)):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    degrees = soup.find_all("a", class_="readMoreOrLess text-success text-nowrap")
    degree_list =["https://www.findamasters.com" + degree["href"] for degree in degrees]
    
    # We write the urls on each page in a text file
    f = open(file, "a")
    f.write('\n'.join(degree_list))
    f.write('\n')
    f.close


    # here we retreive the url of the next page, using a counter and inspect element to get the next url
    page_number += 1
    page_link = soup.find("li", title = f'Page {page_number} of 769').find("a")["href"]
    url = "https://www.findamasters.com" + page_link
print(page_number)    

