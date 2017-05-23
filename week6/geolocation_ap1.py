import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address':address})
    
    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf-8')
    
    js = json.loads(data)
    
    place = js["results"][0]["place_id"]
    print(place)