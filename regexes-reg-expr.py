#!/usr/bin/env python

# Using Regexes to find better patterns

import re
import sys
num = str(sys.argv[1])
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(num)
if mo is not None:
    print('Number found: ' + mo.group())
else: print('No matching')