# 1. Replace set1 char with set2 char in a given string.    
set1 = ['A','B','C','D']
set2 = ['M','N','O','P']

str1 = 'ABCADCDBA'
for i, item in enumerate(set1):
    str1 = str1.replace(set1[i], set2[i])
print(str1)
#MNOMPOPNM

# 2. Indexing and slicing
str1 = 'ABCADCDBA'
print(str1[-5:])
print(str1[:-5])
# DCDBA
# ABCA

# 3. Count the occurance with print as string.
str1 = "aaabccdeee"
str3 = [i for i in str1]
from collections import Counter
mydict = Counter(str3)
print(mydict)
str5 = ""
for i, j in mydict.items():
    if j > 1:
        str5 += str(j) + i
    else:
        str5 += i
print(str5)
# 3ab2cd3e

# 3 with another solution
mdict = {}
str4 = set(str1)
str5 = ""
for i in str4:
    len1 = str1.count(i)
    if len1 > 1:
        str5 = str5 + str(len1) + i
    else:
        str5 = str5 + i
print(str5)
# 3a3e2cbd

# 4. zero division error

def zerodiverr(x, y):
    try:
        x//y
    except ZeroDivisionError as e:
        print(e)
        
zerodiverr(2,0)
