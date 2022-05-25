import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re
import os
import json
import xmltodict 
from collections import OrderedDict
from selenium import webdriver
from datetime import datetime
import lxml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pprint
from time import sleep

class Scrapper():
	def __init_(self,url=None,header=None,retries=5):
		self.header=header
		self.cookie={}
		self.url=url
		self.retries=retries
		requests.adapters.DEFAULT_RETRIES = retries
		self.df = pd.DataFrame()
		self.screen = 0
	
	def get_search_result(self,purl=None):
		retries = self.retries
		url = purl if purl else self.url
		while True:
			try:
				self.page=requests.get(url,cookies=self.cookie,headers=self.header)
				if not self.page.status_code==200:
					self.err="Error loading the page"
			except Exception as e:
				if retries==0:
					self.err="Error after retries "
				print('retrying ',retries)
				retries-=1
	
	def parse_with_beautifulsoup(self):
		if self.page.status_code == 200:
			self.soup = BeautifulSoup(self.page.content , features="lxml")

	def launch_selenium(self,home_title):
		options = webdriver.ChromeOptions()
		options.add_argument("no-sandbox")
		options.add_argument("--disable-gpu")
		options.add_argument("--window-size=800,600")
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--headless")
		options.add_argument('--remote-debugging-port=4444')
		options.add_argument('--log-level=1')		
		if os.name == 'nt':
			self.driver=webdriver.Chrome('C:\\Interviews\\chromedriver_win32\\chromedriver')
		else:
			self.driver=webdriver.Chrome(options=options)
		
		if self.url:
			try:
				WebDriverWait(self.driver, 55).until(ec.title_contains(home_title))
			except TimeoutException:
				self.err = "Too much time to load the page "
			sleep(3)		
		
	def load_into_dataframe(self,print_to_csv=False):
		if self.resultset:
			self.df=pd.DataFrame(self.resultset)
			print('df info '.center(70,'*'))
			print(self.df.info())
			print('\n')
			print('df unique info '.center(70,'*'))
			print(self.df.nunique())
			print('\n')
			print('df duplicates '.center(70,'*'))
			print('Number of duplicates -> ',len(self.df[self.df.duplicated()]))
			print('\n')
			self.df = self.df[~self.df.duplicated()]
			if print_to_csv:
				self.df.to_csv('property_data_05122020.csv',index=False)

#####################################################################################

class MagicBricks(Scrapper):

	__header = {
	 'authority': 'ingestor.magicbricks.com' ,
	 'pragma': 'no-cache' ,
	 'cache-control': 'no-cache' ,
	 'accept': 'application/json, text/javascript, */*; q=0.01' ,
	 'dnt': '1' ,
	 'x-requested-with': 'XMLHttpRequest' ,
	 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' ,
	 'content-type': 'application/json' ,
	 'origin': 'https://ingestor.magicbricks.com' ,
	 'sec-fetch-site': 'same-origin' ,
	 'sec-fetch-mode': 'cors' ,
	 'sec-fetch-dest': 'empty' ,
	 'referer': 'https://ingestor.magicbricks.com/server.html' ,
	 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' 
	 }
	 
	 __pattern = '((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
	 
	def __init__(self):
		super().__init__(header=MagicBricks.__header)
		self.property_urls=[]
		self.properties = []

	def get_mb_search_results(gpstart,pageno):
		self.get_search_result()
	
	def extract_properties_from_html(self):
		self.break_exec = False
		for container in self.soup.findAll('div',{'class':'m-srp-card__container'}):
			prop_title=''
			prop_price=''
			prop_desc=''
			prop_text=''
			summary_data={}
			
			if container.parent.get('data-code').strip() in self.property_urls:
				self.break_exec = True
				break
			else:
				self.property_urls.append(container.parent.get('data-code').strip())
			for title in container.findAll('span',{'class':'m-srp-card__title'}):
				prop_title = re.sub('\W+',' ',title.getText())
			for summary in container.findAll('div',{'class':'m-srp-card__summary__item'}):
				summary_title = summary.findAll("div",{"class":"m-srp-card__summary__title"})[0].getText().strip().lower()
				summary_info = summary.findAll("div",{"class":"m-srp-card__summary__info"})[0].getText().strip().lower()
				summary_title = re.sub('\W+',' ',summary_title)
				summary_info = re.sub('\W+',' ',summary_info)
				summary_data[summary_title] = summary_info
			for description in container.findAll('div',{'class':'m-srp-card__description'}):
				prop_desc = re.sub('\W+',' ',description.contents[0])
			for short_text in container.findAll('span',{'class':'m-srp-card__usp__text'}):
				prop_text = re.sub('\W+',' ',short_text.getText())
			for price in container.findAll('div',{'class':'m-srp-card__info'}):
				prop_price = price.contents[1].text.lower()
				curr = re.sub('\d|\.','',prop_price).strip()
				amt = re.sub('[A-Za-z]','',prop_price).strip()
				if curr == 'cr':
					amt = int(float(amt)*(10**6))
				elif curr == 'lac':
					amt = int(float(amt)*(10**4))
				#print("{:,}".format(amt))

			self.properties.append({'title':prop_title,'price':amt,'short_text':prop_text, 'description':prop_desc, 'summary_data':summary_data})
			#print(str(amt).ljust(10,' '),'->',prop_title)
			#pprint.pprint(summary_data)

###########################################################################################################################
if __name__=='__main__':
	scrapper = MagicBricks()
	for i in range(0,42000,30)
		scrapper.get_search_result()