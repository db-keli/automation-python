#!/usr/bin/env python3

import requests
import sys
import webbrowser
from bs4 import BeautifulSoup

search = ' '.join(sys.argv[1:])
req = requests.get(f'https://google.com/search?q={search}')

soup = BeautifulSoup(req.text, 'lxml')

with open('search.html', 'w') as file:
    file.write(soup.prettify())

linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(f'https://google.com' + linkElems[i].get('href'))
