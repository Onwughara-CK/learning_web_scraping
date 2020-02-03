from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.html.title
    except AttributeError as e:
        return None
    return title

def title_of_website(url):
    title = get_title(url)
    if title == None:
        return 'Site could not be retrieved'
    else:
        print(title)
    return
    