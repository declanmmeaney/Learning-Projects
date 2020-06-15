
count = 0

x = open('mbox-short.txt')
for line in x:
    line = line.rstrip()
    if not line.startswith('From '): continue
    parts = line.split()
    email = parts[1]
    count = count + 1


    print(email)
print("There were", count, "lines in the file with From as the first word")
