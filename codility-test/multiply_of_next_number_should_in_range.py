print "Hello World!\n"
# def solution(A, B):
#     # write your code in Python 3.6
#     count = 0 
#     if A <= B:
#         for i in range(2,B):
#             res = i*(i+1)
#             if A <= res <=B:
#                 count += 1
#     return count

def solution(A, B):
    # write your code in Python 3.6
    if A <= B:
        return len([1 for i in range(2,B) if A <= i*(i+1) <= B])

print(solution(6,20))
print(solution(21,29))

s = "123456789"
print(s[-1])
