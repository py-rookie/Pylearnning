# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:35:14 2018

@author: Chen YC
"""

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

soup.find_all('a') #return as a ResultSet object
soup.p.contents #return as a list
contentList=list(soup.descendants)
nameList=[]
for j in range(len(contentList)):
    if -1<str(contentList[j]).rfind('href')<19:
        print(j+1,' ', contentList[j+1])
        nameList.append(str(contentList[j+1]))

