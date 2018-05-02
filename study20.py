#!/user/bin/env python3
#-*- conding:utf-7 -*-
def huiwenlian():
	a=input('请输入你要打的话：')
	if a==a[::-1]:
		print('为回文联')
	else:
		print('非回文连')
#huiwenlian()
def tongji(*s):
	length=len(s)
	for i in range(length):
		count1=0
		count2=0
		count3=0
		count4=0
		for etch in s[i]:
			if etch.isdigit():
				count1+=1
			elif etch.isalpha():
				count2+=1
			elif etch.isspace():
				count3+=1
			else:
				count4+=1
		print('第%d个字符串共有:英文字母%d个,数字%d个，空格%d个，其他字符%d个'% (i+1,count2,count1,count3,count4))
tongji('I love fish.com','i love you  you love me ')

