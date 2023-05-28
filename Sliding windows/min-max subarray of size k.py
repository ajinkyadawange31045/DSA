j = 0
i = 0
sum = 0
# arr = [2,5,1,8,9,2,1]
arr = [1,2,3,4,5,6,7,8,9]
k = 3 #size of sliding window
import sys
MIN_INT = -sys.maxsize - 1
mx = MIN_INT
# print(MIN_INT)
while (j < len(arr)):
    sum = sum + arr[j]
    if j-i+1<k:
        j += 1
    elif j-i+1 == k:
        mx = max(mx,sum)
        print(mx,end=" ")
        sum = sum - arr[i]
        i += 1
        j += 1
print("")
print("ans : ",mx)


