a=open("f1.txt",'r')
b=open("f2.txt",'r')
p1=a.read()
p2=b.read()
p1=p1.lower()
p2=p2.lower()
def filter(p):
	s='abcdefghijklmnopqrstuvwxyz0123456789_'
	for i in range(len(p)):
		if p[i] not in s:
			p=p.replace(p[i]," ")
		return(p)

n1=filter(p1)
n2=filter(p2)
s = n1.split(" ")
p = n2.split(" ")
def freq(n):
	d={}
	for i in n:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d

def dot_sum(d1,d2):
	sum=0
	for i in d1.keys():
		for j in d2.keys():
			if i==j:
				e=d1[i]*d2[j]
				sum=sum+e
	return(sum)
def sqroot(d):
	x=0
	for i in d:
		x=x+((d[i])**2)
	return(x)

d1=freq(s)
d2=freq(p)
sum=dot_sum(d1,d2)
x=sqroot(d1)
y=sqroot(d2)
import math
q=(math.sqrt(x))*(math.sqrt(y))
c=(sum/q)*100
print(c)






	