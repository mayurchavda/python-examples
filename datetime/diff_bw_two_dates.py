from datetime import *
from time import *
d0 = date(2008, 8, 18)
d1 = date(2009, 9, 26)
delta = d1 - d0
print(delta.days)
print(delta.seconds)


print( datetime.now().day)
print( datetime.now().month)
print( datetime.now().year)
print( datetime.now().hour)
print( datetime.now().minute)
print( datetime.now().second)
sleep(5)
d1 = datetime.now()
print(d1.day)
print(d1.month)
print(d1.year)
print(d1.hour)
print(d1.minute)
print(d1.second)