from collections import Counter
list1=['apple','egg','apple','banana','egg','apple']
counts = Counter(list1)
print(counts)
#Counter({'apple': 3, 'egg': 2, 'banana': 1})

dict = {}
str = "This is to find number of occurence of each word in a string This is cat ant This is dog"
data_lst = str.split()
data_lst = Counter(data_lst)
print(data_lst)

