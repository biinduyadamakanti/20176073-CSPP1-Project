a=open('f1.txt','r')
b=open('f2.txt','r')
n1=a.read()
n2=b.read()
for i in n1:
	if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		i=i.lower()
		print(i)
	else:
		i=chr(32)
print(n1)