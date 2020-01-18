#import time
import datetime
from datetime import date
#from dateutil.relativedelta import relativedelta

#print("Time in seconds since the epoch: %s" % time.time()
print("Current date and time:", datetime.datetime.now())
print("Current date and time:", datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))

print("Current Year:", datetime.date.today().strftime("%Y"))
print("Month of year:", datetime.date.today().strftime("%B"))
print("Week number of the year:", datetime.date.today().strftime("%W"))
print("Week day of the Week:", datetime.date.today().strftime("%w"))
print("Day of the year:", datetime.date.today().strftime("%j"))
print("Day of the month:", datetime.date.today().strftime("%d"))
print("Day of the Week:", datetime.date.today().strftime("%A"))


startdate = date(2017,8,2)
todaydate = date.today()

delta = todaydate - startdate 
print(delta.days)

#now = datetime.datetime.now()
#td = datetime.timedelta(days=500)
td = date(1987,5, 8)
now = date.today()
five_hundred_days_ago = now - td
print(five_hundred_days_ago)
#rdelta =  relativedelta(now, five_hundred_days_ago)
'''rdelta =  relativedelta(now, td)
print("age in years - ",rdelta.years)
print("age in months - ",rdelta.months)
print("age in days - ",rdelta.days)
'''