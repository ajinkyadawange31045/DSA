# a teacher decided to motivate all by giving chocolate for their better grade
# on the 1st day she gave a certain number of chocolates she gave on previous day and she doubled the no of chocolates every day.
# find how manny chocolates she bought? given last day, say N.

# solution ---->
n = 4
# n = 5
s = 1
a = []
for i in range(1,2*n+1,2):
    a.append(s*2)
    s = s*2
# print(s)
# print(a)
k = 0
for i in range(len(a)):
    k = k + a[i]
print(k)


# another logic
N = 5
A = 2
S = 0
for  i in range(N):
    S = S + A
    A = A*2
print(S)  #O(n)


# this is in gp, so we can use formulae, a(1-r^n)//1-r
# ans = 2(1-2**N)//(1-2)
from math import pow
n=5
r=2
a=2

s=int(a*(pow(r,n)-1)//(r-1))

print(s)




# another solution
# Only tried and working in O(N-1)
#code
n = 5

p = 2**n
ans = p
d = p//2
n = n-1
while n != 0:
    ans = ans + d
    d = d//2
    n = n-1
print('ans',ans)
