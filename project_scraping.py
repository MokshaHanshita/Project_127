from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers=["Name:","Distance","Mass","Radius"]

browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(1)
final_data=[]
soup=BeautifulSoup(browser.page_source,"html.parser")
tb=soup.find_all("table",attrs={"class":"wikitable"})[0]
tbody=tb.find_all("tbody")[0]
trTags=tbody.find_all("tr")

temp_list=[]
for trTag in trTags:
    tdTags=trTag.find_all("td")
  
    row = [i.text.rstrip() for i in tdTags]
    temp_list.append(row)

names=[]
distance=[]
mass=[]
radius=[]      
for i in range(0,len(temp_list)):
    names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

print(names)
print(distance)
print(mass)
print(radius)
    
    

for index,name in enumerate(names):
    final_data.append([name,distance[index],mass[index],radius[index]])
with open('Scraped_csv.csv','w',newline='',encoding='utf8')as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(final_data)