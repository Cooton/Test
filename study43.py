#！/user/bin/env python3
#-*-conding:utf:8 -*-
#第0题
class Panduan():
	def __init__(self,*a):
		i=0
		if not a:
			print('并没有传入参数')
		else:
			for i in a:
				i+=1
			print('传入了%d个数,分别是%s'%(i-1,a))
			
#第1题
class Word(str):
	"""docstring for Word"""
	def __init__(self,a):
		self.a=a
		self.a=(self.a.split())[0]
	def __le__(self,other):
		return len(self)<=len(other)
	def __ge__(self,other):
		return len(self)>=len(other)
	def __eq__(self,other):
		return len(self)==len(other)