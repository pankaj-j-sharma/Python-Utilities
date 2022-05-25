import pyfacebook
import facebook
import requests
import pprint
import json

raw_url = 'https://graph.facebook.com/v5.0/'
token = 'EAAjtlR3D9EgBAPKV7aXUBVgZBDWwtziwoFZCMlgu1yZBIX3cMA82IOpV9yDP5HVRTH697gY7nPx44QaGHViDlnTjvZB2Pq0lJlUm7VljykK3OM18tNH13zP2vZCiyFvtw6DChAbOCt1c3SAYKdUzuoDgxTEWyi1JN3LHZCKjhgFvdNvEwOpWH6FArF8HzQmDcZD'

def get_field_fb_sdk():
	graph = facebook.GraphAPI(token)
	fields=['email','gender','posts.limit(20)','feed.limit(10)']
	profile = graph.get_object('me',fields=fields)
	print(json.dumps(profile,indent=4))

def get_field_data(urlquery):
	
	url = raw_url+urlquery+'?access_token='+token
	response = requests.get(url)
	return response.text

if __name__=='__main__':
	get_field_fb_sdk()
	# print('-'*100,'\n')
	# pprint.pprint(get_field_data('me'),indent=4)
	# print('-'*100,'\n')
	# pprint.pprint(get_field_data('me/friends'),indent=4)
	# print('-'*100,'\n')
	# pprint.pprint(get_field_data('me?fields=about,hometown,quotes,security_settings,albums'),indent=4)
	# print('-'*100,'\n')
	