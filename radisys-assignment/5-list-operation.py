my_list = [{'jack': 4098, 'sape': 4139},11,22,"aaa","bbb",{'apple', 'orange', 'apple'},('physics', 'chemistry', 1997, 2000)]
print(my_list)

# Replace any 2 elements with new ones
def replace_element(old,new):
    index = my_list.index(old)
    my_list[index] = new

replace_element(11,66)
replace_element("bbb","Mayur")
print(my_list)

# Search any element of your choice and print the value if found
def search_element(find_item):
    s = [item for item in my_list if item == find_item]
    if s:
        print(s[0])
    else:
        pass
search_element('aaa')
search_element(11)

# Print the sequence one by one and all at once
def one_by_one(my_list):
    for item in my_list:
        print item, " "
one_by_one(my_list)

def all_at_once(my_list):
    print(my_list)
all_at_once(my_list)

def reorder_list(my_list):
    myorder = [6,3, 2, 0, 1, 4, 5,]
    mylist = [my_list[i] for i in myorder]
    print mylist
reorder_list(my_list)

