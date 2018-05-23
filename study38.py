#!/user/bin/env python3
#-*-conding:utf-8-*-
import math
class Point1:
	p=[]
	def dian(self,x,y):
		self.x=x
		self.y=y
		p=[x,y]
		return p
class Line:
	"""docstring for Line"""

	def getLen(self,p1,p2):

		arg=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
		return arg
class Point2(Point1):
	pass	
a1=Point1()
a2=Point2()
p1=a1.dian(1,1)
p2=a2.dian(4,5)
print(p1,p2)
l=Line()
chang=l.getLen(p1,p2)
print(chang)
