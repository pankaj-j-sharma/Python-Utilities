from selenium import webdriver
import lxml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pprint
import bs4
import re
from time import sleep

result=[]
category_items={}

url="https://curiositystream.com/categories/"

# https://phantomjs.org/download.html
#driver = webdriver.PhantomJS(executable_path='C:\\Interviews\\phantomjs\\bin\\phantomjs')

#https://chromedriver.chromium.org/downloads
driver=webdriver.Chrome('C:\\Interviews\\chromedriver_win32\\chromedriver')
driver.get(url)

try:
	WebDriverWait(driver, 10).until(ec.title_is('CuriosityStream - Browse'))
except TimeoutException:
	print("Too much time to load the page ")

sleep(4)

for i in range(len(driver.find_elements_by_css_selector('div.styles__category___3-jGU'))):

	# reinstating the element as it gives stale element error 
	ele = driver.find_elements_by_css_selector('div.styles__category___3-jGU')
	
	title=ele[i].find_element_by_css_selector('span.styles__title___1Vsjl').text
	url = ele[i].get_attribute('style').split(',')[-1].strip().replace('\n','')

	dct={'category':title,'cat_img_url':url,'items':[]}
		
	ele[i].click()
	sleep(3)
	
	# item list page and implementation for infinte scroll
	scroll_pause_time = 1
	screen_height = driver.execute_script("return window.screen.height;")
	i = 1
	scroll_height=0

	while True:
		# scroll one screen height each time
		driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
		i += 1
		sleep(scroll_pause_time)
		if not driver.execute_script("return document.body.scrollHeight;") == scroll_height:
			scroll_height = driver.execute_script("return document.body.scrollHeight;")
			print('scroll_height -> ',scroll_height)
		else:
			scroll_height = driver.execute_script("return document.body.scrollHeight;")  
			# Break the loop when the height we need to scroll to is larger than the total scroll height
			if (screen_height) * i > scroll_height:
				break		
		
	for item in driver.find_elements_by_css_selector('div.card-grid-item'):
		cat_item = item.find_element_by_css_selector('span.styles__mediaTitle___1AIaV').text
		# click on more button 
		#item.find_element_by_css_selector('div.styles__cardMask___3Xs4S').click()
		#sleep(2)
		#cat_item += driver.find_element_by_css_selector('p.styles__producer___1c-2e').text()
		#driver.find_element_by_css_selector('a.styles__closeButton___3V0TG styles__link___5tkGI').click()
		#sleep(1)
		dct['items'].append(cat_item)
	result.append(dct)
	driver.back()
	sleep(3)


pprint.pprint(result)

driver.quit()