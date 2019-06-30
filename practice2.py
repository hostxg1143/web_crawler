import requests
from bs4 import BeautifulSoup
import string

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://practice2.1mb.site/'   #ptt-NBA-board第一頁
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')

#find title
print(soup.title)

#find the person's name(example 1)
print(soup.ol.li.find_next_sibling().find_next_sibling().string)

#find the person's name(example 2)
print(soup.find_all("li")[2].string)

#find href of the university
print(soup.find_all("li")[1].a['href'])

#print out all of the  animes
div = soup.find_all("div" , "anime")
for subDivs in div :
	print(subDivs.img['src'])
	print(subDivs.text.strip())
	print("\n")

#print out all of the deamas
div = soup.find_all("div" , "drama")
for subDivs in div:
	print(subDivs.img['src'])
	print(subDivs.text.strip())
	print("\n")