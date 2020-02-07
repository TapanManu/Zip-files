from zipfile import ZipFile

file_name=input('specify the input zip file to be extracted:')
if '.zip' not in file_name:
	root='/home/tapan'
	root=root.split('/')
	file_name=file_name.split(' ')
	file_name.append('zip')
	file_name='.'.join(file_name).split(' ')
	root.extend(file_name)
	file_name='/'.join(root)
	print(file_name)
	
print('enter the directory where the files should be extracted')
print(' or press enter to extract at current directory')
directory=input()	

with ZipFile(file_name,'r') as zip:
	#printing all the components of zip file
	zip.printdir()
	# extracting all the files 
	print('Extracting all the files now...') 
	zip.extractall(directory)
	print('Done!')  
