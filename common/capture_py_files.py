import os 
import sys

path="C:/"
print(sys.argv[0])
all_py_files = []

for path,subdir,files in os.walk(path):
	for name in subdir:
		subdir=os.path.join(path,name) # will print path of directories
		#print('subdir -> ',subdir)
		
	for name in files:
		if name.endswith('.py'):
			filepath = os.path.join(path,name) # will print path of files		
			print('file -> ',filepath)
			all_py_files.append(filepath)

with open('all_py_file_paths.txt') as f:
	for fpath in all_py_files:
		f.write(fpath)