ASCII_SIZE=256
def getMaxOccuringChar(str):
    count = [0]*ASCII_SIZE
    max = -1
    c = ''
    for i in str:
        count[ord(i)] += 1

    print(count)

    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i

    print("Max: %s"%max)
    print("Char: %s" % c)
    return c

str = "sample string"
print("String: => %s"%str)
print("Max occurring character is {}".format(getMaxOccuringChar(str)))