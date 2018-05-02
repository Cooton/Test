#!/user/bin/env python3
#-*- conding:utf-8 -*-

print('|---欢迎进入通讯率程序---|')
print('|---1：查询联系人资料 ---|')
print('|---2：插入新的联系人 ---|')
print('|---3：删除已有联系人 ---|')
print('|---4：推出通讯录模式 ---|')

zl={}
while 1:
	i=int(input('请输入相关得指令代码：'))
	if i==1:
		name=input('请输入联系人姓名:')
		if name in zl:
			print('联系人电话为:',zl[name])
		else:
			print('您输入的姓名不在通讯录中')
	if i==2:
		name=input('请输入联系人姓名:')
		if name in zl:
			print('您输入得姓名已存在',zl,)
			if input('是否修改用户资料（YES/NO)')=='YES':
				zl[name]=input('请输入联系人电话:')
			else:
				break
		else :
			zl[name]=input('请输入联系人电话:')
	if i==3:
		name=input('请输入你要删除联系人姓名:')
		if name in zl:
			del(zl[name])
			print('删除成功')
		else:
			print('您输入的姓名不在通讯录中')
	if i==4:
		print('|---感谢使用通讯录程序---|')
		break