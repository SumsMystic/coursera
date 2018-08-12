'''
Created on May 26, 2018

@author: Aakansha
'''

name = input("Enter file:")
email_send_hr_histo_dict = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line_list = line.split()
    if (len(line_list) > 2 and line_list[0] == 'From'):
        email_send_hr_str = line_list[5]
        email_send_hr_lst = email_send_hr_str.split(':')
        email_send_hr = email_send_hr_lst[0]
        email_send_hr_histo_dict[email_send_hr] = email_send_hr_histo_dict.get(email_send_hr, 0) + 1

sorted_lst = sorted([(k,v) for k,v in email_send_hr_histo_dict.items()])
for (k,v) in sorted_lst:
    print(str(k) + " " + str(v))
