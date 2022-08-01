from bs4 import BeautifulSoup
import requests

def SongDownloader(link):
    r = requests.get(link)
    page = BeautifulSoup(r.content,'html5lib')
    block = page.find_all('div',{'class':'div-nogap'})[0]
    innerblock = block.find('div',{'class': 'div-nogap'})
    print(link)
    downloadblock = innerblock.find('div',{'class':'downloaddiv'})
    downloadLink = downloadblock.find('a')
    link = downloadLink.get('href')
    return link

