#! /usr/bin/env python3

import datetime

dt = datetime.datetime.now()
print(dt.year, dt.month, dt.day)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('The %dst day of %M'))
