import requests
from bs4 import BeautifulSoup

header={
 'authority': 'www.amazon.in' ,
 'pragma': 'no-cache' ,
 'cache-control': 'no-cache' ,
 'rtt': '50' ,
 'downlink': '2.5' ,
 'ect': '4g' ,
 'dnt': '1' ,
 'upgrade-insecure-requests': '1' ,
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36' ,
 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
 'sec-fetch-site': 'none' ,
 'sec-fetch-mode': 'navigate' ,
 'sec-fetch-user': '?1' ,
 'sec-fetch-dest': 'document' ,
 'accept-language': 'en-GB,en;q=0.9' ,
 'cookie': 'session-id=257-3700676-1869343; i18n-prefs=INR; ubid-acbin=257-2363739-6630506; session-token=rIAIqGvYT/BPi08VUfSQe3nmsoAEleekVQivR9b88s/HTM93h9nZFM2GBWrnA/prxknU/Lw5W0iZPlX60+H3SbtBhQfKbkFrUgj9I/jCdfN9PST3JZcwVATbUoN5Hph4NWimQe0+Wd6joSs6c+2BAmR6HwmjJKRJeUPKrHfKYbTM3OzGIYH/R9FqxOSc6DlAfqzypaIXMs/E2oF+OrI2HfXmnW17RyJlFtJNsHDWaT+M6MssagvjaHphvoL2rjoC; csm-hit=tb:s-DBNY2KN3BTEZWFQ6CBKY|1605637545603&t:1605637546437&adb:adblk_no; session-id-time=2082758401l' 
}

search_query="titan+men+watches"
base_url="https://www.amazon.in/s?k="
url=base_url+search_query

search_response=requests.get(url,headers=header)

search_response.text

cookie={} # insert request cookies within{}
def getAmazonSearch(search_query):
    url="https://www.amazon.in/s?k="+search_query
    print(url)
    page=requests.get(url,cookies=cookie,headers=header)
    if page.status_code==200:
        return page
    else:
        return "Error"

def Searchasin(asin):
    url="https://www.amazon.in/dp/"+asin
    print(url)
    page=requests.get(url,cookies=cookie,headers=header)
    if page.status_code==200:
        return page
    else:
        return "Error"
		
def Searchreviews(review_link):
    url="https://www.amazon.in"+review_link
    print(url)
    page=requests.get(url,cookies=cookie,headers=header)
    if page.status_code==200:
        return page
    else:
        return "Error"

product_names=[]
response=getAmazonSearch('titan+men+watches')
soup=BeautifulSoup(response.content , features="lxml")
for i in soup.findAll("span",{'class':'a-size-base-plus a-color-base a-text-normal'}): # the tag which is common for all the names of products
    product_names.append(i.text) #adding the product names to the list

print(product_names)

data_asin=[]
response=getAmazonSearch('titan+men+watches')
soup=BeautifulSoup(response.content , features="lxml")
for i in soup.findAll("div",{'class':"sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"}):
    data_asin.append(i['data-asin'])

print(data_asin)

link=[]
for i in range(len(data_asin)):
    response=Searchasin(data_asin[i])
    soup=BeautifulSoup(response.content , features="lxml")
    for i in soup.findAll("a",{'data-hook':"see-all-reviews-link-foot"}):
        link.append(i['href'])

reviews=[]
for j in range(len(link)):
    for k in range(10):
        response=Searchreviews(link[j]+'&pageNumber='+str(k))
        soup=BeautifulSoup(response.content , features="lxml")
        for i in soup.findAll("span",{'data-hook':"review-body"}):
            reviews.append(i.text)

response=getAmazonSearch('titan+men+watches&page=2')
soup=BeautifulSoup(response.content , features="lxml")
for i in soup.findAll("div",{'class':"sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"}):
    data_asin.append(i['data-asin'])

for i in range(len(data_asin)):
    response=Searchasin(data_asin[i])
    soup=BeautifulSoup(response.content , features="lxml")
    for i in soup.findAll("a",{'data-hook':"see-all-reviews-link-foot"}):
        link.append(i['href'])

for j in range(len(link)):
    for k in range(10):
        response=Searchreviews(link[j]+'&pageNumber='+str(k))
        soup=BeautifulSoup(response.content , features="lxml")
        for i in soup.findAll("span",{'data-hook':"review-body"}):
            reviews.append(i.text)

print(reviews)			
rev={'reviews':reviews} #converting the reviews list into a dictionary

import pandas as pd
review_data=pd.DataFrame.from_dict(rev) #converting this dictionary into a dataframe
review_data.describe()
			