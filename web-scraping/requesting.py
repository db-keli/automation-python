#!/usr/bin/env python3

import requests

req = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(req))

print(req.status_code == requests.codes.ok)

print(len(req.text))
print(req.text[:250])

print(req.raise_for_status())

req2 = requests.get('https://inventwithpython.com/page_that_does_not_exist')

try:
    req2.raise_for_status()
except Exception as exc:
    print(f'There was a problem:{exc}')
