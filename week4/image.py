import urllib.request, urllib.error, urllib.parse

img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg').read()
file = open('cover.jpg','wb')
file.write(img)
file.close()