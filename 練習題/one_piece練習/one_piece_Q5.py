import requests
from bs4 import BeautifulSoup
import string
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn//post/10903/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#找出能抓到所有圖片的標籤
#------------------放Q4的答案-----------------#
#############################################
all_p = 
#############################################

for p in all_p:
	if(p.img != None):
		#找出圖片的連結
		#ex.從<img alt="海贼王 第903话 第五位皇帝" src="http://wx3.sinaimg.cn/large/83940082gy1fqs2l5szexj20nm0y6wsm.jpg" />中
		#   找出"http://wx3.sinaimg.cn/large/83940082gy1fqs2l5szexj20nm0y6wsm.jpg"
		#---------------------Q5--------------------#
		#############################################

		src = 
	
		#############################################
		print(src)