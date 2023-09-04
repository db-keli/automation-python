#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# req = requests.get('simple.html')

with open('simple.html') as file:
    Soup = BeautifulSoup(file, 'lxml')

link = []
for a in Soup.find_all('div'):
    link.append(a)

print(link[0])
