#!/usr/bin/env python

import shelve
import os

shelffile = shelve.open('data.dat')
cats = ['brown', "micky", "pooka", "orange",]
shelffile['cats'] = cats

print(shelffile.values())
shelffile.close()