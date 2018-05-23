#!/user/bin/env python3
#-*- conding:utf-8 -*-
from datetime import date
import time
import pickle
import os
class  MyDecriptor(object):
	def __get__(self,instance,owner):
		print('getting..',self,instance,owner)
	def __set__(self,instance,value):
		print('setting..',self,instance,value)
	def __delete__(self,instance):
		print('deleting..',self,instance)
class Test(object):
	x=MyDecriptor()  
class  MyProperty(object):
	def __init__(self,fget=None,fset=None,fdel=None):
		self.fget=fget
		self.fset=fset
		self.fdel=fdel

	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		self.fset(instance,value)
	def __del__(self,instance):
		self.fdel(instance)
class C(object):
	def __init__(self):
		self._x=None
	def getX(self):
		return self._x
	def setX(self,value):
		self._x=value
	def delX(self):
		del self._x
	x=MyProperty(getX,setX,delX)
class Celsius:
	def __init__(self,value=26.0):
		self.value=float(value)
	def __get__(self,instance,owner):
		return self.value
	def __set__(self,instance,value):
		self.value=float(value)
class Fahrenheit:
	def __get__(self,instance,owner):
		return instance.cel *1.8+32
	def __set__(self,instance,value):
		instance.cel=(float(value)-32)/1.8
class  Temperature:
	cel=Celsius()
	fah=Fahrenheit()
#第0题
class  MyDes:
	"""docstring for  MyDes"""
	def __init__(self,value,name):
		self.value=value
		self.name=name
	def __get__(self,instance,owner):
		print('正在获取变量:%s'%self.name)
		return self.value
	def __set__(self,instance,value):
		print('正在修改变量:%s'%self.name)
		self.value=value
	def __delete__(self,instance):
		print('正在删除变量:%s'%self.name)
		print('该变量无法删除')
class Test:
	x=MyDes(10,'x')
#第1题
class MyDes:
	def __init__(self,value,name):
		self.value=value
		self.name=name
		self.temp=[]
	def __get__(self,instance,owner):
		self.ttime=time.ctime()
		with open('E:\\编程\\GitHub\\Test\\record.txt','a') as self.f:
			self.f.write(self.name+'变量于北京时间'+str(self.ttime)+'被读取:'+self.name+'='+str(self.value))
		return self.value
	def __set__(self,instance,value):
		
		self.time=date.today()
		with open('E:\\编程\\GitHub\\Test\\record.txt','a') as self.f:
			self.f.write(self.name+'变量于北京时间'+str(self.ttime)+'被修改:'+self.name+'='+str(self.value))
		self.value=value
class Test:
	x=MyDes(10,'x')
	y=MyDes(8,'y')
#第2题
class MyDes:
	temp=[]
	def __init__(self,name=None):
		self.name=name
		self.filename='E:/编程/GitHub/Test/'+self.name+'.pkl'
	def __get__(self,instance,owner):
		if self.name not in MyDes.temp:
			raise AttributeError('%ss属性还没有被赋值'%self.name)
		with open(self.filename,'rb') as f:
			value=pickle.load(f)
		return value
	def __set__(self,instance,value):
		f=open(self.filename,'wb')
		pickle.dump=(value,f)
		f.close()
		MyDes.temp.append(self.name)
	def __delete__(self,instance):
		os.remove(self.filename)
		MyDes.temp.remove(self.name)