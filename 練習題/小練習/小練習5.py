import requests
from bs4 import BeautifulSoup
import string

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://practice2.1mb.site/'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

divs = 

for div in divs :	
	text = 
	print(text)



