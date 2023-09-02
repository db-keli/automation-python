#!/usr/bin/env python3
import requests
import bs4

req = requests.get('http://nostarch.com')
print(req.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(req.text)
print(type(noStarchSoup))
