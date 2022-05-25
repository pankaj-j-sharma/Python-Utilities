# setting up on ubuntu
# https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
# sudo apt-get install default-jdk
# sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
# sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# sudo apt-get -y update
# sudo apt-get -y install google-chrome-stable
# wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip

# sudo mv chromedriver /usr/bin/chromedriver
# sudo chown root:root /usr/bin/chromedriver
# sudo chmod +x /usr/bin/chromedriver

# wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar

# wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
# unzip testng-6.8.7.jar.zip

# xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar
# sudo apt-get install -y chromium-browser
# chromedriver --url-base=/wd/hub
# error with chrome exited 127 resolved by checking chrome version and driver version
# sudo apt install gconf2
# chromedriver --version
# google-chrome --version
# whereis chromedriver

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

property_urls=[]

##############################################################################################
def setup():
	# override max retries from the requests lib
	requests.adapters.DEFAULT_RETRIES = 10

	header={
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
	 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' ,
	 'cookie': '_ga=GA1.2.460746434.1606627342; usrDetPresent=Y; JSESSIONID=8427413BFDB0E8B6246C306A0CC6A66E-n1.MBAPP-176; alertRaisedCount=1; _col_uuid=bca30b6f-476a-4741-94b6-d48ee148369b-1sj7k; _fbp=fb.1.1606627345786.509052803; trackerCookie=Google_Organic; firstInteractionCookie=P; paidInteractionCookie=Y; userType=I; projectCategory=B; propCategory=Residential; Type=S; nearByLocGA=; lastSearchedLoc=; _gid=GA1.2.526092862.1606914904; PgPlotRedirection=Y; HDSESSIONID=b20e3e76-3b63-4051-bfca-a1619ac51e76; mbNps=Y; subPropertyTypeCookie="10002,10003,10021,10022"; subPropertyType="Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment"; propertyTypeCookie="Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment"; cityCookie=4320; cityCode=4320; cityNameCookie=Mumbai; subPropertyTypeText="Multistorey Apartment, Builder Floor Apartment, Penthouse, Studio Apartment"; cityNameTTvl=Mumbai; uniqUserSearchId=7af2e885cc3543d5a1f09d0d929871538ec9805f_1606915282482; cookieDtfirstIntr=20201203; SEARCHSESSIONID=d2f32e39-5ac2-433e-a021-3ccad4226602; viewedProperties=51546611; viewedPropertiesForDetails=51546611; DETAILSESSIONID=a51f5213-890b-42e9-8c4d-36f4046dbb1c; _hjTLDTest=1; _hjid=1cc1d06a-68c3-495c-b178-7fc35c0e9686; _hjFirstSeen=1; RSESSIONID=1D09EB39C5756539430EE7A1559B03B5-n2.RTNG55; EXT_RMKT=43707%2C43831; GEN_RMB=1303271%2C1302575%2C1301925; SHWN_GEN_RMB=1302575%2C1303271%2C1301925; ConRec=N; ConRecUser=Builder; showForm=A; _gali=resultDiv',
	}

	cookie = {}

	url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Mumbai'
	url_page = 'https://www.magicbricks.com/mbsearch/propertySearch.html?propertyType_new=10002_10003_10021_10022&postedSince=-1&city=4320&searchType=1&propertyType=10002,10003,10021,10022&disWeb=Y&pType=10002,10003,10021,10022&category=S&cusImgCount=0&groupstart={group_start}&offset=0&maxOffset=229&attractiveIds=&page=2&ltrIds=51388062,51545101&preCompiledProp=&excludePropIds=&addpropertyDataSet='
	
	load_prop_worth_data = 'https://www.magicbricks.com/mbsearch/mbApiproxy/getpropworth?id=50974034'

	properties = []
	df= pd.DataFrame()
	screen=0

	return header,cookie,url,url_page,properties,df,screen

##############################################################################################
def extract_property_urls(urls):
	pattern = '((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
	result=[]
	for url in urls:
		result.append(re.search(pattern,url).group())
		
	return result
	
##############################################################################################
def get_search_result(url,cookie,header,retries=5):
	while True:
		try:
			page=requests.get(url,cookies=cookie,headers=header)
			if page.status_code==200:
				return page
			else:
				return "Error "+page.status_code
		except Exception as e:
			if retries==0:
				return "Error after retries "
			print('retrying ',retries)
			retries-=1
##############################################################################################		
def load_full_page_with_selenium(url):

	driver=webdriver.Chrome('C:\\Interviews\\chromedriver_win32\\chromedriver')
	driver.get(url)

	home_title='MagicBricks'

	start = datetime.now()
	try:
		WebDriverWait(driver, 15).until(ec.title_contains(home_title))
	except TimeoutException:
		print("Too much time to load the page ")

	sleep(3)

	# item list page and implementation for infinte scroll
	scroll_pause_time = 3
	screen_height = driver.execute_script("return window.screen.height;")

	i = 1
	scroll_height=0

	while True:
		# scroll one screen height each time
		#driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i)) 
		driver.execute_script("window.scrollTo(0, {scroll_height}-10);".format(scroll_height=scroll_height)) 
		i += 1
		# Assuming modal appeared 
		if i%5 == 0:
			driver.execute_script("hideExitIntent();")
		sleep(scroll_pause_time)
		if not driver.execute_script("return document.body.scrollHeight;") == scroll_height:
			scroll_height = driver.execute_script("return document.body.scrollHeight;")
			print('scroll_height -> ',scroll_height)
		else:
			scroll_height = driver.execute_script("return document.body.scrollHeight;")  
			# Break the loop when the height we need to scroll to is larger than the total scroll height
			if (screen_height) * i > scroll_height:
				break		
	# item list page and implementation for infinte scroll 
	return driver.page_source


