import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'  
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#獲取本頁所有貼文的資訊####(Q1答案)
title = soup.#把Q1的答案複製到這
################################


for i in range(len(title)):
	if(title[i].find('a') != None):

		#選出此時的貼文資訊並提取出網址(Q3答案)
		href = 'https://www.ptt.cc' + title.#把Q3的答案複製到這
		###################################

		target = href
		req = requests.get(url = target , headers = headers)
		soup = BeautifulSoup(req.text , 'html.parser')

		#獲得貼文內容(Q4)
		content = soup.#答案寫這
		print(content)
		################
