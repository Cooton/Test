#!/usr/bin/env python3
# -*- coding: utf-8 -*-
temp=input('请输入一个年份，我来判断是否为闰年:')
time=int(temp)
while not temp.isdigit():
	temp=input("抱歉，输入错误的格式，请输入数字")
if (time/100==int(time/400)) and (time/400==int(time/400)):
	print(temp+'为闰年')
else:
	if(time/4==int(time/4)):
		print(temp+'为闰年')
	else:
		print('非闰年')
