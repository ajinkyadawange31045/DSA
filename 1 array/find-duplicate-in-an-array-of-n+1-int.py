# duplicate in arr of n+1 intergers
# arr = [2,3,1,4,5,3]
arr = [1,3,4,2,2]
n = len(arr)

# TC = O(n^2)
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             print(arr[i])

# freq = [0]*(n+1)
# for i in range(n):
#     freq[arr[i]] += 1

# for i in range(len(freq)):
#     if freq[i] == 2:
#         print(i)

s = arr[0]
f = arr[0]
while s != f :
    s  = arr[s]
    f = arr[arr[f]]
    
f = arr[0]
while s != f:
    s  = arr[s]
    f  = arr[f]

print(s)
    


    