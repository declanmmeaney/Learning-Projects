
import urllib.request, urllib.parse, urllib.error
import json

w = input('URL -')

x = urllib.request.urlopen(w)

y = x.read()

sum = 0

info = json.loads(y)

x = info['comments']

for item in x:
    #print('Name', item['name'])
    z = item['count']        
    sum = sum + int(z)

print(sum)
