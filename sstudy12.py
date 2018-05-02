#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list1=[]
for x in range(10) :
	for y in range(10) :
		if x%2==0:
			if y%2!=0:
				list1.append((x,y))
print(list1)