from bs4 import BeautifulSoup
import requests


def generateImage(query):
    seartext = query
    count = "1"
    adlt = 'off'
    sear = seartext.strip()
    sear = sear.replace(' ', '+')
    URL = 'https://bing.com/images/search?q=' + \
        sear + '&safeSearch=' + adlt + '&count=' + count
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    results = []
    soup = BeautifulSoup(resp.content, "html.parser")
    wow = soup.find('a', class_='iusc')
    return eval(wow['m'])['murl']


print(generateImage("samsung smart phone"))
