# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value=0
count =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find('.')
    value = value + float(line[pos-1:])
    count = count + 1
print('Average spam confidence:', value/count)
