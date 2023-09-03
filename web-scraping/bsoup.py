#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
req = requests.get('http://nostarch.com')

with req as req:
    noStarchSoup = BeautifulSoup(req.text, 'lxml')

print(noStarchSoup)
tag = noStarchSoup.b
print(tag.name)

with open('index.html', 'w') as f:
    f.write(noStarchSoup.prettify())
