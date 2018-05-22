#! python3
# Search copied text for email address

import re,pyperclip

ereg=re.compile(r'''(
 [a-zA-Z0-9._%+_]+
 @
 [a-zA-Z0-9.-]+
 (\.[a-zA-Z]{2,6})
 )''',re.VERBOSE)

text=str(pyperclip.paste())

me=[]

for groups in ereg.findall(text):
	me.append(groups[0])

pyperclip.copy('\n'.join(me))