##############################################################################################
def launch_selenium(url):

	options = webdriver.ChromeOptions()
	options.add_argument("no-sandbox")
	options.add_argument("--disable-gpu")
	options.add_argument("--window-size=800,600")
	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("--headless")
	options.add_argument('--remote-debugging-port=4444')
	options.add_argument('--log-level=1')	

	driver = None
	if os.name == 'nt':
		driver=webdriver.Chrome('C:\\Interviews\\chromedriver_win32\\chromedriver')
	else:
		driver=webdriver.Chrome(options=options)

	driver.get(url)
	home_title='MagicBricks'
	start = datetime.now()
	try:
		WebDriverWait(driver, 55).until(ec.title_contains(home_title))
	except TimeoutException:
		print("Too much time to load the page ")
	sleep(3)
	return driver

##############################################################################################    
def load_part_page_with_selenium(driver,scroll_height,i):

	# item list page and implementation for infinte scroll
	scroll_pause_time = 3
	loop = True
	screen_height = driver.execute_script("return window.screen.height;")
	driver.execute_script("window.scrollTo(0, {screen_height}*{i}-100);".format(screen_height=scroll_height, i=i))  
	# Assuming modal appeared 
	#if i%5 == 0:
		#driver.execute_script("hideExitIntent();")
	sleep(scroll_pause_time)

	if not driver.execute_script("return document.body.scrollHeight;") == scroll_height:
		scroll_height = driver.execute_script("return document.body.scrollHeight;")
		#print('scroll_height -> ',scroll_height)
	else:
		scroll_height = driver.execute_script("return document.body.scrollHeight;")  
		# Break the loop when the height we need to scroll to is larger than the total scroll height
		if (screen_height) * i > scroll_height:
			loop=False
	return loop,driver.page_source,scroll_height

##############################################################################################
def parse_html_response(soup,properties):
	break_exec = False
	for container in soup.findAll('div',{'class':'m-srp-card__container'}):
		prop_title=''
		prop_price=''
		prop_desc=''
		prop_text=''
		summary_data={}
		global property_urls
		
		spandata = container.parent
		if spandata.get('data-code').strip() in property_urls:
			break_exec = True
			break
		else:
			property_urls.append(spandata.get('data-code').strip())
		
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

		properties.append({'title':prop_title,'price':amt,'short_text':prop_text, 'description':prop_desc, 'summary_data':summary_data})
		print(str(amt).ljust(10,' '),'->',prop_title)
		#pprint.pprint(summary_data)
	return properties,break_exec

##############################################################################################
def flatten_summary_item(properties):
	keys=[]
	for property in properties:
		for k in property['summary_data'].keys():
			keys.append(k)
	
	keys = list(set(keys))
	
	for property in properties:
		for key in keys:
			if property['summary_data'].get(key):
				property[key] = property['summary_data'][key]
			else:
				property[key]=" "
		del property['summary_data']

	return properties
	
##############################################################################################
def load_dataframe(properties):
	df=pd.DataFrame(properties)
	print('df info '.center(70,'*'))
	print(df.info())
	print('\n')
	print('df unique info '.center(70,'*'))
	print(df.nunique())
	print('\n')
	print('df duplicates '.center(70,'*'))
	print('Number of duplicates -> ',len(df[df.duplicated()]))
	print('\n')
	df_unique = df[~df.duplicated()]
	df_unique.to_csv('property_data_05122020.csv',index=False)
	
##############################################################################################
def call_via_selenium_load():
	header,cookie,url,url_page,properties,df,screen = setup()
	chrome_driver = launch_selenium(url)
	scroll_height = 0
	
	while True:
		screen+=1
		loop,response,scroll_height = load_part_page_with_selenium(chrome_driver,scroll_height,screen)
		print('loop =>',loop,'scrollHeight =>',scroll_height)
		if not loop:
			break
		soup=BeautifulSoup(response , features="lxml")
		properties = parse_html_response(soup,properties)
		print('No of properties loaded -> ',len(properties))

	# pprint.pprint(properties)
	load_dataframe(properties)
	
##############################################################################################	
def call_via_request():
	global property_urls
	start = datetime.now()
	header,cookie,url,url_page,properties,df,screen = setup()
	
	try:
		for i in range(0,42000,30):
			response = get_search_result(url_page.format(group_start=str(i)),cookie,header)
			if isinstance(response,str):
				break		
			soup=BeautifulSoup(response.content , features="lxml")
			properties,stop = parse_html_response(soup,properties)
			if stop:
				break
			#print('+'*150)
			#pprint.pprint(property_urls)
			#print('+'*150)
			print('\n',(str(len(properties))+' properties ').center(60,'*'),'\n')
	except Exception as e:
		print('Eror with ',i,' ',str(e))
	
	properties = flatten_summary_item(properties)
	with open('prperty_urls_data.txt','w+') as f:
		for url in extract_property_urls(property_urls):
			f.write(url)
	load_dataframe(properties)
	print('Time taken ->',datetime.now() - start)
	
call_via_request()