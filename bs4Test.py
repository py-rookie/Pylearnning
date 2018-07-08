# -*- coding: utf-8 -*-

#according to book to test
"""
Created on Sun Jul  8 00:35:14 2018

@author: Chen YC
"""

import bs4
htmlDoc = open('htmlExample.html')
htmlDoc = bs4.BeautifulSoup(htmlDoc.read())
elem=htmlDoc.select('p a')
nameList=[]
for i in range(len(elem)):
    item = elem[i].getText()
    nameList.append(item)

print(nameList)


