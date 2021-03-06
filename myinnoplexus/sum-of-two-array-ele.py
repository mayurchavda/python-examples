CONST_MAX = 100
# function to check for the given sum in the array
def printPairs(arr, arr_size, sum):
    # initialize hash map as 0
    binmap = [0] * CONST_MAX
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and binmap[temp] == 1):
            print("Pair with the given sum is", arr[i], "and", temp)
        binmap[arr[i]] = 1


# driver program to check the above function
A = [1, 6, 5, 45, 4, 5, 10, -8]
n = 10
printPairs(A, len(A), n)

