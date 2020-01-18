import time
import datetime
start = time.time()
print(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'))

time.sleep(5)  # or do something more productive

done = time.time()
print(datetime.datetime.fromtimestamp(done).strftime('%Y-%m-%d %H:%M:%S'))

elapsed = done - start

print(elapsed)
print(datetime.datetime.fromtimestamp(elapsed).strftime('%Y-%m-%d %H:%M:%S'))




