from selenium import webdriver
from datetime import datetime
import lxml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pprint
import bs4
import re
from time import sleep

result={}
url_list=[]
category_items={}

url="https://www.voot.com/"

driver=webdriver.Chrome('C:\\Interviews\\chromedriver_win32\\chromedriver')
driver.get(url)

home_title='VOOT - Watch Free Online TV Shows, Movies, Kids Shows HD Quality on VOOT. Keep Vooting.'

start = datetime.now()
try:
	WebDriverWait(driver, 15).until(ec.title_is(home_title))
except TimeoutException:
	print("Too much time to load the page ")

sleep(3)

debug=""

# switch tabs when multiple opened
#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
# perform ctrl + click
#ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()


# item list page and implementation for infinte scroll
scroll_pause_time = 3
screen_height = driver.execute_script("return window.screen.height;")
i = 1
scroll_height=0

while False:
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
# item list page and implementation for infinte scroll
			
for i,element in enumerate(driver.find_elements_by_class_name('carouselTray')):
	title = []
	# print('source start'.center(70,'*'))
	# print(element.find_element_by_class_name('slick-initialized').get_attribute('innerHTML'))
	tray_header = str(i+1)+' -> '+re.sub(r'\W+', ' ',element.find_element_by_tag_name('h3').text)
	# print('source end'.center(70,'*'))
	# print('\n')
	try:
		while True:
			for im in element.find_elements_by_tag_name('img'):
				if im.get_attribute('title'):
					url_list.append({im.get_attribute('title'):im.get_attribute('src')})
			for el in element.find_elements_by_tag_name('h4'):
				if el.text and el.text!='':
					title.append(el.text)
			
			if i==2:
				im.find_element_by_xpath('..').find_element_by_xpath('..').click()
				sleep(3)
				break
			button= element.find_element_by_class_name('slick-next')
			if len(button.get_attribute('class').split(' '))==2:
				button.click()
				sleep(1)
				# print('button -> ',button.get_attribute('class'))
			else:
				break
				print(url_list,'\n')
		result[tray_header]=title
		# print('title -> ',title)
	except Exception as e:
		print('Error -> ',str(e))

# pprint.pprint(result)
		
# with open('voot_output.json','w') as f:
	# f.write(str(result))
	# f.write('\n')
	# f.write(' '.join([str(k) for k in url_list]))
	
# print('finished in -> ',datetime.now() - start)
driver.quit()