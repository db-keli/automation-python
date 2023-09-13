#! /usr/bin/env python3

import sys
import requests
import json

if len(sys.argv) < 2:
    print('Usage: weather.py <location>')
location = ' '.join(sys.argv[1:])
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3" % location
response = requests.get(url)
response.raise_for_status()
