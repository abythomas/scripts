#!python3
#Open top five google searches

import sys,requests,bs4,webbrowser

print('Searching...')
url='http://google.com/search?q='+'+'.join(sys.argv[1:])
res=requests.get(url)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)


linkElements=soup.select('.r a')

num=min(len(linkElements),5)
for i in range(num):
	webbrowser.open('http://google.com'+linkElements[i].get('href'))
	
