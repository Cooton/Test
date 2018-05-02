#!/user/bin/env python3
#-*-conding:utf-8-*-
# name='E:/'+input('请输入文件名:')
# a=open(name,'w')
# temp=input('请输入内容（单独输入\':w\'保存退出）:')
# a.write(temp)
# while 1:
# 	temp=input()
# 	a.write(temp)
# 	a.write('\n')
# 	if temp==':w':
# 		break
# a.close()

name1='E:/'+input('请输入要比较的文件名:')
name2='E:/'+input('请输入要比较的另一个文件名:')
a=open(name1)
b=open(name2)
a1=a.readline()
b1=b.readline()
count=0
x=0
while a1:
	a1=a.readline()
	b1=b1=b.readline()
	if a1!=b1:
		count+=1
for line in a:
	x+=1

print('两个文件共有%d处不同：'%count)
a.close()
b.close()

# name=input('请输入要打开的文件:')

# a=open(name)
# a1=a.readlines()
# print(a1[int(input('请输入要显示的行数:'))])
# a.close()

# name=input('请输入要打开的文件:')
# a=input('请输入要替换的字符:')
# b=input('请输入你想要的字符:')
# count=0
# content=[]
# f_read=open(name)
# z1=f_read.readlines()
# w=open(name,'w')
# for eachline in f_read:
# 	if a in eachline:
# 		count=eachline.count(a)
# 		eachline=eachline.replace(a,b)
# 	content.append(eachline)
# panduan=input('文件%s中有个%s个【%s】你确定要把所有的【%s】替换为【%s】嘛'%(name,count,a,a,b))
# if panduan=='YES':
# 	for i in z1:
# 		w.write(i.replace(a,b))
# else:
# 	w.close()
# z1.close()
