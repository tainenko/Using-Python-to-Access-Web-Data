import urllib.request, urllib.parse, urllib.error
import json
url=('  http://py4e-data.dr-chuck.net/comments_39013.json')
uh=urllib.request.urlopen(url)
data=uh.read().decode()

info=json.loads(data)
total=0
count=0

for item in info["comments"]:
    total+=int(item['count'])
    count+=1
print('Count:',count)
print('Total:',total)