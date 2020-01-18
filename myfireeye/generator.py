import time
def gen(num):
    n = 0
    while n < num :
        yield n + 1
        n += 1
start1 = time.time()
for i in gen(10000):
    print(i)
end1 = time.time()


start2 = time.time()
for i in range(10000):
    print(i)
end2 = time.time()
print(end1 - start1)
print(end2 - start2)