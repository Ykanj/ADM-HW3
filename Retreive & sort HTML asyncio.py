import requests
from bs4 import BeautifulSoup 
from tqdm import tqdm
import os
import aiohttp
import asyncio

# First lets create a folder for each page to store its degree HTML 
for i in range(1,401):
    path_page = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(i)
    if not os.path.exists(path_page): 
        os.makedirs(path_page)


# I defined a function to request the url and return it as a prettified soup HTML,
# I first tired running this code with concurrent.futures.ThreadPoolExecutor()
# but that is preferred for cpu bound tasks, since here in web scraping we are
# I/O bound, i found a better solution to be asyncio, which instead of splitting 
# rescources between cores on the cpu like ThreadPool, asyncio sends out multiple 
# requests at once and proceeds with iterating, and updates the opened file when
# it receives a result from the sent request. Here aiohttp handles sending out 
# the requests, while asynchio organizes and handles the scheduling


# This method turned out very fast ~20 min, except for the fact thet the website started sending
# blank responses as a result of the server being requested from multiple times, so we turn back
# to Threadpool 

async def parser(url, degree_path):

    try:
        async with aiohttp.ClientSession() as request:
            async with request.get(url.strip()) as result:
                page_content = await result.text()
                soup = BeautifulSoup(page_content, "html.parser")
                with open(degree_path,"w",encoding = 'utf-8') as html:
                    html.write(str(soup.prettify()))
    except requests.exceptions.Timeout:
                print('The request timed out at: ', count)    
             
async def main():
    # i initialized a counter for naming each saved html page,
    # another for the page number to sort into files,
    # and another to count every 15 files
    page_number = 1
    degree_number = 1
    count = 0

    degree_urls = r"C:\Users\youse\Desktop\ADM Hw3\Each Degree URL.txt"
    page_path = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(page_number)

    # Reading from the list of urls, we send each file path and url to our parser fucntion
    with open(degree_urls, "r", encoding = 'utf-8') as file:
        for line in tqdm(file):
            count += 1
            degree_path = page_path + "\degree " + str(degree_number) +".txt"

            await parser(line, degree_path)
            print(degree_path)

            if count % 15 == 0:
                page_number +=1
                count = 0
                page_path = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page\page " + str(page_number)

            degree_number += 1

if __name__ == "__main__":
    asyncio.run(main())           