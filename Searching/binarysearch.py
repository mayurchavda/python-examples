

def binarySearch(arr, left, right, find):
    if right >= left:
        mid = int(left + (right - left)/2)
        if arr[mid] == find:
            return mid
        elif(arr[mid] > find):
            return binarySearch(arr, left, mid-1, find)
        else:
            return binarySearch(arr, mid+1, right, find)

    else:
        return -1

arr = [2,3,4,10,40]
x = 10
result=binarySearch(arr,0,len(arr)-1, x)
if result != -1:
    print("Element is present at position %d"%(result+1))
else:
    print("Element is not present in array")
