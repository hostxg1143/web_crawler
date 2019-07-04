import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#獲取本頁所有貼文的資訊-------(Q1)
title = soup.find_all('div' , 'title')
print(title)

print(title)