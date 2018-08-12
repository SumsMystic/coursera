'''
Created on July 15, 2018

@author: Sumeet Agrawal
'''

import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1: quit()

print('Retrieving ', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved ', len(data), ' characters')
data.decode()

json_data_dict = json.loads(data)
print('User count:', len(json_data_dict))

comments_list = json_data_dict['comments']
print('Count: ', len(comments_list))

comments_count_sum = 0
for item in comments_list:
    comments_count_sum += int(item['count']) 
    
print("Sum: ", comments_count_sum)