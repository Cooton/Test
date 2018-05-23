#!/user/bin/env python3
#-*-conding:utf-8-*-
class FileObject():
	def __init__(self,name):
		self.name=name
		with open(self.name) as n:
			pass
	def __del__(self):
		pass
#第一题
class C2F(float):
	"""docstring for C2F"""
	def __new__(c2f,value):
		value=(value*1.8)+32
		return float.__new__(c2f,value)
#第二题
class Nint(int):
	def __new__(nint,value):
		sum=0
		if not str(value).isdigit():
			for x in value:
				sum=sum+ord(x)
			return int.__new__(nint,sum)
		else:
			return value

#参考
class Nint(int):
	def __new__(nint,value=0):
		sum=0
		if isinstance(value,str):
			for x in value:
				sum=sum+ord(x)
				value=sum
		return int.__new__(nint,value)
