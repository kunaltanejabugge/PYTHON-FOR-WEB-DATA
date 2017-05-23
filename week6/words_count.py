import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_217222.json'

uh = urllib.request.urlopen(url)
data = uh.read()

js = json.loads(data)

'''print the sum of all 'count' occurrences. The file has the following structure:
 {
  "note":"This file contains the actual data for your assignment",
  "comments":[
    {
      "name":"abc",
      "count":100
    },
    {
      "name":"cde",
      "count":77
    }, ...
  }
'''

total = 0
for items in js['comments']:
    total = total + int(items['count'])

print('total is ',total)