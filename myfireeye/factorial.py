
def factorial(n):
    if n <= 1:
        return 1
    else:
        n1 = factorial(n-1)
        n2 = factorial(n-2)
        return n1 + n2


for i in range(10):
    print(factorial(i))