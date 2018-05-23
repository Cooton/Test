#!/user/bin/env python3
#-*-conding:utf-8-*-
# class Hunter:
# 	"""docstring for hunter"""
# 	count=0
# 	def __init__(self):
# 		self.x=5
# 		self.y=4
# 		Hunter.count+=1
# 	def __del__(self):
# 		Hunter.count-=1
class Stack:
	def __init__(self,start=[]):
		self.stack=[]
		for x in start:
			self.push(x)
	def isEmpty(self):
		return not self.stack
	def push(self,x):
		self.stack.append(x)
	def pop(self):
		return self.stack.pop()
	def top(self):
		if not self.stack:
			print('栈为空')
		else:
			return self.stack[-1]
	def bottom(self):
		if not self.stack:
			print('栈为空')
		else:
			return self.stack[0]