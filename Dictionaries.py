
name = open("mbox-short.txt")

counts = dict()

for line in name:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigemail = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email 
        bigcount = count

print(bigemail, bigcount)
