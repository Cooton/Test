#!/use/bin/env python3
#-*- conding:utf-8 -*-
def power(x,y):
	return x**y
def gcd(a,b):
	if a<b:
		print('a值小于b值，请让a>=b')
	while b:
		c=a%b
		a=b
		b=c
	return a

def bin(a):
	c=a//2
	i=[a%2]
	while c:
		a=c
		c=a//2
		i.append(a%2)
	return i[::-1]
print(bin(789))
print(gcd(100,10))


