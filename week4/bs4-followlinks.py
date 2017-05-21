import urllib
from bs4 import BeautifulSoup

url = input('enter url: ')
count = int(input('enter count: '))
position = int(input('enter position: '))

for num in range(0,count+1):
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    if num < count:
        print('retrieving: ',url)
    else:
        print('last url: ',url)
        break
    
    tags = soup('a')
    
    pos = 0 
    for tag in tags:
        if pos == position - 1:
            url = str(tag.get('href',None))
            break
        pos += 1