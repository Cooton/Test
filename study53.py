#!/user/bin/env python3
#-*- conding:utf-8 -*-
import urllib.request
import requests
# for i in range(5):
# 	response=urllib.request.urlopen('http://placekitten.com/g/500/400')
# 	img=response.read()
# 	with open(str(i)+'图片.jpg','wb')as f:
# 		f.write(img)

# import urllib.request
# import urllib.parse
# import json

# content = input("请输入需要翻译的内容：")

# url='https://translate.google.cn/'

# data={}
# data['type']= 'AUTO'
# data['i'] = content
# data['doctype']= 'json'
# data['xmlVersion'] = 1.8
# data['keyfrom'] ='fanyi.web'
# data['ue'] = 'UTF-8'
# data['typoResult']='true'
# data = urllib.parse.urlencode(data).encode('utf-8')


# response = urllib.request.urlopen(url,data)
# html = response.read().decode('utf-8')

# target = json.loads(html)
# print("翻译结果为：%s"%(target['translateResult'][0][0]['tgt']))

# DOWNLOAD_URL = 'http://movie.douban.com/top250/'
#
# def download_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
#     }
#     data = requests.get(url, headers=headers).content
#     return data
# def main():
#     print(download_page(DOWNLOAD_URL))
#
# if __name__ == '__main__':
#     main()
import requests
"""
爬取豆瓣电影TOP250 - 完整示例代码
"""

import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250/'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()

        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
if __name__ == '__main__':
    main()