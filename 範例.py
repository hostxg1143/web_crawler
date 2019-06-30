from bs4 import BeautifulSoup

html_doc = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title">
			<b>The Dormouse's story</b>
		</p>
		<p class="story">Once upon a time there were three little sisters; and their names were
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
			<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;and they lived at the bottom of a well.
		</p>
		<p class="story">...</p>
	</body>
</html>
'''
soup = BeautifulSoup(html_doc,'html.parser')

#print(soup.head ,'\n')

#print(soup.body,'\n')

#print(soup.p,'\n')

#print(soup.head.p , '\n')

#print(soup.body.p , '\n')

#--------------------------
#print(soup.title , '\n')

#print(soup.title.text , '\n')

#print(soup.b.text , '\n')

#print(soup.body.text, '\n')

#--------------------------

#print(soup.p['class'] , '\n')

#print(soup.a['href'] , '\n')

#--------------------------

#print(soup.find('head') ,'\n')

#print(soup.find('body') ,'\n')

#print(soup.find('p'),'\n')

#print(soup.find('head').find('p') , '\n')

#print(soup.find('body').find('p') , '\n')

print(soup.find('a') , '\n')

#print(soup.find('a' , id  = 'link3') , '\n')

#--------------------------

#print(soup.find_all('a' , 'sister') , '\n')
'''
sister_list = soup.find_all('a' , 'sister')
for sister in sister_list :
	print(sister.text)
'''
#--------------------------

print(soup.find('head').find_next('p') , '\n')

print(soup.find('head').find_next('p').find_next('a') , '\n')

print(soup.find('head').find_next('p').find_next('a' , id = 'link2') , '\n')

#print(soup.find('p').find_next_sibling('p'),'\n')