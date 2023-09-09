import re

file = open('file.txt', 'r')

# for line in file:
#     line = line.rstrip()
#     if re.search('F..m', line):
#         print(line)

for line in file:
    line = line.rstrip()
    if re.search('E.+th', line):
        print(line)

    if re.search('I.+o', line):
        print(line)

    if re.findall('F..m', line):
        print(line)

    if re.findall('', line):
        print(line)
