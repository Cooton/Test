#!/user/bin/env python3
#-*- conding:utf-8 -*-
# import urllib.request
# import requests
# for i in range(5):
# 	response=urllib.request.urlopen('http://placekitten.com/g/500/400')
# 	img=response.read()
# 	with open(str(i)+'图片.jpg','wb')as f:
# 		f.write(img)

import urllib.request
import urllib.parse
import json
import requests
# content = input("请输入需要翻译的内容：")
# head={
# 	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
# }
# url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# data={}
# data['type']= 'AUTO'
# data['i'] = content
# data['doctype']= 'json'
# data['version'] = 2.1
# data['keyfrom'] ='fanyi.web'
# data['ue'] = 'UTF-8'
# data['typoResult']='true'
# data['smartresult']='dict'
# data['client']='fanyideskweb'
# data['salt']='1527170360343'
# data['sign']='7d6a7722320d0f37c198db7e83ba1d38'
# data['action']='FY_BY_CLICKBUTTION'

# data = urllib.parse.urlencode(data).encode('utf-8')
# req=urllib.request.Request(url,data,head)
# response = urllib.request.urlopen(req)
# html = response.read().decode('utf-8')

# target = json.loads(html)
# print("翻译结果为：%s"%(target['translateResult'][0][0]['tgt']))



head={
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
url='http://www.whatismyip.com.tw'
proxy_support=urllib.request.ProxyHandler({'http':'115.229.86.153:9000'})
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
