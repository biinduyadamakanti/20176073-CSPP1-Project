#a=open('f1.txt','r')
#b=open('f2.txt','r')
#p1=a.read()
#p2=b.read()
#p1=p1.lower()
#p2=p2.lower()
p1='to a@ t be'
s=''
q='abcdefghijklmnopqrstuvwxyz0123456789_'
for i in p1:
	if i in q:
		s=s+i
	elif i==' ':
		s=s+" "
	elif i=="@ ":
		s=s+""
	else:
		s=s+" "
s=s.split(" ")
l=[]
for i in s:
	if i!='':
		print(i)
		l.append(i)

print(l)
#print(p)	
#print(p1)