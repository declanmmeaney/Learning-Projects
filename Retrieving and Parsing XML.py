
import urllib.request, urllib.parse, urllib.error
import re
import xml.etree.ElementTree as ET

w = input('URL -')

x = urllib.request.urlopen(w)

y = x.read()

sum = 0

stuff = ET.fromstring(y)
lst = stuff.findall('comments/comment')
print('Comment count:', len(lst))

for item in lst:
    z = item.find('count').text
    sum = sum + int(z)

print(sum)
