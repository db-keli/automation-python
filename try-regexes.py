#!/usr/bin/env python

#Using Regexes to find a pattern in a string
import re
import sys

string = sys.argv[1]

def reg_get(string):
    global mo
    pattern = re.compile('Kofi')
    mo = pattern.search(string)
    if mo is not None:
        print("Regex found " + mo.group())

reg_get(string)
