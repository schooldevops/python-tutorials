# from datetime import datetime, timedelta
from calendar import month
import inspect
import datetime
from datetime import datetime as dt  

# 패키지 위치 찾기. 
print(inspect.getfile(datetime))
print(inspect.getfile(dt))

# /usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py
# /usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py


print(datetime)
print(dt) 

print(datetime.datetime)
print(dt)

print(datetime.datetime.now())
print(dt.now())

# ------------------------------------------

datetime01 = datetime.datetime 
datetime02 = dt 

print(datetime01.now())
print(datetime02.now())

print(datetime01.now().strftime("%Y-%m-%d"))
print(datetime02.now().strftime("%Y-%m-%d"))

d_time = dt(2022, 1, 1, 10, 30, 30)
print(d_time)

d_time = dt.now()
print(d_time)

d_time1 = dt(2022, 1, 1, 13, 30, 30)
d_time2 = dt.now() 

print('subsctract ------ ')
print(d_time2 - d_time1)

print(type(d_time2 - d_time1))
print((d_time2 - d_time1).days)
print((d_time2 - d_time1).seconds)
print((d_time2 - d_time1).microseconds)

from datetime import timedelta
print('한달전: ', (d_time2 + timedelta(days = -30)))
print('한달후: ', (d_time2 + timedelta(days = 30)))
print('10일전: ', (d_time2 + timedelta(days = -10)))
print('10일후: ', (d_time2 + timedelta(days = 10)))
print('10시간전: ', (d_time2 + timedelta(hours = -10)))
print('10시간후: ', (d_time2 + timedelta(hours = 10)))
print('10분전: ', (d_time2 + timedelta(minutes = -10)))
print('10분후: ', (d_time2 + timedelta(minutes = 10)))
print('10초전: ', (d_time2 + timedelta(seconds = -10)))
print('10초후: ', (d_time2 + timedelta(seconds = 10)))

print('formatting date')
print('2022-01-01  ', d_time1.strftime('%Y-%m-%d'))
print('2022-01-01 13:30:30 ', d_time1.strftime('%Y-%m-%d %H:%M:%S'))
print('2022-01-01 01:30:30', d_time1.strftime('%Y-%m-%d %I:%M:%S'))