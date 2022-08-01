from googlesearch import search
from Naming import nameReading
from dataScrapper import SongDownloader
import requests
import os


os.makedirs("Songs",exist_ok=True)

def lambda_handler():
    
    names = nameReading()
    downloadLinks = []
    for name in names:
        name += ' song download pagal world'
        songLink = list(search(name,stop = 3))[0]
        link = SongDownloader(songLink)
        downloadLinks.append(link)
    for i in range(len(downloadLinks)):
        r = requests.get(downloadLinks[i])
        
        open(f'Songs/{names[i]}.mp3','wb').write(r.content)
        
lambda_handler()

