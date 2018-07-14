import urllib
import requests
from bs4 import BeautifulSoup
import shutil


def main():
    log_file = open("CH_4.txt", "w")
    log_file.write("歌曲种类：國語歌曲\n\n")

    url_default = "http://sql.jaes.ntpc.edu.tw/javaroom/midi/alas/Ch/"  # ch4_1.mid
    for i in range(1, 4):
        # Download .mid file
        url_use = url_default + "ch4_" + str(i) + ".mid"
        print(url_use)
        with urllib.request.urlopen(url_use) as response, open("./CH_4/ch4_" + str(i) + ".mid", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        '''
        Log information about the song
        1. Get Title
        2. Get Artist Name
        3. Get Lyrics

        '''

        wiki = url_default + "lyrics4_" + str(i) + ".htm"

        html = requests.get(wiki)
        html.encoding = 'utf-8'
        html = html.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.title)


main()