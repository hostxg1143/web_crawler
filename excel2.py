import requests
import string
from bs4 import BeautifulSoup
import xlsxwriter
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
target = 'https://m.thsrc.com.tw/tw/Article/ArticleContent/1ee878bf-475a-40d0-8f88-44806522427c'
req = requests.get(url=target,headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')

workbook = xlsxwriter.Workbook('demo2.xlsx')
worksheet = workbook.add_worksheet()
#增添儲存格格式(字顏色,背景色,置中)
pink = workbook.add_format({'bg_color':'#FFEBEF','align':'center'})
blue = workbook.add_format({'bg_color':'#E4F6FF','align':'center'})
non = workbook.add_format({'align':'center'})
tit = workbook.add_format({'font_color':'#FFFFFF','bg_color':'#7D7C7E','align':'center'})
#獲得所有row
title = soup.find_all('tr')

#
for m in range(len(title)-2):
	cell = title[m].find_all()  #從第m row中提取 cells
	for n in range(len(cell)):  #判斷各cell 為何種格式
		if cell[n].name == 'th':
			worksheet.write(m,n,cell[n].text,tit)
		elif cell[n]['class'][0] == 'FFEBEF':
			worksheet.write(m,n,cell[n].text,pink)
		elif cell[n]['class'][0] == 'E4F6FF':
			worksheet.write(m,n,cell[n].text,blue)
		else :
			worksheet.write(m,n,cell[n].text,non)
workbook.close()
