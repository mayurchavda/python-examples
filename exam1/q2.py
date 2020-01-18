arr = [1,7,4,5,6,3,2,9]
arr1 = sorted(arr, reverse=True)
print(arr1)
print(max(arr))

arr.remove(max(arr))
print(max(arr))
