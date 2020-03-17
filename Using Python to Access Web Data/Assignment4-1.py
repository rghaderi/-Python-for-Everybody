from urllib.request import urlopen 
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
sum = 0;
for span in spans:
	sum = sum + int(span.contents[0])
	
print(sum)



