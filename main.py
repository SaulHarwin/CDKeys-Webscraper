import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.cdkeys.com/daily-deals"

results = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")
items_ = soup.find(class_="product-items__filter-by-region")
items_ = items_.findAll("div", {"class": "product-item-details"}) 

items = []

for i in items_:
    itemUrl = i.find("a")['href']
    
    videoFetch = requests.get(itemUrl)
    soup = BeautifulSoup(videoFetch.text, "html.parser")
    video = soup.find("div", {"id":"videos"})

    item = {
        "Name": i.find("a").getText(),
        "Price": [i.findAll("span", {"class": "price"})[0].getText(), i.findAll("span", {"class": "price"})[1].getText()],
        "Link": itemUrl,
        "video": video
        }
    
    items.append(item)