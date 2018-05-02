#!/user/bin/env python3
#-*- conding:utf-8 -*-
def funOut():
	def funIn():
		print('你成功访问到我啦！')
	return funIn
funOut()