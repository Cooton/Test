#!/user/bin/env python3
#-*-conding:utf-8-*-
class Price:
	def __init__(self,adult,chile,date='非星期天'):
		self.adult=adult
		self.chile=chile
		self.date=date
	def lala(self):
		price_a=100*(int(self.adult))
		price_c=50*(int(self.chile))
		sum=price_a+price_c
		if self.date=='星期天':
			print('星期天总价为%d元'%(sum*1.2))
		print('总价为%d元'%sum)
class Wugui:
	HP=100
	foot1=1
	foot2=2
	def eat(self):
		self.HP+=30
		if self.HP>=100:
			self.HP=100
	def walk(self):
		pass
	def dead(self):
		if HP<=0:
			print('Game over')

class Fish:
	foot=1

	def walk(self):
		pass