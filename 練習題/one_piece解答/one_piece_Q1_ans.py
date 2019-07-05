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

#抓取 id 為 chapter12 的 <div> 標籤
#<div id="chapter12" class="chapter">......</div>
#---------------------Q1--------------------#
#############################################

chapters = soup.find('div' , id = 'chapter12')

#############################################

print(chapters.encode(req.encoding).decode('utf-8'))

