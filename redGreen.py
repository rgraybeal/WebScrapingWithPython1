"""

Using CSS to differentiate red and green text

pg 17
https://www.pythonscraping.com/pages/warandpeace.html
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())


headerTags = bs.find_all('h1', 'h2', 'h3')
for tag in headerTags:
    print(tag.get_text())

print("---------------")
nameList2 = bs.find_all(text = 'the prince')
print(len(nameList2))

print("-------------------")
print(bs.h1)
wordList = bs.find_all(text = 'they')

print(len(wordList))
