#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[34]:


#connect to website

URL = 'https://www.amazon.co.uk/Data-Analytics-Engineering-Business-Intelligence/dp/B0922P1MN8/ref=sr_1_1?crid=19WJCTPZACH5J&dib=eyJ2IjoiMSJ9.t1Hn3Z0OIjAOHrL8icexWbKqnkl2pQlJ_msjzB-zvPniyTR2mIc9f65XM9stoXkMixipa6IVG2RiNR6DCcv80uG800E03PAPqFZDglc3BTmPRHvheLZ0cFdvCPsionunnK9nmz1ObKzsNkPqwvtXXIq3EvKqdqVWYqX17yHGbjD5PZyh8Yjoq3DYlocJl5BCwQ1VPHaG7nnFOQAY9j6tegoYfyFOi3jo4nYEXr46q5nC2LZBxBOlLQdb4JzlBrsqah80EzLbR0RjqIqILcUst_uhx-e5zvYYGNkS0-3ivHw.npzSFHoO2N8tB4BD_zJUentreFkU0QimG4o59kKZ86Q&dib_tag=se&keywords=data+analytics+tshirt&qid=1716908935&sprefix=data+analytics+tshirt%2Caps%2C73&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

title = soup2.find(id='productTitle').get_text(strip=True)

price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text(strip=True)

print(title)
print(price[1:6])



# In[39]:


import datetime

today = datetime.date.today()

print(today)


# In[41]:


import csv

header = ['Title', 'Price','Date']
data = [title,price[1:6], today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[42]:


import pandas as pd

pd.read_csv(r"C:\Users\Owner\AmazonWebScraperDataset.csv")


# In[ ]:


#Now we are appending the data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[43]:


def check_price():
    URL = 'https://www.amazon.co.uk/Data-Analytics-Engineering-Business-Intelligence/dp/B0922P1MN8/ref=sr_1_1?crid=19WJCTPZACH5J&dib=eyJ2IjoiMSJ9.t1Hn3Z0OIjAOHrL8icexWbKqnkl2pQlJ_msjzB-zvPniyTR2mIc9f65XM9stoXkMixipa6IVG2RiNR6DCcv80uG800E03PAPqFZDglc3BTmPRHvheLZ0cFdvCPsionunnK9nmz1ObKzsNkPqwvtXXIq3EvKqdqVWYqX17yHGbjD5PZyh8Yjoq3DYlocJl5BCwQ1VPHaG7nnFOQAY9j6tegoYfyFOi3jo4nYEXr46q5nC2LZBxBOlLQdb4JzlBrsqah80EzLbR0RjqIqILcUst_uhx-e5zvYYGNkS0-3ivHw.npzSFHoO2N8tB4BD_zJUentreFkU0QimG4o59kKZ86Q&dib_tag=se&keywords=data+analytics+tshirt&qid=1716908935&sprefix=data+analytics+tshirt%2Caps%2C73&sr=8-1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    title = soup2.find(id='productTitle').get_text(strip=True)

    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text(strip=True)

    print(title)
    print(price[1:6])
    
    import datetime
    today = datetime.date.today()
    print(today)

    header = ['Title', 'Price','Date']
    data = [title,price[1:6], today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r"C:\Users\Owner\AmazonWebScraperDataset.csv")

df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




