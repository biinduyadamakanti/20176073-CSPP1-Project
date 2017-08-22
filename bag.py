n1='to be or not to be' #input()
n2='doubt truth to be a liar'#input()
s = n1.split(" ")
print(s)
p = n2.split(" ")
print(p)
def freq(n):
	d={}
	for i in n:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d

d1=freq(s)
d2=freq(p)
print(d1)
print(d2)
sum=0
for i in d1.keys():
	for j in d2.keys():
		if i==j:
			e=d1[i]*d2[j]
			sum=sum+e
print(sum)
x=0
y=0
import math
for i in d1:
	x=x+((d1[i])**2)
for i in d2:
	y=y+((d2[i])**2)
print(x)
print(y)
q=(math.sqrt(x))*(math.sqrt(y))
print(q)
c=(sum/q)*100
print(c)