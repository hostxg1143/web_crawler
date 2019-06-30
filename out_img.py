import requests
from bs4 import BeautifulSoup
import re
import string
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://wall.alphacoders.com/by_sub_category.php?id=172897&name=%E7%88%B1%E4%B8%BD%E4%B8%9D%E6%A2%A6%E6%B8%B8%E4%BB%99%E5%A2%83+%E5%A3%81%E7%BA%B8&lang=Chinese'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
#找出一頁有幾張圖
picture = soup.find_all('div', 'boxgrid')

for i in range(len(picture)):
	#進入第i張圖的頁面
	page = 'https://wall.alphacoders.com/' + picture[i].find_next('a')['href']
	target = page
	req = requests.get(url=target,headers=headers)
	soup = BeautifulSoup(req.text, 'html.parser')
	#獲取圖片網址
	addr = soup.find('div', 'center img-container-desktop').find_next('a')['href']
	#獲取圖片內容
	img = requests.get(addr).content
	#輸出成PNG檔
	file = open('pic2/'+str(i)+'.png','wb')
	file.write(img)
	file.close()
	print('第'+str(i)+'張圖片下載完成')