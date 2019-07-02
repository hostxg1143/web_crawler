import requests
from bs4 import BeautifulSoup
import string
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/comic/'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
folder_path = 'C:\\Users\\吳振瑋\\Desktop\\真的會用到的\\海賊王圖片\\'
if (os.path.exists(folder_path) == False): #判斷資料夾是否存在
	os.makedirs(folder_path) #Create folder


chapters = soup.find_all('div' , 'chapter')
j = 0;
for chapter in chapters :
	j += 1
	folder_path = 'C:\\Users\\吳振瑋\\Desktop\\真的會用到的\\海賊王圖片\\' + str(j) + '\\'
	if (os.path.exists(folder_path) == False) : #判斷資料夾是否存在
		os.makedirs(folder_path) #Create folder
	a_tags = chapter.find_all('a')
	i = 0
	for a in a_tags :
		ep_url = 'https://one-piece.cn/comic/' + a['href']
		req = requests.get(url = ep_url , headers = headers)
		ep = BeautifulSoup(req.text,'html.parser')
		all_p = ep.find_all('p')
		for p in all_p :
			i += 1
			src = p.img['src']
			img_byte = requests.get(src).content
			file = open(folder_path + str(i) + '.png' , 'wb')
			file.write(img_byte)
			
			file.close()
			print('第'+str(i)+'張圖片下載完成')
			#img = requests.get(url).content	

