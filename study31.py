#!/user/bin/env python3
#-*-conding:utf-8-*-
import pickle

def target(file_name):
	f=open(file_name)
	
	count=1
	boy=[]
	girl=[]
	for each_line in f:
		if each_line[:6]!='======':
			(role,line_sopken)=each_line.split('：',1)
			if role=='骚男':
				boy.append(line_sopken)
			if  role=='骚女':
				girl.append(line_sopken)
		else:
			save(boy,girl,count)
			boy=[]
			girl=[]
			count+=1
	save(boy,girl,count)
	f.close()

def save(boy,girl,count):
	file_name_boy ='boy_'+str(count)+'.txt'
	file_name_girl ='girl_'+str(count)+'.txt'

	file_name_boyx ='boyx'+str(count)+'.pkl'
	file_name_girlx ='girlx'+str(count)+'.pkl'

	pickle_file_boy=open(file_name_boyx,'wb')
	pickle_file_girl=open(file_name_girlx,'wb')

	boy_file=open(file_name_boy,'w')
	girl_file=open(file_name_girl,'w')

	boy_file.writelines(boy)
	girl_file.writelines(girl)

	boy_file.close()
	girl_file.close()
	
	boy_file_r=open(file_name_boy,'r')
	girl_file_r=open(file_name_girl,'r')

	b=boy_file_r.read()
	g=girl_file_r.read()

	pickle.dump(b,pickle_file_boy)
	pickle.dump(g,pickle_file_girl)
	
	count+=1
	pickle_file_boy.close()
	pickle_file_girl.close()

	boy=[]
	girl=[]

target('E:\\record.txt')
