def filter(p):
	s='abcdefghijklmnopqrstuvwxyz0123456789_'
	for i in range(len(p)):
		if p[i] not in s:
			p=p.replace(p[i]," ")
		return(p)
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
def cos(d1,d2):
	sum=dot_sum(d1,d2)
	x=sqroot(d1)
	y=sqroot(d2)
	import math
	q=(math.sqrt(x))*(math.sqrt(y))
	c=(sum/q)*100
	return(c)

def filelist():
	import glob,os
	l=[]
	os.chdir("filesp")
	for f in glob.glob("*.txt"):
		l.append(f)
	return l

l=filelist()
q=["        "]
q.extend(l)
print(q)
o=[]	
for i in l:
	o.append(i)
	t=[]
	for j in l:
		if i!=j:
			a=open(i,'r')
			b=open(j,'r')
			p1,p2=a.read(),b.read()
			p1,p2=p1.lower(),p2.lower()
			n1,n2=filter(p1),filter(p2)
			s,p = n1.split(" "),n2.split(" ")
			d1,d2=freq(s),freq(p)
			e=cos(d1,d2)
			t.append(e)
		else:
			e="  0"
			t.append(e)
	o.append(t)


print(o)



#print("for %c and %c match is %s",i,j,cos(d1,d2))






	
