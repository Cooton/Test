#!/user/bin/env python3
#-*- conding:utf-8 -*-
def dg(x):
	sum=1
	for i in range(1,x+1):
		sum=sum*i
	return sum
def digui(x,y):
	if y==1:
		return x
	else:
		return x*digui(x,y-1)
print(digui(3,4))

def gcd(x,y):
	while x%y:
		return gcd(y,x%y)
	if x%y==0:
		print('%d为最大公约数'%y)
gcd(27,18)