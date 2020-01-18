

def fib(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n-1, b, a+b)

for i in range(9):
    print(fib(i))

'''
def fib(n):
    if(n == 0):
        return 0
    elif( n == 1):
        return 1
    else:
        x = fib(n-1)
        y = fib(n-2)
        return x+y

#print(fib(5))
for i in range(5):
    x = fib(i)
    print(x)'''