import random
import re
input = "Mississippi"
extractstr = "ipsssi"
print("s count: %s"%input.count("s"))
print("i count: %s"%input.count("i"))

def find_combination(word):
    foo = list(word)
    random.shuffle(foo)
    return ''.join(foo)

while True:
    randstr = find_combination(input)
    m= re.search("^ips{3}i$",randstr)
    if m != None:
        aaa = m.group(1)
        if aaa == extractstr:
            print(aaa)
            break
    '''if randstr.startswith(extractstr):
        print(randstr[0:6])
        break'''
