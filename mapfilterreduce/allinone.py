def square(x):
    return x*x
    
out = map(square, range(1,6))
print(out)

out = map(lambda x: x*x, range(1,6))
print(out)

def isPrime(num):
    tmp = True
    if num > 2:
        for i in range(2, num):
            if num%i == 0:
                tmp = False
        return tmp
    
out = filter(isPrime, range(100))
print(out)


nums = range(3, 100)
for i in range(2,8):
    nums = filter(lambda x: x == i or x % i, nums)
print nums

import functools

def mult(x,y):
    print("X: {}, Y: {}".format(x,y))
    return x*y

aa = functools.reduce(mult, range(1,5+1))
print(aa)
