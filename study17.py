#!/use/bin/env python3
#-*- conding:utf-8 -*-
a=[1,2,3,4,5,'a','b']
zong=0
for x in a:
	if(type(x)==int) or (type(x)==float):
		zong=zong+x
	else:
		continue
print(zong)