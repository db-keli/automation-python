#! /usr/bin/env python3

import threading
import time

print('Start of program')


def takeanap():
    time.sleep(1)
    print('Wake Up!')


threadObj = threading.Thread(target=takeanap)
threadObj.start()

print('End of program')

threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': '%'})
threadObj2.start()
