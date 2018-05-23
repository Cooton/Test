#!/user/bin/env python3
#-*- conding:utf-8 -*-
#第0题
from math import sqrt
def  MyRev(value):
	i=len(value)
	while True:
		i=i-1
		yield value[i]
		if i==0:
			raise StopIteration
def MyRev(value):
	for i in range(len(value)-1,-1,-1):
		yield value[i]
#第一题
class sums():
	def __init__(self,values):
		self.values=values
	def is_prime(self,n):
	    if n == 1:
	        return False
	    for i in range(2, int(sqrt(n))+1):
	        if n % i == 0:
	            return False
	    return n
	def sumss(self,values):
		self.sums=0
		for i in range(values):
			if self.is_prime(i):
				self.sums+=i
		return self.sums