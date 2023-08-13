#!/usr/bin/env python3
import re
# file = open('try.txt')
# for line in file:
#     line = line.rstrip()
#     if re.search('F..m:', line):
#         print(line)

# #Extracting Data Using Regexes
# s = 'A message frome csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# list = re.findall('\S+@\S+', s)
# print(list)
sentence = ' . . start a sentence and then bring abc it to an end, kekelidompeh@gmail.com 234 start 43'
number = '''
        9894mike-342-2342
        8678-43545-1323
        '''
        
pattern = re.compile(r'\d\d\d\d[m-]ike')

matches = pattern.finditer(number)
for match in matches:
    print(match)
    