from sys import maxsize

def createStack( ):
    stack = []
    return stack

def push(stack, value):
    stack.append(value)
    print("%s added to stack"% value)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()

def isEmpty(stack):
    return len(stack) == 0

st = createStack()
push(st,10)
print(pop(st))
print(pop(st))
print(pop(st))
print(st)