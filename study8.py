#!/usr/bin/env python3
# -*- coding: utf-8 -*-
chengji=int(input('请输入1-100的数字：'))
if 0<chengji<101:
	if chengji>90:
		print('A')
	elif chengji>80:
		print('B')
	elif chengji>60:
		print('C')
	elif chengji<60:
		print('D')
else:
	print('输入错误')