#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.	# 密码安全性检查代码
# 2.	#
# 3.	# 低级密码要求：
# 4.	#   1. 密码由单纯的数字或字母组成
# 5.	#   2. 密码长度小于等于8位
# 6.	#
# 7.	# 中级密码要求：
# 8.	#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# 9.	#   2. 密码长度不能低于8位
# 10.	#
# 11.	# 高级密码要求：
# 12.	#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
# 13.	#   2. 密码只能由字母开头
# 14.	#   3. 密码长度不能低于16位

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

mima=input('请输入你要设置的密码: ')
len1=len(mima)
while (len1==0) or (mima.isspace()):
	print('你输入的密码包含空格,或者空，请重新输入:')
	mima=input('请输入你要设置的密码: ')
if len1<=8:
	flag_len1=1
elif 8<len1<16:
	flag_len1=2
else:
	flag_len1=3
flag_con=0
for x in mima:
	if x in nums:
		flag_con+=1
		break
for x in mima:
	if x in chars:
		flag_con+=1
		break
for x in mima:
	if x in symbols:
		flag_con+=1
		break
while 1:
	if (flag_len1==1) or(flag_con==1):
		print('你的密码强度为低！')
	elif (flag_len1==2) or (flag_con==2):
		print('你的密码强度为中！GOOD')
	else:
		print('你的密码强度为高！THAT is so good,Ass we can!')
		break
	break

