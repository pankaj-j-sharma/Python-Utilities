from base_ecommerce import Scrapper
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re
import json

class Flipkart(Scrapper):
	
	def __init__(self):
		super().__init__('flipkart')
		self.counter=0
		self.product_names=[]
		self.prod_url=[]
		self.link=[]
		self.link_not_found=[]		
		self.reviews = []
		self.debug_counter=10
	
	@Scrapper.logger
	def get_product_links(self,search_page):
		self.counter=0
		for div in search_page.findAll(self.config['search_prod'][0],self.config['search_prod'][1]):
			self.counter+=1
			if self.counter>self.debug_counter:
				break
			for sub in div.findAll(self.config['link_prod'][0][0],self.config['link_prod'][0][1]):
				print('href -> ',sub['href'][:50])
				self.prod_url.append(sub['href'])
				for atagsub in sub.findAll(self.config[ 'name_prod'][0],self.config['name_prod'][1]):
					self.product_names.append(atagsub.getText())
				
			for subdiv in div.findAll(self.config['link_prod'][1][0],self.config['link_prod'][1][1]):
				self.product_names.append(subdiv.text)
				self.prod_url.append(subdiv['href'])

			for span in div.findAll(self.config['link_prod'][2][0],self.config['link_prod'][2][1]):
				self.product_names.append(span.text)
				self.prod_url.append(span['href'])
				
		self.product_names =list(set(self.product_names))
		self.prod_url = list(set(self.prod_url))
		return self.prod_url

	@Scrapper.logger
	def get_product_review_links(self,product_url):
		self.counter=0
		for url in product_url:
			atag=""
			self.counter+=1
			if self.counter>self.debug_counter:
				break
			product_response=self.get_product_page(url)
			soup=self.get_parsed_html()
			for div in soup.findAll(self.config['link_review'][0],self.config['link_review'][1]):
				if div.parent.name=='a':
					atag=div.parent
					self.link.append(atag['href'])
			if atag=="":
				self.link_not_found.append(url)
		self.link = list(set(self.link))
		self.link_not_found = list(set(self.link_not_found))
		return self.link,self.link_not_found

	@Scrapper.logger
	def get_product_page_reviews(self,product_url):
		self.counter=0
		for url in product_url:
			self.counter+=1
			name=""
			if self.counter>self.debug_counter:
				break
			product_response=self.get_product_page(url)
			soup=self.get_parsed_html()
			
			for span in soup.findAll(self.config['title_review'][0],self.config['title_review'][1]):
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
					self.reviews.append(dct)
					# print('#'*10,dct,'#'*10)

	@Scrapper.logger
	def get_reviews_data(self,review_page):
		self.counter=0
		name=""
		for review in review_page:
			name=""
			self.counter+=1
			if self.counter>self.debug_counter:
				break
			review_response = self.get_product_page(review)
			soup=self.get_parsed_html()
			cnt=0
			for div in soup.findAll('div',{'class':'_2s4DIt'}):
				if name=="":
					name = div.getText()
			for div in soup.findAll('div',{'class':'_1AtVbE col-12-12'}):
				dct={'Title':name,'Review Title':'','Review Rating':'','Review Text':''}
				for subdiv in div.findAll('div',{'class':'row'}):
					if subdiv['class']==['row']:
						cnt+=1
						if cnt>self.debug_counter:
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
					self.reviews.append(dct)

	@Scrapper.logger
	def save_reviews(self,csv=False):
		if csv:
			self.print_data_to_csv(self.reviews)
		else:
			self.save_data_to_json(self.reviews)
	
	def get_all_saved_data(self):
		print('Product URL -> ',self.prod_url)
		print('Product Names -> ',self.product_names)
		print('Links URL -> ',self.link)
		print('Link not found -> ',self.link_not_found)
		print('Reviews -> ')
		pprint.pprint(self.reviews)
		
		