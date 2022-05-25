import firebase_admin
import pprint
from firebase_admin import credentials, firestore

product_file_path="productdata.csv"

with open(product_file_path,'r') as lines:
	for line in lines:
		print(line)


def firebase_read_write():
	path_to_file = "C:\\Suven\elearning\\urbanbasket-ae189-firebase-adminsdk-4rqyr-0e5cced26f.json"

	cred = credentials.Certificate(path_to_file)
	firebase_admin.initialize_app(cred)

	database = firestore.client()
	col_ref = database.collection('CATEGORIES')  # col_ref is CollectionReference

	category_id = []
	category_doc={}

	# print(dir(col_ref))
	# print('-'*50)

	# for col in col_ref.where('index', '>', 1).order_by('index').stream():
		# category_id.append(col.id)
		# category_doc[col.id] = col_ref.document(col.id).get().to_dict()

	data={"product_id_1":"UNGAFSAWAA010","product_title_1":"Aashirwad Aata 10 Kg","product_size_1":"101kg","product_price_1":"400"}
	documents = col_ref.where('index', '==', 3).stream()
	add_doc = col_ref.document("UNGAFS").collection("MORE").document("UNGAFSAW").set(data)


	# adding data to home collection with id being the type of the document
	home = col_ref.document('HOME').collection('TOP_DEALS').document()

	# index start 
	index=9
	# Strip ad banner 
	strip_add_banner_flds = {"background":"",
							"index":index,
							"strip_ad_banner":"",
							"view_type":1}
	index+=1
							
	# slider banner 
	slider_ad_banner_flds = {"banner_1":"",
							"banner_1_background":"",
							"index":index,
							"no_of_banners":"",
							"view_type":1}
	index+=1
	# product fields
	product_det_flds = {"index":index,
						"layout_background":"",
						"layout_title":"",
						"no_of_products":99,	
						"view_type":2,					
						"COD_1":True,
						"average_rating_1":"",
						"cutted_price_1":9999,
						"free_coupons_1":0,
						"in_stock_1":True,
						"product_ID_1":"",
						"product_full_title_1":"",
						"product_image_1":"",
						"product_price_1":"",
						"product_subtitle_1":"",
						"product_title_1":"",
						"total_ratings_1":99999
						}
						
	index+=1				