#! python3
#pw.py - password locker

PASSWORDS = { 'email' : 'asfaf',
'blog' : 'asdfgh',
'luggage' : '12345'}

import sys,pyperclip

if len(sys.argv)<2:
	print('Usage: py pw.py [account] - copy account password')
	sys.exit()

account =sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password copied')
else:
	print('No such account exists')