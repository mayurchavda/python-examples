a = "abcdefghijklmnopqrst"
print(a[-1])

# def solution(N, K):
#     if N == 0:
#         return [""]
#     result = []
#     for p in solution(N - 1, K - 1):
#         for l in "abc":
#             if p[-1:] != l:
#                 result += [p + l]
#     return result[:K]

def solution(N, K):
    if N == 0:
        return [""]
    result = []
    for p in solution(N - 1, K):
        for l in "abc":
            if p[-1:] != l:
                result += [p + l]
    return result[:K]

# for i in range(15):
#     print(solution(i, 50))
#     print(str(i)+" = "+str(len(solution(i, 50))))

print(solution(2, 4))
print(len(solution(2, 4)))
print(solution(3, 20))
print(len(solution(3, 20)))
print(solution(5, 6))
print(len(solution(5, 6)))
print(solution(4, 4))
print(len(solution(4, 4)))
print(solution(20, 6))
print(len(solution(20, 6)))
