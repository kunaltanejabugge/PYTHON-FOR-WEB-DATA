import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_217218.xml'
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')
tot = 0
for count in counts:
    tot += int(count.text)
    
print('total: ',tot)
