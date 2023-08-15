#!/usr/bin/env python
import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileobj = open('cats.py', 'w')
pcats = pprint.pformat(cats)
fileobj.write('cats = %s \n' % pcats)
fileobj.close()

fileobj = open("cats.py")
print(fileobj.read())