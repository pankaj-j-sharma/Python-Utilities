import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re

product_names=[]
cookie={} # insert request cookies within{}
data_asin=[]
link=[]
reviews=[]
product_reviews=[]
final=[]

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

max_no_products=5 # this is for debug purpose only as we need to see only few products to spot check
review_pages=5 # max number of pages the scraper will look for reviews
prd_span_classes = {'class':'a-size-base-plus a-color-base a-text-normal'}
prd_asin_classes = {'class':"sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"}
prd_asin_classes = {"data-asin":True}
prod_title_classes = {'class':'a-size-large product-title-word-break'}

# get the search input from the user to search for
query=str(input("Enter search criteria \n"))

def get_amazon_search_result(query):
	url="https://www.amazon.in/s?k="+query
	print(url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"

def get_amazon_search_result_pg(query,pageno=1):
	''' this is for multi page search where specific pagenum is supplied '''
	url="https://www.amazon.in/s?k="+query+"&page="+str(pageno)
	print(url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"

def get_amazon_product_result(asin):
	url="https://www.amazon.in/dp/"+asin
	print(url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"
		
def get_amazon_prod_review_result(review_link):
	url="https://www.amazon.in"+review_link
	#print(url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"

response=get_amazon_search_result(query)
soup=BeautifulSoup(response.content , features="lxml")

# filter all product names and product ids i.e. ASIN from the response page
product_names = list(set([span.text for span in soup.findAll("span",prd_span_classes)]))
data_asin= list(set([div['data-asin'] for div in soup.findAll("div",prd_asin_classes) if div['data-asin']]))

# slicing as we need to show only max product as defined by variable for debug
data_asin=data_asin[:max_no_products]

# fetch the 'see all reviews' page for a product using the hyperlink present at the bottom 
for count,productid in enumerate(data_asin):
	dct={'title':'','href':'','id':productid}
	product_response=get_amazon_product_result(productid)
	soup=BeautifulSoup(product_response.content , features="lxml")
	for span in soup.findAll("span",prod_title_classes):
		dct['title']=re.sub(r'\W+', ' ', span.getText())	
	for atag in soup.findAll("a",{'data-hook':"see-all-reviews-link-foot"}):
		link.append(atag['href'])
		dct['href']=atag['href']
	final.append(dct)

# for each product review look through the pages defined by review_pages
for rev_lnk in link:
	for page in range(review_pages):
		reviews_response=get_amazon_prod_review_result(rev_lnk+'&pageNumber='+str(page))
		soup=BeautifulSoup(reviews_response.content , features="lxml")
		for span in soup.findAll("span",{'data-hook':"review-body"}):
			reviews.append(re.sub(r'\W+', ' ', span.text))

# creating product and reviews list
for dict in final:
	rev_lnk=dict['href']
	if rev_lnk =='':
		continue
	for page in range(review_pages):
		reviews_response=get_amazon_prod_review_result(rev_lnk+'&pageNumber='+str(page))
		soup=BeautifulSoup(reviews_response.content , features="lxml")
		for div in soup.findAll("div",{'data-hook':"review"}):
			for span in div.findAll("span",{'data-hook':"review-body"}):
				review_body = re.sub(r'\W+', ' ', span.getText())
			for atag in div.findAll("a",{'data-hook':"review-title"}):
				review_title = re.sub(r'\W+', ' ', atag.getText())
			for itag in div.findAll("i",{'data-hook':"review-star-rating"}):
				review_stars = itag.getText()
			
			product_reviews.append({'Id':dict['id'],'Title':dict['title'],'Review Title':review_title,'Review Rating':review_stars,'Review Text':review_body})


# print the fetched product names and ASIN nums
pprint.pprint(product_names)
pprint.pprint(product_reviews)
print('-'*90)
print(final,'\n')
print(link)
print('-'*90)

# display reviews and filter the non word characters 
# reviews = [re.sub(r'\W+', ' ', review) for review in reviews]

review_data=DataFrame(reviews) #converting this dictionary into a dataframe
review_data.to_csv('Scraping reviews.csv',index=False)
print(review_data.describe())

df=DataFrame(product_reviews,columns=['Id','Title','Review Title','Review Rating','Review Text']) #converting this dictionary into a dataframe
df.sort_values(by=['Title'], inplace=True)
df.to_csv('Scraping Product reviews.csv',index=False)
print(df.describe())
