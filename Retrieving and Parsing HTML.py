
import urllib.request, urllib.parse, urllib.error

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in x:
    print(line.decode().strip())
