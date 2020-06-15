x = open('mbox-short.txt')

counts = dict()

for line in x:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    pieces = time.split(':')
    hour = pieces[0]
    counts[hour] = counts.get(hour, 0) + 1

y = list()
for key, val in counts.items():
    newtup = (key, val)
    y.append(newtup)

y = sorted(y)

for val, key in y:
    print(val, key)
