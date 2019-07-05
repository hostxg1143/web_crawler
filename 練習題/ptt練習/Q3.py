import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#獲取本頁所有貼文的資訊(Q1答案)
############################
title = soup.#把Q1的答案複製到這
############################

for i in range(len(title)):
	if(title[i].find('a') != None):
		#選出此頁的貼文資訊並提取出網址(Q3)
		################################
		href = 'https://www.ptt.cc' + title.#答案寫這
		################################
		print(href)