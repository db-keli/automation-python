#!/usr/bin/env python3
import re
file = open('try.txt')
for line in file:
    line = line.rstrip()
    if re.search('F..m:', line):
        print(line)

#Extracting Data Using Regexes
s = 'A message frome csev@umich.edu to cwen@iupui.edu about meeting @2PM'
list = re.findall('\S+@\S+', s)
print(list)

