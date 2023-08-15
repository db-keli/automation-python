#!/usr/bin/env python

import os
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.isabs(os.path.abspath(".")))

hellofile = open('/home/kekeli/Repos/automation-python/hello.txt', 'r')
hellocontent = hellofile.readlines()
print(hellocontent)
hellofile.close()

baconfile = open('bacon.txt', 'w')
message = 'I love me some more bacon'
baconfile.write(message)
baconfile.close()

baconfile = open('bacon.txt')
content = baconfile.read()
print(content)
