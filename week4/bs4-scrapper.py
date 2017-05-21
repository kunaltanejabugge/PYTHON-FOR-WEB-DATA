import urllib
from bs4 import BeautifulSoup

url = input('enter url: ')
link = urllib.request.urlopen(url)
soup = BeautifulSoup(link,'html.parser')

spans = soup('span')

numbers = list()

for span in spans:
    numbers.append(int(span.string))
    
print(sum(numbers))