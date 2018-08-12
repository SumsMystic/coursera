'''
Created on July 7, 2018

@author: Sumeet Agrawal
'''

import urllib.request
import xml.etree.ElementTree as ET

serviceurl1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
serviceurl2 = 'http://py4e-data.dr-chuck.net/comments_84851.xml'

address = input('Enter location: ')
if len(address) < 1: quit()

print('Retrieving ', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved ', len(data), ' characters')
data.decode()
tree = ET.fromstring(data)

num_comment_nodes = 0
total_comments_sum = 0

comments_tree_lst = tree.findall('.//comment')
num_comment_nodes = len(comments_tree_lst)
for each_comment in comments_tree_lst:
    count_node_txt = each_comment.find('count').text
    total_comments_sum = total_comments_sum + int(count_node_txt)

print('Count: ', num_comment_nodes)
print('Sum: ', total_comments_sum)
