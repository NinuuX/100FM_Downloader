from os import path
from os import mkdir
from time import sleep
import urllib2

if not path.isdir("100FM MUSIC"):
	mkdir('100FM MUSIC')

headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

print "[INFO] BOOTING UP"

url_req = urllib2.Request("http://www.100fm.co.il/jwplayer/jw_playlist.aspx?id=&Plrandom=0&ptop=0", headers=headers)
data = str(urllib2.urlopen(url_req).read()).split("<title>")

del data[:2]

file_name = []

for i in data:
	file_name.append(" - " + i[:i.find("</title>")])
	file_name.append(i[i.find('<media:credit role="musician">') + len('<media:credit role="musician">'):i.find('</media:credit>')])

	print "[+] Downloading {0}{1} file".format(file_name[1], file_name[0])

	URL = str(i[i.find('<media:content url="') + len('<media:content url="'):i.find('.mp3"') + 4]).replace(" ", "%20").replace("&amp;", "%26")
	req = urllib2.Request(URL , headers=headers)

	open("100FM MUSIC/{0}{1}{2}.mp3".format(PATH, file_name[1].replace("&amp;", "&"), file_name[0].replace("&amp;", "&")) , 'w').write(urllib2.urlopen(req).read())

	del file_name[:]