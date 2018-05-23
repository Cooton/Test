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
#第二题
# gen=input('请输入你要找的初始目录：')
# target=input('请输入你要找的文件：')
# os.chdir(gen)
# def sarch(gen,target):
# 	for each_file in os.listdir('.'):
# 		if each_file==target:
# 			print(os.getcwd()+'//'+each_file)
# 		if os.path.isdir(each_file):
# 			sarch(gen,target)
# 			os.chdir(os.pardir)
# sarch(gen,target)

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

# 第四题
def print_pos(key_dict):
	keys=key_dict.keys()
	keys=sorted(keys)
	for each_key in keys:
		print('关键字出现再第%s行，第%s个位置。'%(each_key,str(key_dict[each_key])))
def pos_in_line(line,key):
	pos=[]
	begin=line.find(key)
	while begin!=-1:
		pos.append(begin+1)
		begin=line.find(key,begin+1)
	return pos
def sarch_in_file(file_name,key):
	f=open(file_name)
	count=0
	key_dict=dict()
	for each_line in f:
		count+=1
		if key in each_line:
			pos=pos_in_line(each_line,key)
			key_dict[count]=pos
	f.close()
	return key_dict
def find(keyn,panduan):
	txt_files=[]
	for root,dirs,files in os.walk('.'):
		for name in files:
			a=(name)
			b=os.path.splitext(a)
			if b[1]=='.txt':
				each_line=os.path.join(root,a)
				txt_files.append(name)
				for each_txt_file in txt_files:
					key_dict=sarch_in_file(each_txt_file,key)
					if key_dict:
						print('在文件%s中找到关键字%s'%(each_txt_file,key))
						if panduan in['YES','Yes','yes']:
							print_pos(key_dict)
os.chdir('E:\\New\\')
key=input('输入关键字：')
panduan=input('找到关键字的具体位置，是否打出？[YES,NO]')
find(key,panduan)

