#!/user/bin/env python3
#-*-conding:utf-8-*-
#第0题
class Nstr(str):
	def __sub__(self,other):
		return self.replace(other,'')
#第一题
class Nstr(str):
	def __new__(nstr,temp):
		a=temp
		return str.__new__(nstr,a)
	def __lshift__(self,other):
		return (a[other:]+a[:other])
	def __rshift__(self,other):
		return (a[:other]+a[other:])
#第二题
class Nstr(int):
	def __new__(nstr,value=0):
		sum=0
		for x in value:
			sum=sum+ord(x)
			value=sum
		return int.__new__(nstr,value)
	def __rsub__(self,other):
		return int.__sub__(self,other)
	def __radd__(self,other):
		return int.__add__(self,other)
	def __rtruediv__(self,other):
		return int.__truediv__(self,other)
	def __rmul__(self,other):
		return int.__mul__(self,other)
	def __rfloordiv__(self,other):
		return int.__rfloordiv__(self,other)

