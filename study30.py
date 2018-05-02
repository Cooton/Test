#!/user/bin/env python3
#-*-conding:utf-8-*-
import os
import os.path
#第0题
# os.chdir('E:\\')
# a=os.listdir(path='.')
# count_txt=0
# count_png=0
# count_py=0
# count_文件夹=0
# for i in a:
# 	b=os.path.splitext(i)
# 	if b[1]=='.txt':
# 		count_txt+=1
# 	if b[1]=='.png':
# 		count_png+=1
# 	if b[1]=='.py':
# 		count_py+=1
# 	if b[1]=='':
# 		count_文件夹+=1
# print('该文件夹下共有类型为【txt】的文件：%d\n该文件夹下共有类型为【png】的文件：%d\n该文件夹下共有类型为【py】的文件：%d\n该文件夹下共有类型为【文件夹】的文件：%d\n'%(count_txt,count_png,count_py,count_文件夹))

#第一题
# os.chdir('E:\\')
# a=os.listdir(path='.')
# for i in a:
# 	b=os.path.getsize(i)
# 	print('%s【%s】'%(i,b))

#第三题
# os.chdir('E:\\')
# mulv=input('请输入待查找的目录：')
# cc=open('vdieo.txt','w')
# for root,dirs,files in os.walk(mulv):
# 	for name in files:
# 		a=(name)
# 		b=os.path.splitext(a)
# 		if b[1]=='.mp4':
# 			print(os.path.join(root,name))
# 			cc.write(os.path.join(root,name))
def find(key):
	count=0
	for root,dirs,files in os.walk('.'):
		for name in files:
			a=(name)
			b=os.path.splitext(a)
			if b[1]=='.txt':
				print(os.path.join(root,name))
				cc=open(a)
				a1=cc.readline()
				while a1:
					a1=cc.readline()
					if key in a1:
						count+=1
						wz=cc.tell()
						print('在文件%s中找到关键字%s\n在第%d行第%d位置'%(os.path.join(root,name),key,count,wz))
					

#
				cc.close()
os.chdir('E:\\New\\')
key=input('输入关键字：')
# panduan=input('是否打印位置：（YES\NO）')
# if panduan=='YES':
find(key)
# else:
# 	print('退出程序')
