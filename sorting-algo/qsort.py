
def partition(arr, low, high):

    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] =arr[j]
            arr[j] = temp
    if arr[high] < arr[i+1]:
        temp = arr[i+1]
        arr[i+1] = arr[high]
        arr[high] = temp
    return (i+1)

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr,pi+1, high)


arr = [10,7,8,9,1,5]
n = len(arr)
quicksort(arr, 0, n-1)
for i in range(n):
    print("%d"%arr[i])

print([x for x in range(0,6)])
