import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pprint
import re
from requests_html import HTMLSession
import scrapy

cookie={}
url=""
query="https://curiositystream.com/categories/1"
query="https://www.voot.com/"
splash_url="http://incampus.co.in:8050/"

# scrapy startproject taskassignment
# docker run -d -p 80:80 docker/getting-started
# docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash

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

def get_url(url):
	session = HTMLSession()
	r = session.get(url)
	r.html.render()
	return r
	page=requests.get(url,cookies=cookie,headers=header)
	if page.status_code==200:
		return page
	else:
		return "Error"

		
response=get_url(query)
print(response.content)
