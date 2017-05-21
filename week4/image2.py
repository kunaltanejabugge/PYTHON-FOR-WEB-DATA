import urllib.request, urllib.error, urllib.parse

img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg')
file = open('cover.jpg','wb')
size = 0
while True:
    info = img.read(100000)
    if len(info)<1:
        break
    size = size + len(info)
    file.write(info)
    
print(size , "character copied.")
file.close()