#!/user/bin/env python3
#-*- conding:utf-8 -*-
#第0题
it=iter(range(5))
while True:
	try:
		a=next(it)
	except StopIteration:
		break
	print(a)
#第一题
class LeapYear():
	def __init__(self,n=2018):
		self.n=n
	def __iter__(self):
		return self
	def isLeapYear(self,year):
		if (year%4==0 and year%100!=0)or year%400==0:
			return True
		else:
			return 0
	def __next__(self):
			while not self.isLeapYear(self.n):
					self.n-=1
			temp=self.n
			self.n-=1
			return temp
class  MyRev:
	def __init__(self,value):
		self.i=len(value)
		self.value=value
	def __iter__(self):
		return self
	def __next__(self):
			if self.i==0:
				raise StopIteration
			self.i=self.i-1
			return self.value[self.i]


