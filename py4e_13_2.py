'''
Created on July 15, 2018

@author: Sumeet Agrawal
'''

import urllib.request, urllib.parse
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'


address = input('Enter location: ')
if len(address) < 1: quit()

url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Address entered is invalid ====')
    print(data)
    quit()

location = js['results'][0]['place_id']
print("Place id: ", location)

