for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for key in {'one':1, 'two':2}.items():
    print(key)
for char in "123":
    print(char)
print(open("myfile.txt"))
print(type(open("myfile.txt")))
for line in open("myfile.txt"):
    print(line)
