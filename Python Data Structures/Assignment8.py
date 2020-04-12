name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict ={}
for line in handle:
    if not line.startswith('From '):
        continue
    time = line.split()[-2]
    hour = time.split(':')[0]
    dict[hour] = dict.get(hour, 0) + 1
    

temp  = dict.items()
temp = sorted(temp )
for k,v in temp:
    print (k , v)
    
    
    
