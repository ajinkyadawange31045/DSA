# next permutation
# arr -> 1 to n
# 1 2 3
# 1 3 2
def nextPermutation(arr,n):
    a = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            a = i
            break
    
    if a == -1:
        arr.reverse()
        print(arr)
    # print(a)
    for i in range(n-1, a,-1):
        if arr[i] > arr[a]:
            arr[a],arr[i] = arr[i],arr[a]
            break
    
    b = []
    for i in range(n-1,a,-1):
        b.append(arr[i])
        arr.pop()
    
    for i in range(len(b)):
        arr.append(b[i])
    print(arr)
    # x = a
    # y = n-1
        
    
    
    return arr

# 3 1 7 5 4 1 0
# 3 4 7 5 1 1 0
# 3 4 0 1 1 5 7

# arr = [1,2,3]
# arr = [3,1,7,5,4,1,0]
arr = [1,1,5]
n = len(arr)
nextPermutation(arr,n)




















        


