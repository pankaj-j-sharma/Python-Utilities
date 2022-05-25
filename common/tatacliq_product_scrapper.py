import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re
from requests_html import HTMLSession
import pyppdf.patch_pyppeteer

# had to use older version of urllib to make it work
# pip install -U "urllib3<1.25"

base_url='https://www.tatacliq.com/'
trail_url=''
product_names=[]
prod_url=[]
cookie={} # insert request cookies within{}
link=[]
reviews=[]
debug_counter=1000

header={
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'DNT': '1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Language': 'en-GB,en;q=0.9'
}



#https://www.tatacliq.com/marketplacewebservices/v2/mpl/products/searchProducts/?searchText=mobiles%3Arelevance%3AinStockFlag%3Atrue&isKeywordRedirect=false&isKeywordRedirectEnabled=true&channel=WEB&isMDE=true&isTextSearch=false&isFilter=false&page=3&isPwa=true&pageSize=40&typeID=all

#https://www.tatacliq.com/marketplacewebservices/v2/mpl/products/searchProducts/?searchText=fridge%3Arelevance%3AinStockFlag%3Atrue&isKeywordRedirect=false&isKeywordRedirectEnabled=true&channel=WEB&isMDE=true&isTextSearch=false&isFilter=false&page=0&isPwa=true&pageSize=40&typeID=all


# get the search input from the user to search for
query=str(input("Enter search criteria \n"))

#######################################################################################
def get_parsed_html(content):
	return BeautifulSoup(content , features="lxml")

#######################################################################################
def get_tatacliq_search_result(query):
	global cookie
	query=query.replace(" ","%20")                            
	url="https://www.tatacliq.com/search/?searchCategory=all&text="+query
	print('search_result -> ',url)
	page=requests.get(url,cookies=cookie,headers=header)
	cookie=page.cookies.get_dict()
	print(cookie)
	
	# print(dir(page),'\n','*'*60)
	# for k in dir(page):
		# if not '__' in k:
			# print(k,' -> ',getattr(page,k),'\n')
	#print(page.cookies.get_dict())
	# pprint.pprint(page.headers.get('Set-Cookie'))
	
	# # using session to retrieve cookie data 
	# session = HTMLSession()
	# print('*'*100)
	# print(session.cookies.get_dict())	
	# print('*'*100)
	# ses_response = session.get(url,cookies=cookie,headers=header)
	# ses_response.html.render()
	# print(ses_response.cookies.get_dict())
	# pprint.pprint(ses_response.headers.get('Set-Cookie'))
	# return ses_response
	
	page.status_code=100
	if page.status_code==200:
		return page
	else:
		return "Error"
		
#######################################################################################
def get_tatacliq_search_result_pg(query,pageno=1):
	''' this is for multi page search where specific pagenum is supplied '''
	url="https://www.flipkart.com/search?q="+query+"&page="+str(pageno)
	#print(url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"		
		
