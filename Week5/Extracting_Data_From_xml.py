import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url='http://py4e-data.dr-chuck.net/comments_39012.xml'
xml=urllib.request.urlopen(url).read()
tree=ET.fromstring(xml)
sum=0
counts=tree.findall('.//comment')
for count in counts:
     sum+=int(count.find('count').text)
print('Sum:',sum)
