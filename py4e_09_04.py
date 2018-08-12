'''
Created on May 26, 2018

@author: Aakansha
'''

name = input("Enter file:")
email_sender_histo_dict = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line_list = line.split()
    if (len(line_list) > 2 and line_list[0] == 'From'):
        email_sender = line_list[1]
        email_sender_histo_dict[email_sender] = email_sender_histo_dict.get(email_sender, 0) + 1
        
max_sender_count = 0
max_sender_mail = None
for senders_key,senders_count in email_sender_histo_dict.items():
    if (max_sender_count == 0 or senders_count > max_sender_count):
        max_sender_count = senders_count
        max_sender_mail = senders_key
        
print(str(max_sender_mail) + " " + str(max_sender_count))