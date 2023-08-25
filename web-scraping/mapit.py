#!/usr/bin/env python3
import webbrowser as wb
import sys
from pyperclip import paste

if len(sys.argv) > 1:
    address = ''. join(sys.argv[1:])
else:
    address = paste()

wb.open(f'https://www.google.com/maps/place/{address}')
