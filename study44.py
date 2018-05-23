#!/user/bin/env python3
#-*-conding:utf-8-*-
import time as t
class Mytimer(object):
	def __init__(self):
		self.begin=0
		self.end=0
	def start(self):
		self.begin=t.time()
		print('计时开始')
	def stop(self):
		self.end=t.time()
		self._cale()
		print('计时结束')
	def _cale(self):
		self.pormpt='总共运行了'
		self.pormpt+=str(self.end-self.begin)
		print(self.pormpt)