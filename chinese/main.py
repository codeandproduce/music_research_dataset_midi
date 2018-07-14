from lxml import html
import urllib
import requests
import shutil
from bs4 import BeautifulSoup




def main():
    log_file = open("CH_4.txt", "w")
    log_file.write("歌曲种类：國語歌曲\n\n")

    url_default = "http://sql.jaes.ntpc.edu.tw/javaroom/midi/alas/Ch/"  # ch4_1.mid
    for i in range(1, 4):

        # Download .mid file
        url_use = url_default + "ch4_" + str(i) + ".mid"
        print(url_use)
        with urllib.request.urlopen(url_use) as response, open("./CH_4/ch4_"+str(i)+".mid", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)


        '''
        Log information about the song
        1. Get Title
        2. Get Artist Name
        3. Get Lyrics
        
        '''
        page = requests.get(url_default + "lyrics4_" + str(i) + ".htm")
        tree = html.fromstring(page.content)

        log_file.write("國語4的第"+str(i)+"首歌,\t\t")

        # Get Title:
        title = tree.xpath("//title/text()")
        log_file.write("歌名：" + title[0]+"\n")

        # Get Artist Name

        artist_name = tree.xpath('//*[contains(text(), "唱：")]')
        print(artist_name[0].text_content())
        artist_name = artist_name[0].text_content()

        if artist_name != []:
            log_file.write(artist_name[0]+"\n")
        else:
            log_file.write("Not Provided\n")

        # Get Lyrics
        lyrics = tree.xpath('//tr//td/text()')
        print("lyrics:")
        print(lyrics)

        if lyrics == []:
            lyrics = tree.xpath('//td//font/text()')
            if lyrics == []:
                lyrics = tree.xpath('//td//strong/text()')

        log_file.write("歌词:\n")
        for i in lyrics:
            log_file.write(i+"\n")


        # Space between songs
        log_file.write("\n\n\n")


main()