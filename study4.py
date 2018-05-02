#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
shuzi = random.randint(1,9)
print('你好，猜猜我喜欢的数字是什么？')
guess = 0
i=3
while (guess!=shuzi) and (i>0):
	temp=input()
	while not temp.isdigit():
		temp=input("抱歉，输入错误的格式，请输入数字")
	guess = int(temp)
	i=i-1	
	if guess == shuzi:
		print('流弊,猜中了.')
	else:
		if guess >shuzi:
			print('老哥，大了')
		else:
			print('老哥，小了')
		if i>0:
			print('请再输入一次吧')
		else:
			print('猜错三次，滚粗,正确答案是:',shuzi)
print('游戏结束啦~')