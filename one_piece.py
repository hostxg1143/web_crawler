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
folder_path = 'one_piece/'

# 建立 one_piece 資料夾(不用改)
if os.path.exists(folder_path):
	shutil.rmtree(folder_path)
else:
	os.makedirs(folder_path)

#抓取 id 為 chapter12 的 <div> 標籤(Q1)
chapters = soup.find('div' , id = 'chapter12')
#####################################


#從 chapters 裡面抓取所有 <a> 標籤(Q2)
a_tags = chapters.find_all('a')
#############################################

j = 0
now = 0
for a in a_tags :
	now += 1
	#建立 第n話 資料夾(不用改)
	folder_path = 'one_piece/' + a.string.encode(req.encoding).decode('utf-8') + '/'
	if os.path.exists(folder_path):
		shutil.rmtree(folder_path)
	else:
		os.makedirs(folder_path)
	########################

	#從 <a href="/post/10903/" target="_blank">第903话 第五位皇帝</a> 中取出"href"連結(Q3)
	ep_url = 'https://one-piece.cn/' + a['href']
	###################################################################################

	#進入連結(不用改)
	req = requests.get(url = ep_url , headers = headers)
	ep = BeautifulSoup(req.text,'html.parser')
	###############

	#找出能抓到所有圖片的標籤
	#---------------------Q4---------------------
	all_p = ep.find_all('p')
	
	i = 0
	for p in all_p :
		i += 1
		#確認在此<p>標籤當中是有<img>標籤的
		if(p.img != None):
			#從<img alt="海贼王 第903话 第五位皇帝" src="http://wx3.sinaimg.cn/large/83940082gy1fqs2l5szexj20nm0y6wsm.jpg" />
			#中找出圖片的連結(Q5)
			src = p.img['src']
			#############################################

			#進行存取  下載(不用改)
			img_byte = requests.get(src).content
			file = open(folder_path + str(i).zfill(2) + '.png' , 'wb')
			file.write(img_byte)
			file.close()
			
			#匯報進度(不用改)
			print('進度:'+str(now)+'/'+str(len(a_tags))+'   '+str(i)+'/'+str(len(all_p)))
			
