import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=' http://py4e-data.dr-chuck.net/comments_39010.html'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags
tags=soup('span')
counts=0
for tag in tags:
    counts+=int(tag.contents[0])
print(counts)