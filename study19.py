#!/user/bin/env python3
#-*- conding:utf-8 -*-
def he(a,b,c,d=3):
	return (a+b+c)*d
#print(he(2,3,4,5))

def sxh():
	for i in range(100,1000):
		sum=0
		temp=i
		while temp:
			sum=sum+((temp%10)**3)
			temp//=10
		if  sum==i:
			print(i)
sxh()
# def findstr():
# 	a=input('请输入目标字符串')
# 	b=input('请输入子字符串（2个）')
# 	print('子字符串在目标字符串中共出现');return a.count(b)
	
# findstr()