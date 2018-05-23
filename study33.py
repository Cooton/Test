#!/user/bin/env python3
#-*-conding:utf-8-*-
# import random
# shuzi = random.randint(1,9)
# try:
# 	temp=input('你好，猜猜我喜欢的数字是什么？')
# 	guess=int(temp)
# except (EOFError,KeyboardInterrupt,ValueError):
# 	print('你输入滴格式错误，请重新输入')
# 	guess=shuzi
# while (guess!=shuzi):
# 	temp=input('哎呀，猜错了，请重新输入吧')
# 	guess = int(temp)
# 	while not temp.isdigit():
# 		temp=input("抱歉，输入错误的格式，请输入数字")
# 	if guess == shuzi:
# 		print('流弊,猜中了.')
# 	else:
# 		if guess >shuzi:
# 			print('老哥，大了。')
# 		else:
# 			print('老哥，小了。')
# print('游戏结束啦~')
def int_input(prompt=''):
	while True:
		try:
			int(input(prompt))
			break
		except (TypeError,ValueError):
			print('输入格式有误，请重新输入')
int_input('请输入一个整数')