a=open('f1.txt','r')
b=open('f2.txt','r')
n1=a.read()
n2=b.read()
n1=n1.lower()

for i in range(len(n1)):
	if n1[i] not in 'abcdefghijklmnopqrstuvwxyz0123456789_':
		n1=n1.replace(n1[i]," ")
print(n1)

		