import functools

a = [1,2,3,4,5]
b = [10,20,30,40,50]

n = [x for x in range(1,101)]

result = map(lambda x,y: x+y, a,b)
print([x for x in result])

result = filter(lambda x: x%3==0 and x%5==0, n)
print([x for x in result])

result = functools.reduce(lambda x,y:x+y, a)
print(result)