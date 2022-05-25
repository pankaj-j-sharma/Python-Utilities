import os

def search_file(directory = None, file = None):
	assert os.path.isdir(directory)
	current_path, directories, files = os.walk(directory).next()
	if file in files:
		return os.path.join(directory, file)
	elif directories == '':
		return None
	else:
		for new_directory in directories:
			result = search_file(directory = os.path.join(directory, new_directory), file = file)
			if result:
				return result
		return None
		
path=input(" enter the path to search \n")
excluded=["lib","windows","incampusit","users","gcp","drivers","win"]
breakloop=False
filteronly=".ipynb"
searchtxt=input(" enter the search text \n")

for path,subdir,files in os.walk(path):
	
	for exclude in excluded:		
		if exclude in path.lower():
			breakloop=True
			break
	if breakloop:
		breakloop=False
		continue
	
	for name in subdir:
		subdir=os.path.join(path,name) # will print path of directories
	
	for name in files:
		if name.endswith(filteronly):
			filepath = os.path.join(path,name) # will print path of files		
			#print("Searching .. ",filepath)
			with open(filepath,'r',encoding='cp1252') as f:
				try:
					for line in f:
						if searchtxt in line:
							print("match found => ",filepath)
							print("matching line => ",line)
							break
				except Exception as e:
					print("Error reading .. ",filepath)