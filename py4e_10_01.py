import re

sum_num = 0
fhandle = open('regex_sum_84847.txt')
for line in fhandle:
	num_list = re.findall('[0-9]+', line)
	sum_num = sum_num + sum([int(x) for x in num_list])
	'''
	for x in num_list:
		sum_num = sum_num + int(x)
	'''

print(sum_num)