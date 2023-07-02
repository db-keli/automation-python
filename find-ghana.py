# A program to check if the number of a user is ghanaian or not
#!/usr/bin/env python

import re
import sys

number = str(sys.argv[1])

def ghana(number):
    ghana = re.compile('(\\d\\d\\d)-(\\d\\d\\d\\d\\d\\d\\d\\d\\d)')
    mo = ghana.search(number)
    if mo.group(1) == '233':
        print("He's Ghanaian!!")
    else:
        print("Oh Dang, A foreigner")
        
ghana(number)