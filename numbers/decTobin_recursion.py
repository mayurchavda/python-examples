
def convertToBinary(num):
    if num > 1:
	convertToBinary(num//2)
    print (num%2)

dec = 34
convertToBinary(dec)
