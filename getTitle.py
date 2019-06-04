"""
Reusable code bit

Get title
function returns the title of a web address or returns a none object if
there is an issue.
Captures http errors
"""

from urllib.request import urlopen
from urlib.error import HTTPError
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
