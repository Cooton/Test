#!/user/bin/env python3
#-*- conding:utf-8 -*-
#第0题
class C():
	def __getattr__(self,name):
		print('该属性不存在')
#第1题
class Demo(object):
	def __init__(self):
		self.x='FishC'
	def __getattr__(self,name):
		self.name='FishC'
		return self.name
#第2题
class Counter():
	def __init__(self):
		super().__setattr__('counter',0)
	def __setattr__(self,name,value):
		super().__setattr__('counter',self.counter+1)
		super().__setattr__(name,value)
	def  __delattr__(self,name):
		super().__setattr__('counter',self.counter1)
		super().__delattr__(name)
