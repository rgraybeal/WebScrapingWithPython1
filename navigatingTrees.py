"""


https://pythonscraping.com/pages/page3.html


"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
try:

    images = bs.find_all('img', {'src':re.compile('..\/img\/gifts/img.*.jpg')})
    for image in images:
        print(image['src'])
except AttributeError as e:
    print("error")
