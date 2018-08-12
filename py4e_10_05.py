'''
Created on June 24, 2018

@author: Sumeet Agrawal
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

print("Retrieving: ", url)
tags = soup('a')
for looper in range(count):
    # Look at the parts of a tag
    tag = tags[position-1]
    print('Contents:', tag.contents[0])
    url = tag.get('href', None)
    print("Retrieving: ", url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
