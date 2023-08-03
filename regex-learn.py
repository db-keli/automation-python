#!/usr/bin/env python3
import re
file = open('try.txt')
for line in file:
    line = line.rstrip()
    if re.search('F..m:', line):
        print(line)