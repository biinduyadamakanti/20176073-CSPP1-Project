a=open('f1.txt','r')
b=open('f2.txt','r')
p1=a.readline()
print(p1)
p2=b.read()
p1=p1.lower()
p2=p2.lower()
s='abcdefghijklmnopqrstuvwxyz0123456789_'
for i in p1:
	for c in str(i):

		if c not in s:
			p1=p1.replace(c," ")
		#print(p)	
		#print(p1)