#!/user/bin/env python3
#-*-conding:utf-8-*-
def qianyan():
	print('|---新建用户(n)---|')
	print('|---登陆用户(e)---|')
	print('|---推出程序(q)---|')
qianyan()
zl={}
def New():
	a='请输入用户名：'
	while True:	
		name=input(a)
		if name in zl:
			a='此用户名已被使用，请重新输入'
			continue
		else :
			break
	password=input('请输入密码：')
	zl[name]=password
	print('注册成功,That\'s good')
def Enter():
	temp1=input('请输入用户名：')
	if temp1 in zl:
		temp2=input('请输入登陆密码：')
		if temp2==zl[temp1]:
			print('登陆成功~That\'s good')
		else:
			print('密码错误')
	else:
		print('输入的用户名不在~请重新输入')
		Enter()

while 1:
	i=input('|---请输入指令:---|')
	if i=='n':
		New()
	if i=='e':
		Enter()
	if i=='q':
		pass

