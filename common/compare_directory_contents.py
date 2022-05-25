# python program to compare two directory contents and write the output to a file 
import os 

print('We will compare the contents of the two directories and store the output to result.txt')
source = input('Enter the path of source folder \n')
target = input('Enter the path of target folder \n')

for root,dirs,files in os.walk(source):
	for name in files:
		#print(os.path.join(root, name))
		try:
			temp1=[]
			temp2=[]
			with open(os.path.join(root, name),'rb') as f:
				temp1=set(f.readlines())				
			with open(os.path.join(root.replace(source,target), name),'rb') as f:
				temp2=set(f.readlines())				
			if list(temp2-temp1):
				print(name)
			for line in list(temp2-temp1):
				print(line)
				print('-'*50)
		except FileNotFoundError:
			print('File not present -> ',os.path.join(root, name))			
