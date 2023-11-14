import pandas as pd
import os
import requests
from bs4 import BeautifulSoup 
from tqdm import tqdm
import concurrent.futures

# initialize a dataframe with all our needed columns
df = pd.DataFrame(columns=[
    'courseName', 'universityName', 'facultyName', 'isItFullTime',
    'description', 'startDate', 'fees', 'modality', 'duration',
    'city', 'country', 'administration', 'url', 'cleaned description'])

root_dir = r"C:\Users\youse\Desktop\ADM Hw3\Degrees by Page"
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for subdir, dirs, files in tqdm(os.walk(root_dir)):
        for file in files:
            with open(os.path.join(subdir, file), 'r', encoding='utf-8') as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, "html.parser")

                courseName = universityName = facultyName = isItFullTime = description = startDate = fees = modality = duration = city = country = administration = url = None

                try:
                    courseName = soup.find("h1", class_="text-white course-header__course-title")["data-permutive-title"]
                except:
                    pass
                try:
                    universityName = soup.find("a", class_="course-header__institution").text.strip()
                except:
                    pass  
                try:
                    facultyName = soup.find("a", class_="course-header__institution").text.strip()
                except:
                    pass 
                try:
                    isItFullTime = " ".join(soup.find("span", class_="key-info__content key-info__study-type py-2 pr-md-3 text-nowrap d-block d-md-inline-block").text.strip().split())
                except:
                    pass
                try:
                    description = soup.find("div", class_="course-sections__content").text.strip()
                except:
                    pass
                try:
                    startDate = soup.find("span", class_="key-info__content key-info__start-date py-2 pr-md-3 text-nowrap d-block d-md-inline-block").text.strip()
                except:
                    pass
                try:
                    fees = " ".join(soup.find("div", class_="course-sections course-sections__fees tight col-xs-24").find('div', class_='course-sections__content').find('p').text.strip().split())
                except:
                    pass
                try:
                    modality = soup.find("span", class_="key-info__content key-info__qualification py-2 pr-md-3 text-nowrap d-block d-md-inline-block").text.strip()
                except:
                    pass
                try:
                    duration = soup.find("span", class_="key-info__content key-info__duration py-2 pr-md-3 d-block d-md-inline-block").text.strip()
                except:
                    pass
                try:
                    city = soup.find("a", class_="card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__city").text.strip()
                except:
                    pass
                try:
                    country = soup.find("a", class_="card-badge text-wrap text-left badge badge-gray-200 p-2 m-1 font-weight-light course-data course-data__country").text.strip()
                except:
                    pass
                try:
                    administration = soup.find("div", class_="course-data__container col-24 ml-md-n1 p-0 pb-3").find_all("a")[-1].text.strip()
                except:
                    pass
                try:
                    url = soup.find("head").find_all("link")[0]["href"]
                except:
                    pass
                
                df.loc[len(df)] = [courseName, universityName, facultyName, isItFullTime, description, startDate, fees, modality, duration, city, country, administration, url]
                # Here we save the last row of the data frame as an individual tsv file
                df.iloc[-1].to_csv(f"c:\\Users\\youse\\Desktop\\ADM Hw3\\Databases\\Each row tsv\\ row {len(df)}.tsv", sep="\t", index = False)
                # and here using the cleaning function we wrote and imported from NLTK_cleaning we add a cleaned description column
                
        print(df.shape)
    for i in range(len(df)):
        text = df["description"][i]
        try:
            df["cleaned description"][i] = clean(text)
        except:
            df["cleaned description"][i] = text 
    


    df.to_csv(r"c:\Users\youse\Desktop\ADM Hw3\Parsed_database.csv")
