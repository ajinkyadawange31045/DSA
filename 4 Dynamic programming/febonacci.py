# write a functino to return nth term of fibonacci sequence
'''
fibonacci sequence
index -> 0,1,2,3,4,5,6,7,8
fib seq->0,1,1,2,3,5,8,13,21

problem - write function to return nth term of fibonacci sequence

feb(5th) = feb(4) + feb(3)
feb(4) = feb(3) + feb(2)
feb(3) = feb(2) + feb(1)
feb(2) = feb(1) + feb(0)
feb(1) = 1
feb(0) = 0
'''

'''
# O(2^n)
def feb(n):
    if n==1 or n==0:
        return n
    return feb(n-1)+feb(n-2)

print(feb(6))

for i in range(50):
    print(i,feb(i)) #It takes too much time, it is explain in the picture given with that.
    
# we can solve that using dynamic programming
# we use DP, when we get overlapping subproblems
2 methods to solve DP problems
- memoization
- Tabular

'''


'''
# O(n)
a_dict = {}#this should be globally available

# using memoization
def feb1(n):
    # a = {}
    if n in a_dict:#checking if the key is present in the dictionary
        return a_dict[n]#here we are accessing the value of that key
    if n==1 or n==0:
        value = n
    else:
        value = feb1(n-1)+feb1(n-2)
    a_dict[n] = value
    return value

for i in range(100):
    print(i,feb1(i)) 
'''

# to short the above code
'''
# O(n)
a_dict = {
    1:1,
    0:0,
}
#this should be globally available

# using memoization
def feb1(n):
    if n in a_dict:#checking if the key is present in the dictionary
        return a_dict[n]#here we are accessing the value of that key
    value = feb1(n-1)+feb1(n-2)
    a_dict[n] = value
    return value

for i in range(100):
    print(i,feb1(i)) 
'''



# method 2 : tabular method -> it is a iterative method and we can use tables
'''
# O(n)
in 90%  of the cases the answer will be the last number in the list, either 1d or 2d list
[0,0,0,0,ans]

[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,ans],
]
'''

def feb2(n):
    table = [0]*(n+1)
    try:
        table[1] = 1
    except:
        return
    for j in range(2,n+1):
        table[j] = table[j-1] + table[j-2]
    return table

print(feb2(4))
print('ans : ',feb2(4)[4])
        
# for i in range(2,50):
#     print(i,feb2(i)[i]) 