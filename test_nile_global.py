#print (a,3)(b,1)(d,4)(c,2)

st = "aaabccdddd"

for i in set(st):
    print('({},{})'.format(i, st.count(i)))

#================================

import random

numberList = [111,222,333,444,555]
l = len(numberList)
while True:
    if l:
        ran = random.choice(numberList[0:l])
        p = numberList.pop(numberList.index(ran))
        print(p)
        numberList.append(p)
        l -= 1
    else:
        break

#=========================================    
input="My name@#$ is123 Mayur.."
#output="yM eman@#$ 321si ruyaM.."

mylist = input.split()
str1 = ''
for i in mylist:
    a = s = ''
    for j in i:
        if j.isalnum():
            a = a + str(j)
        else:
            s = s + str(j)
    str1 += a[::-1] + s + ' '
print(str1)
