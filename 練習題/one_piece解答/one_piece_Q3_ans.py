import requests
from bs4 import BeautifulSoup
import string
import os
import time
import shutil
#前置步驟(不用改)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/comic/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#------------------放Q1的答案-----------------#
##############################################
chapters = soup.find('div' , id = 'chapter12')
##############################################

#------------------放Q2的答案-----------------#
##############################################
a_tags = chapters.find_all('a')
##############################################

for a in a_tags:
	#從 <a> 標籤中取出"href"連結
	#ex. 從<a href="/post/10903/" target="_blank">第903话 第五位皇帝</a>中 取出 "/post/10903/"
	#---------------------Q3--------------------#
	#############################################

	ep_url = 'https://one-piece.cn/' + a['href']
	
	#############################################
	
	print(ep_url)