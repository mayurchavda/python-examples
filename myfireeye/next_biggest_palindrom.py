def reverse(num):
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return rev
#print reverse(105)

n = int(input("Enter any number: "))

def palindrom(n):
    temp = n
    while True:
        if temp == reverse(n):
            print ("It's a Palindrom")
        else:
            print ("Not a Palindrom")

palindrom(n)
