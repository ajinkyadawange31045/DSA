# given a range of the form [L,R]. The task is to print all the numbers which has difference six in the range
# input L = 1, R=19
# output : (5,11)(7,13)(11,17)(12,19)

from math import sqrt

def generatePrimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    
    for i in range(2,int(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i*i,n+1,i):
                primes[j] = False
    return primes
L =  6
R = 59

myprimenos = generatePrimes(R)
# print(myprimenos)
for i in range(L,len(myprimenos)-6):
    if myprimenos[i] ==True:
        x = i
        y = x+6
        if myprimenos[y] == True:
            print(f'({x},{y})',end=" ")