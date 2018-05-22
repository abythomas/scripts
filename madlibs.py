import re,pyperclip

a=raw_input()
n=raw_input()
v=raw_input()

text=str(pyperclip.paste())

adj=re.compile(r'ADJECTIVE')
noun=re.compile(r'NOUN')
verb=re.compile(r'VERB')

text=adj.sub(a,text)
text=noun.sub(n,text)
text=verb.sub(v,text)

fy=open('test.txt','w')
fy.write(text)
fy.close()