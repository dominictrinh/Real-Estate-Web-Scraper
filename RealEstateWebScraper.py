#!/usr/bin/env python
# coding: utf-8

# In[307]:


import pandas
import requests
from bs4 import BeautifulSoup

site = ""

while "https://webcache.googleusercontent.com" not in site:
    site = input("Please enter the cached version of the real estate website you would like to view.")

r = requests.get(site.strip(), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content


soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"list-card-info"})

l = []

for item in all:
    d = {}
    #address
    d["Address"] = item.find("address", {"class":"list-card-addr"}).text
    
    #price
    d["Price"] = item.find("div", {"class":"list-card-price"}).text
    
    #bedrooms, baths, sq ft
    d["Bedrooms"] = item.find_all("li", {"class":""})[0].text
    d["Bathrooms"] = item.find_all("li", {"class":""})[1].text
    d["Square Feet"] = item.find_all("li", {"class":""})[2].text
    
    #type of house
    d["House Type"] = item.find("li", {"class":"list-card-statusText"}).text
    
    print(" ")
    
    l.append(d)

#output data to a table
listings = pandas.DataFrame(l)
listings.to_csv("output_csv")
pandas.set_option('display.max_rows', len(l))

print(listings)


# In[ ]:





# In[ ]:




