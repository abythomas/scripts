#! python3
# Compress a file by giving location as an argument

import zipfile,os,sys

if (sys.argv<2):
	print("FILE TO BE ZIPPED NOT PASSED AS INPUT")
else:
	loc=sys.argv[1]
	loc=os.path.abspath(loc)
	print(loc)
	num=1
	while True:
		zipName=os.path.basename(loc)+'_'+str(num)+'.zip'
		if not os.path.exists(zipName):
			break
		num=num+1
	print('Creating %s...'%(zipName))
	backup=zipfile.ZipFile(zipName,'w')
	
	for foldername,subfolders,filenames in os.walk(loc):
		print('Adding files in %s...'%(foldername))
		backup.write(foldername)
		for filename in filenames:
			backup.write(os.path.join(foldername,filename))
	backup.close()
	print('Done')




































			
