#! /usr/bin/env python3

import sys
import requests
import json

if len(sys.argv) < 2:
    print('Usage: weather.py <location>')
location = ' '.join(sys.argv[1:])
url = "https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=3504dc1eaa44375489b5824fd20b9f66" % location
response = requests.get(url)
data = json.loads(response.text)
