name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict ={}
for line in handle:
    if not line.startswith("From "):
        continue
    email = (line.split()[1]).strip()
    dict[email] = dict.get(email,0) + 1
 
max = None
most_profilic = None 
for email, count in dict.items():
    if max is None or max< count:
        max = count
        most_profilic = email

print(most_profilic, max)