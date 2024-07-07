import csv
import requests
from bs4 import BeautifulSoup


response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
##print(f"response is: {response}")
##print(f"response.text is: {response.text}")
bs = BeautifulSoup(response.text,"lxml")
print(bs.title)
print(bs.title.text)
print(bs.h1)
print("felix")
print(bs.find(name=None, attrs={}, recursive=True, string=None))
print(bs.find("p").text)
tableofcontents = bs.find("div",class_="toc")
print(tableofcontents)
print(bs.find("div",{"class": "toc"}) )
headings = bs.find(tableofcontents.find_all("li"))
data = []
for heading in headings:
    headtext = heading.find("span", class_="toctext").text
    headnum = heading.find("span",class_="tocnumber").text
    data.append({
        'heading_number': headnum,
        'heading_text': headtext,
    })
with open(data.csv, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['heading_number', 'heading_text'])
    writer.writeheader()
    writer.writerows(data)