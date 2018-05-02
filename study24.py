#!/user/bin/env python3
#-*- conding:utf-8 -*-
def rubb(x):
	if x==1:
		return 1
	if x==2:
		return 1
	else:
		return rubb(x-1)+rubb(x-2)
def bin1(x):
	c=x//2
	a=[x%2]
	while c:
		x=c
		c=x//2
		a.append(x%2)
	return(a[::-1])
def bin2(x):
	a=[]
	if x:
		a= bin2(x//2)
		return a+[(x%2)]
	else:
		return a[::-1]
#print(bin2(4))
# def get_digits1(n):
# 	a=[]
# 	temp=n
# 	while temp:
# 		a=a+[(temp%10)]
# 		temp//=10
# 	if  ((temp//10)-10)<0:
# 		print(a[::-1])
# get_digits1(456)
a=[]
def get_digits2(n):
	if n>0:
		a.insert(0,n%10)
		get_digits2(n//10)
	else:
		print(a)
get_digits2(456)
# def age(n):
# 	if n==1:
# 		return 10
# 	else :
# 		return age(n-1)+2
# print(age(2))