#######################################################################################
def get_tatacliq_product_result(href):
	url="https://www.flipkart.com"+href
	print('product_result -> ',url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"
		
#######################################################################################
def get_tatacliq_prod_review_result(review_link):
	url=base_url+review_link
	print('prod_review_result -> ',url)
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"

#######################################################################################
def get_tatacliq_prod_links(search_page):
	counter=0
	product_names=[]
	prod_url=[]
	print('prod_links -> ')
	for div in search_page.findAll("div",{"data-id":True}):
		counter+=1
		if counter>debug_counter:
			break
		for sub in div.findAll("a",{"class":True}):
			prod_url.append(sub['href'])
			for atagsub in sub.findAll('div',{"class":"_4rR01T"}):
				product_names.append(atagsub.getText())
			
		for subdiv in div.findAll("a",{"class":"IRpwTa"}):
			print(subdiv.text,' -> ',subdiv['href'],'\n')
			product_names.append(subdiv.text)
			prod_url.append(subdiv['href'])

		for span in div.findAll("a","s1Q9rs"):
			product_names.append(span.text)
			prod_url.append(span['href'])
			
	return list(set(product_names)),list(set(prod_url))

#######################################################################################
def get_tatacliq_prod_review_links(product_url):
	counter=0
	link=[]
	link_not_found=[]
	print('prod_review_links -> ',[p[:30] for p in product_url])
	for url in product_url:
		atag=""
		counter+=1
		if counter>debug_counter:
			break
		product_response=get_tatacliq_product_result(url)
		soup=get_parsed_html(product_response.content)
		for div in soup.findAll("div",{'class':"_3UAT2v"}):
			if div.parent.name=='a':
				atag=div.parent
				link.append(atag['href'])
		if atag=="":
			link_not_found.append(url)
	return list(set(link)),list(set(link_not_found))

#######################################################################################
def extract_tatacliq_reviews_data(review_page):
	counter=0
	reviews=[]
	name=""
	print('reviews_data -> ')
	for review in review_page:
		name=""
		counter+=1
		if counter>debug_counter:
			break
		review_response = get_tatacliq_prod_review_result(review)
		soup=get_parsed_html(review_response.content)
		cnt=0
		for div in soup.findAll('div',{'class':'_2s4DIt'}):
			if name=="":
				name = div.getText()
		for div in soup.findAll('div',{'class':'_1AtVbE col-12-12'}):
			dct={'Title':name,'Review Title':'','Review Rating':'','Review Text':''}
			for subdiv in div.findAll('div',{'class':'row'}):
				if subdiv['class']==['row']:
					cnt+=1
					if cnt>debug_counter:
						break
					for rdiv in subdiv.findAll('div',{'class':'_3LWZlK'}):
						if rdiv.getText() and rdiv.getText()!="":
							dct['Review Rating']=rdiv.getText()
					for p in subdiv.findAll('p',{'class':'_2-N8zT'}):
						if p.getText() and p.getText()!="":
							dct['Review Title']=p.getText()
					for bdiv in subdiv.findAll('div',{'class':'_6K-7Co'}):
						if bdiv.getText() and bdiv.getText()!="":
							dct['Review Text']=re.sub(r'\W+', ' ', bdiv.getText())
					if dct['Review Text']=="":
						for bdiv in subdiv.findAll('div',{'class':'t-ZTKy'}):
							for bsdiv in bdiv.findAll('div',{'class':True}):
								if bsdiv.getText() and bsdiv.getText()!="":
									dct['Review Text']=re.sub(r'\W+', ' ', bsdiv.getText())
			if dct['Review Text'] !='':
				reviews.append(dct)
	return reviews

#######################################################################################
def get_tatacliq_prod_page_reviews(product_url):
	counter=0
	reviews=[]
	print('reviews_data on prd page -> ')
	print('prod_review_links -> ',[p[:30] for p in product_url])
	for url in product_url:
		counter+=1
		name=""
		if counter>debug_counter:
			break
		product_response=get_tatacliq_product_result(url)
		soup=get_parsed_html(product_response.content)
		
		for span in soup.findAll("span",{'class':"B_NuCI"}):
			if name=="":
				name = span.getText()
		for div in soup.findAll("div",{'class':"_16PBlm"}):
			dct={'Title':name,'Review Title':'','Review Rating':'','Review Text':''}
			for subdiv in div.findAll('div',{'class':'row'}):
				if subdiv['class']==['row']:
					for rdiv in subdiv.findAll('div',{'class':'_3LWZlK'}):
						if rdiv.getText() and rdiv.getText()!="":
							dct['Review Rating']=rdiv.getText()
					for p in subdiv.findAll('p',{'class':'_2-N8zT'}):
						if p.getText() and p.getText()!="":
							dct['Review Title']=p.getText()
					for bdiv in subdiv.findAll('div',{'class':'_6K-7Co'}):
						if bdiv.getText() and bdiv.getText()!="":
							dct['Review Text']=re.sub(r'\W+', ' ', bdiv.getText())
					if dct['Review Text']=="":
						for bdiv in subdiv.findAll('div',{'class':'t-ZTKy'}):
							for bsdiv in bdiv.findAll('div',{'class':True}):
								if bsdiv.getText() and bsdiv.getText()!="":
									dct['Review Text']=re.sub(r'\W+', ' ', bsdiv.getText())
			if dct['Review Text'] !='':
				reviews.append(dct)
				# print('#'*10,dct,'#'*10)
	return reviews

#######################################################################################
def print_tatacliq_data_to_csv(reviews):
	df=DataFrame(reviews,columns=['Title','Review Title','Review Rating','Review Text']) #converting this dictionary into a dataframe
	df.sort_values(by=['Title'], inplace=True)
	df.to_csv('Scraping Flipkart Product reviews.csv',index=False)
	
#######################################################################################
if __name__=='__main__':
	response = get_tatacliq_search_result(query)
	# soup = get_parsed_html(response.content)
	# product_names,prod_url=get_tatacliq_prod_links(soup)
	# print('-'*100)
	# pprint.pprint(product_names)
	# print('-'*100)
	# pprint.pprint([u[:30] for u in prod_url])	
	# link,link_not_found = get_tatacliq_prod_review_links(prod_url)
	# if len(link_not_found)>0:
		# if len(link)==0:
			# reviews = get_tatacliq_prod_page_reviews(link_not_found)
		# else:
			# reviews = get_tatacliq_prod_page_reviews(link_not_found) + extract_tatacliq_reviews_data(link)
		# print('-'*100)
	# else:
		# pprint.pprint([l[:30] for l in link])	
		# reviews = extract_tatacliq_reviews_data(link)
		# print('-'*100)
	# pprint.pprint(reviews)
	# print_tatacliq_data_to_csv(reviews)