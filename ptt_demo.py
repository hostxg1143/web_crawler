import requests
from bs4 import BeautifulSoup
import string
import os
import shutil
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://www.ptt.cc/bbs/NBA/index.html'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
#print(soup.prettify())
num = 0
first_dir='ptt/'
if os.path.exists(first_dir):
	shutil.rmtree(first_dir)
else:
	os.makedirs(first_dir)
#小爬個兩頁
for page in range(2):
	#建立子資料夾
	second_dir='ptt/'+'page'+str(page+1)+'/'
	if os.path.exists(second_dir):
		shutil.rmtree(second_dir)
	else:
		os.makedirs(second_dir)
	#獲取本頁所有貼文的資訊-------(Q1)
	title = soup.find_all('div','title')
	
	#獲得下一頁的網址-------(Q2)
	next_page ='https://www.ptt.cc'+soup.find('div','btn-group btn-group-paging').find_next('a','btn wide').find_next_sibling('a')['href']
	#單獨進入各貼文
	for i in range(len(title)):
		if(title[i].find('a')!=None): #若貼文非已刪除貼文
			#選出此時的貼文資訊並提取出網址-------(Q3)
			href='https://www.ptt.cc'+title[i].find('a')['href']
			
			target = href
			req = requests.get(url=target,headers=headers)
			soup = BeautifulSoup(req.text,'html.parser')
			#獲得貼文內容-------(Q4)
			content = soup.find('div',id="main-container").text
			#輸出檔案
			file = open(second_dir+str(num+1)+'.txt','w', encoding = 'UTF-8')
			file.write(str(content))
			file.close()
			num+=1
			print('第'+str(num)+'篇文章下載完成')
			
	target = next_page
	req = requests.get(url=target,headers=headers)
	soup = BeautifulSoup(req.text,'html.parser')
	#print(href[i].text.strip())
	#print(href[i].find('a').text)
#for i in range(len(href)):
#for ch in soup.find('div', 'b-ent').children:
#	print(ch.find_next())
#	print('==================')

#for i in range(len(href)):
#	print(href[i].contents[1].contents[7].string)

