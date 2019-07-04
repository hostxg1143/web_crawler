import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

###獲得下一頁的網址####(Q2)
next_page ='https://www.ptt.cc'+soup.find('div','btn-group btn-group-paging').find_next('a','btn wide').find_next_sibling('a')['href']
print(next_page)
######################