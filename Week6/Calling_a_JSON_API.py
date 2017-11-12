import urllib.request,urllib.parse,urllib.error
import json

serviceurl='http://py4e-data.dr-chuck.net/geojson?'

while True:
    address=input('Enter location: ')
    #location: Fachhochschule FH Salzburg
    if len(address)<1:break

    url=serviceurl+urllib.parse.urlencode({'address': address})
    print('Retrieving',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieved', len(data),'characters')
    print('Retrieved', len(data))

    try:
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js,indent=4))

    id=js["results"][0]["place_id"]
    print('Place id:',id)

