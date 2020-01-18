def sort(arr=[12,4,5,6,7,3,1,15]):
    left = []
    pivot = []
    right = []


    if len(arr) > 1:
        piv = arr[0]
        for x in arr:
            if x < pivot:
                left.append(x)
            if x == pivot:
                pivot.append(x)
            if x > pivot:
                right.append(x)

        return sort(left) + pivot + sort(right)
    else:
        return arr

sort()