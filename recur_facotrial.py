
def findFactorial(n):
    if n == 1:
	return n
    else:
	return n * findFactorial(n-1)

num = 5
num = int(input("Enter number to find factorial: "))
if num == 0:
    print("The factorial for zero is 1")
elif num < 0:
    print("Factorial can not be generated for negative values")
else:
    print("The factorial for {} is {}".format(num, findFactorial(num)))
