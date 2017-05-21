import urllib.request, urllib.error, urllib.parse

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file:
    print(line.decode().strip())