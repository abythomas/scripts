#! python3

import sys,requests

if sys.argv<2:
	print('No link provided')
else:
	res=requests.get(str(sys.argv[1]))
	try:
		res.raise_for_status()
		textfile=open('textfile.txt','wb')
		for chunk in res.iter_content(100000):
			textfile.write(chunk)
		textfile.close()
	except Exception as exc:
		print('There was a problem:%s'%(exc))

