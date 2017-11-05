import urllib.request, urllib.parse, urllib.error
fhand=rullib.request.rulopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

