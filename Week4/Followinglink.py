import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=' http://py4e-data.dr-chuck.net/known_by_Safia.html'


#Retrieve all of the anchor tags
counts=7
position=18

for i in range(counts):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    address = 1

    for tag in tags:
        if address==position:
            url=tag.get('href',None)
            print('Retrieving:',url)
        address+=1