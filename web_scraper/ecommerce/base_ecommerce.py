import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re
import json

class Scrapper:

	def __init__(self,provider=None):
		self.cookie={}
		self.provider = provider
		self.__load_config_for_provider(provider)

		
	def logger(func):
		def wrapper(*args,**kwargs):
			print('calling -> ',func.__name__)
			return func(*args,**kwargs)
		return wrapper

		
	@logger
	def __load_config_for_provider(self,provider):
		config = {"url": ""}
		with open('config/{}.json'.format(provider)) as conf:
			config = json.load(conf)
		self.config = config

		
	def __get_page(self,url):
		print('fetch ->',url)
		return requests.get(url,cookies=self.cookie,headers=self.config["header"])
	

	def get_parsed_html(self,features="lxml"):
		return BeautifulSoup(self.page.content , features=features)		

	@logger		
	def get_search_result(self,keywords,pageno=1):
		keywords=keywords.replace(" ","%20")                            
		url = self.config["base_url"].format(keywords=keywords,pageno=pageno)		
		page=self.__get_page(url)
		if page.status_code==200:
			self.page = page
		else:
			self.page = None
			self.err = "An error occurred loading the page"

	def print_data_to_csv(self,data):
		print('data print_data_to_csv',data)
		df=DataFrame(data,self.config["columns"]) #converting this dictionary into a dataframe
		print('df print_data_to_csv',df)
		df.sort_values(by=self.config["sort_by"], inplace=True)
		df.to_csv('{provider}_Product_reviews.csv'.format(provider=self.provider),index=False)

	@logger
	def save_data_to_json(self,data):
		with open('data/{provider}_Product_reviews.json'.format(provider=self.provider),'w+') as f:
			json.dumps(data,f)
	
	@logger
	def get_product_page(self,product):
		page=self.__get_page(self.config["prod_url"].format(product=product))
		if page.status_code==200:
			self.page = page
		else:
			self.page = None
			self.err = "An error occurred loading the page"	
			