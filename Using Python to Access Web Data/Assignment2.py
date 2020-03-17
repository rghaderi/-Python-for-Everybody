import re 

file = open('regex_sum_378536.txt')
summ = 0
#for line in file:
#	nums = re.findall('([0-9]+)',line)
#	summ = summ + sum([int(num) for num in nums])
#
#print (summ)
print(sum([int(num) for num in re.findall('([0-9]+)',file.read())]))
	
