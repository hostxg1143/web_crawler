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
chapters =
##############################################


#從 chapters 裡面抓取所有 <a> 標籤
#---------------------Q2---------------------#
##############################################

a_tags = 

##############################################
for a in a_tags:
	print(a.encode(req.encoding).decode('utf-8'))