import pprint
from flipkart_scrapper import Flipkart

if __name__=='__main__':
	useroptions = 'Please select one of the providers below :\
	\n1.Flipkart \
	\n2.Amazon \
	\n3.TataCliq \
	\nEnter 0 to exit \n'
	
	query = str(input('Please enter the query to search for \n'))
	scrapper = None
	while True:
		try:
			option = int(input(useroptions))
			if option not in [0,1,2]:
				print('\n*******Enter a valid selection******\n')
			elif option == 0:
				break
			elif option == 1:
				scrapper = Flipkart()
				break
			elif option == 2:
				scrapper = Amazon()
				break
			elif option == 3:
				scrapper = TataCliq()
				break
		except KeyboardInterrupt as e:
			break
		except ValueError as e:
			print('\n******Please select a valid option*******\n')

	if isinstance(scrapper,Flipkart):
		scrapper.get_search_result(query)	
		soup = scrapper.get_parsed_html()
		prod_url= scrapper.get_product_links(soup)
		if prod_url:
			link,link_not_found = scrapper.get_product_review_links(prod_url)
			if len(link_not_found)>0:
				scrapper.get_product_page_reviews(link_not_found)
				if len(link)>0:
					scrapper.get_reviews_data(link)
			else:
				scrapper.get_reviews_data(link)
			scrapper.get_all_saved_data()
			scrapper.save_reviews()			
		else:
			print('No Product URL found ')