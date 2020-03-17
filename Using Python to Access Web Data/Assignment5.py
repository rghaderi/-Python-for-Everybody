import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
data = urllib.request.urlopen(url, context = ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

sum =0
for count in counts:
	sum = sum + int(count.text)

print(sum)