import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
data = urllib.request.urlopen(url, context = ctx).read()
data = json.loads(data)

count = 0;
for comment in data['comments']:
	count = count + int(comment['count'])
print(count)

