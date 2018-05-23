#!/user/bin/env python3
#-*-conding:utf-8-*-
import easygui as g
import os
import os.path
#第0题
import random
shuzi = random.randint(1,9)
temp=g.integerbox('你好，猜猜我喜欢的数字是什么？(0-9)','数字小游戏','',0,9)
guess=int(temp)
while guess!=shuzi:
	temp=g.integerbox('哎呀，猜错了，请重新输入吧')
	guess = int(temp)
	if guess == shuzi:
		g.msgbox('流弊,猜中了.','数字小游戏')
	else:
		if guess >shuzi:
			g.msgbox('老哥，大了。','数字小游戏')
		else:
			g.msgbox('老哥，小了。','数字小游戏')
g.msgbox('游戏结束啦~','数字小游戏')

#第一题
# msg='[*真实姓名]为必填项\n[*手机号码]为必填项\n[*E-mail]为必填项'
# fields=('*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail')
# filevalues  =[]
# filevalues =g.multenterbox(msg,'用户信息填写',fields)
# while True:
#     if filevalues==None:
#         break
#     errmsg=''
#     for i in range(len(filevalues)):
#         option=fields[i].strip()
#         if (filevalues[i].strip()=='')and(option[0]=='*'):
#             errmsg=('带*号的必填%s'%fields[i])
#             g.msgbox(errmsg)
#     if errmsg=='':
#         break
#     filevalues=g.multenterbox(msg,'用户信息填写',fields,filevalues)
# print('你打印的信息为'+str(filevalues))

#第二题
# files=['E:\\record.txt','E:\\文件.txt']
# f=g.choicebox('选择你要打开的文件','文件浏览',files)
# text=open(f)
# neirong=text.read()
# g.textbox('文件内容为：','文件浏览器',neirong)
# text.close()
#第三题
# choice=('覆盖保存','放弃修改','另存为')
# files=g.fileopenbox()
# #f=g.choicebox('选择你要打开的文件','文件浏览',files)
# text=open(files)
# neirong=text.read()
# a=g.textbox('文件内容为：','文件浏览器',neirong)
# if a.strip()!=neirong.strip():
#     get_choice=g.choicebox('检测到文件有修改内容','警告',choice)
#     if get_choice=='覆盖保存':
#         text.close()
#         text_r=open(f,'w')
#         text_r.write(a)
#         g.msgbox('文件已保存。')
#     if get_choice=='放弃修改':
#         g.msgbox('用户放弃修改')
#     if get_choice=='另存为':
#         lcw=g.enterbox('请输入要保存的位置以及文件名(如E:\\text1.txt)')
#         lcw_r=open(lcw,'w')
#         lcw_r.write(a)
# text.close()

# #第四题
# wjj=g.diropenbox('请选择你的代码库','浏览文件')
# print(wjj)
# sum=0
# for (root,dirs,file) in os.walk(wjj):
#     for name in file:
#         b = os.path.splitext(name)
#         f=open(wjj+'\\'+name)
#         f_r=f.readline()
#         line=0
#         for i in f_r:
#         	line+=1
#         f_w=open('E://text1.txt','a')
#         f_w.write('%s文件的代码行为'%name+str(line)+'\n')
#         sum+=line
#         f.close()
#         f_w.close()
#         t_o=open('E://text1.txt')
#         t_r=t_o.read()
# t_o.close()
# baifenbi=sum/100000
# cha=100000-sum
# msg=('您目前编写了%s代码,完成度%s\n离十万行还差%s,请继续努力'%(sum,baifenbi,cha))
# g.textbox(msg, '统计文件', t_r)
# if g.ccbox("你想要干嘛？","选择","我没想干嘛"):
#         g.msgbox('滚蛋')         # user chose to continue
# else:
#         exit()
#
# a=['爱我','不爱','拒绝回答']
# g.choicebox('老猪你爱不爱我？','选项',choices=a)
#
# g.buttonbox('你爱我嘛','选项',('拉拉，我和稀泥','爱爱爱','我叼你之际'),image='I want you.jpg')
#
# g.enterbox('你爱我嘛')
#
# g.integerbox('请输入1-99之间的数字：')
#
# a=g.passwordbox('请输入密码：')
# print(a)
#
# f=open('record.txt')
# f_read=f.read()
#
# g.textbox('record.txt的内容为','内容显示',str(f_read))