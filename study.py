#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
def triangles():
	L=[1]
	while True:
		yield L
		L=[L[i-1]+L[i] for i in range(len(L))]
		L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

def x(a):
	return a*a
L=[]
for a in range(10):
	L.append(x(a))
print(L)


digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def strint(s):
	def f(x,y):
		return x*10+y
	def char2num(s):
		return digits[s]
	print(reduce (f,map(char2num,s)))
strint('15731')
