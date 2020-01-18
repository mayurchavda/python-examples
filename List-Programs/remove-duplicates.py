import random

def remove_duplicate(list1):
    output = []
    seen = set()
    for ele in list1:
        if ele not in seen:
            output.append(ele)
            seen.add(ele)
    return output

list1 = [1,1,1,2,2,3,3,4,5]
list1 = remove_duplicate(list1)

print(random.choice(list1))



