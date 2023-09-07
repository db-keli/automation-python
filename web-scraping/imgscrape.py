#!usr/bin/env python3

from bs4 import BeautifulSoup
import os
import lxml

import requests

url = 'https://xkcd.com'

while not url.endswith('#'):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    print(req.raise_for_status())
