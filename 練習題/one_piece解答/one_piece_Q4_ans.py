import requests
from bs4 import BeautifulSoup
import string
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn//post/10903/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#找出能抓到所有圖片的標籤
#---------------------Q4--------------------#
#############################################

all_p = soup.find_all('p')

#############################################

for p in all_p:
	print(p.encode(req.encoding).decode('utf-8'))