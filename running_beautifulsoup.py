from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup



def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(">>>get Title HTTPError")
        print(e)
        return None

    try:
        bsObject = BeautifulSoup(html.read(), 'html.parser')
        title = bsObject.body.h1
    except AttributeError as e:
        print(">>>Attribute error")
        print(">>>", e)
        return None
    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print("Title could not be found")
else:
    print(title)
