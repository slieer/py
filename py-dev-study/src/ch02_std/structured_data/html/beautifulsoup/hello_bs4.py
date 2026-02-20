#!/usr/bin/python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup

html_doc = open('hello_bs4.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))
print(soup.get_text())
