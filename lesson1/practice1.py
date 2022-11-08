'''
Используемые библиотеки:

beautifulsoup - библиотека для преобразование страницы сайта в дерево эл. python
Она предоставляет набор инструментов для извлечения информации из этого самого дерева

lxml - парсер HTML страниц
'''

from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

''' Методы BeautifulSoup '''



