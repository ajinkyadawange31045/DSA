# # time complexity O(n!)
# result = []
# def permutation(data,i,n):
#     if i==n:
#         result.append("".join(data)) #['a','b','c']
#     for j in range(i,n+1):
#         data[i],data[j] = data[j],data[i]
#         permutation(data, i+1, n)
#         data[i],data[j] = data[j],data[i]#back tracking

# data = "ABC"
# i = 0
# n = len(data)-1
# permutation(list(data), i, n)
# print(result)


# the above soln for interviews

# solution using inbuilt functions
from itertools import permutations
result = list(permutations("ABC"))#time complexity O(1)

# to join them
result1 = ["".join(x) for x in list(permutations("ABC"))]#list comprehension methods, with time complexity O(n)
print(result)
print(result1)

