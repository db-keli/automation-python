#!/usr/bin/env python3

import webbrowser as wb
import sys
import pyperclip
if len(sys.argv) > 1:
    spec = '/'.join(sys.argv[1:])
    address = f'https://portal.umat.edu.gh/{spec}'
else:
    address = pyperclip.paste()

wb.open(address)
