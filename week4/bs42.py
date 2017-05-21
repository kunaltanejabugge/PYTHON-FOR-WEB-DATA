from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter - ')
html = urlopen(url, context= ctx).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href',None))
    print('contents:', tag.contents[0])
    print('attrs:', tag.attrs)