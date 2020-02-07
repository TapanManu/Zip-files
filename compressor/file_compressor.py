from zipfile import ZipFile
import os
#python code to zip all files in a given directory
def get_all_file_paths(directory):
	file_paths=[os.path.join(root,filename) for root,directories,files in os.walk(directory) for filename in files]
	#get the file paths of all files in the given directory
	return file_paths

temp='/home/tapan/'
templ=temp.split('/')
templ=templ[:3]

#get the directory
directory=input("get the directory whose contents need to be zipped:")
templ.append(directory)
directory='/'.join(templ)
print('directory to be zipped:',directory)
filepath=get_all_file_paths(directory)
print('following files will be zipped')

for file_name in filepath:
	print (file_name)	

#specify the target zip file
zip=input('specify the target file:')		
zip=zip.split(' ')
print(zip)
zip.append('.zip')
zip=''.join(zip)

with ZipFile(zip,'w') as zip:
	for files in filepath:
		zip.write(files)

print('all files zipped successfully')			
