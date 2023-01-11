# k = 2
def fact(n):
    if n==0:
        return 1
    # if n == 1:
    #     return 1
    # k = k*n
    
    return n*fact(n-1)


print(fact(1))
    
# The thing should be of recursive nature
# n! = n*(n-1)!3 