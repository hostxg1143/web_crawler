import requests
import string
from bs4 import BeautifulSoup
import xlsxwriter
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://m.thsrc.com.tw/tw/Article/ArticleContent/1ee878bf-475a-40d0-8f88-44806522427c'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

#獲得所有row
title = soup.find_all('tr')

#
for m in range(len(title)-2):
	cell = title[m].find_all()  #從第m row中提取 cells
	for n in range(len(cell)):  #判斷各cell 為何種格式
		worksheet.write(m,n,cell[n].text)
workbook.close()
