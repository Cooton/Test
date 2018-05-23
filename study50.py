#!/user/bin/env python3
#-*- conding:utf-8 -*-
class Const:
	def __setattr__(self,name,value):
		if name in self.__dict__:
			raise TypeError('常量无法改变')
		if not name.isupper():
			raise TypeError('常量名必须为大小写')
		self.__dict__[name]=value

import sys
sys.modules[__name__]=Const()
