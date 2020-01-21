# Hello World program in Python
    
print ("Hello World!");
def findSubArrays(A,n): 
  
    dictionary = {} 
    out = 0
    total = 0
    for i in range(len(A)): 
        total += A[i] 
        if total == 0: 
            out +=1
        mylist = [] 
        if total in dictionary: 
            mylist = dictionary.get(total) 
            for j in range(len(mylist)): 
                out +=1
                #out.append((mylist[j] + 1, i)) 
        mylist.append(i) 
        dictionary[total] = mylist 
    return out 
  
# Utility function to print 
# all subarrays with sum 0  
def printOutput(output): 
    for i in output: 
        print ("Subarray found from Index " + 
                str(i[0]) + " to " + str(i[1])) 
                
# Driver Code 
if __name__ == '__main__': 
    arr = [2, -2, 3, 4, 0, -7]
    n = len(arr) 
    out = findSubArrays(arr, n) 
    print(out)
      
    # if we did not find any subarray with 0 sum,  
    # then subarray does not exists  
    # if (len(out) == 0): 
    #     print ("No subarray exists") 
    # else: 
    #     printOutput (out)
