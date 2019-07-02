import requests
from bs4 import BeautifulSoup
import string
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/post/10947/'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

folder_path = 'C:\\Users\\吳振瑋\\Desktop\\真的會用到的\\海賊王圖片\\'
if (os.path.exists(folder_path) == False): #判斷資料夾是否存在
    os.makedirs(folder_path) #Create folder

all_p = soup.find_all('p')
i = 0
for p in all_p :
	if(p.img != None):
		i += 1
		src = p.img['src']
		img_byte = requests.get(src).content
		file = open(folder_path + str(i) + '.png' , 'wb')
		file.write(img_byte)
		file.close()
		print('第'+str(i)+'張圖片下載完成')
	#img = requests.get(url).content


