import requests
from bs4 import BeautifulSoup
import string
import os
import time
import shutil

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://one-piece.cn/comic/'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
folder_path = 'one_piece/'
if os.path.exists(folder_path):
	shutil.rmtree(folder_path)
else:
	os.makedirs(folder_path)

chapters = soup.find('div' , id = 'chapter12')
j = 0;


a_tags = chapters.find_all('a')
#print(a.string.encode(req.encoding).decode('utf-8'))

now = 0
for a in a_tags :
	now += 1
	folder_path = 'one_piece/' + a.string.encode(req.encoding).decode('utf-8') + '/'
	if os.path.exists(folder_path):
		shutil.rmtree(folder_path)
	else:
		os.makedirs(folder_path)
	ep_url = 'https://one-piece.cn/' + a['href']
	#print(ep_url)
	req = requests.get(url = ep_url , headers = headers)
	ep = BeautifulSoup(req.text,'html.parser')
	all_p = ep.find_all('p')
	#print(all_p)
	i = 0
	for p in all_p :
		#print(p)
		i += 1
		if(p.img != None):
			src = p.img['src']
			img_byte = requests.get(src).content
			file = open(folder_path + str(i).zfill(2) + '.png' , 'wb')
			file.write(img_byte)
			file.close()
			print('進度:'+str(now)+'/'+str(len(a_tags))+'   '+str(i)+'/'+str(len(all_p)))
			#img = requests.get(url).content	

