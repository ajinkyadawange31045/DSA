# It is the function which calls itself
# it also need a base case to stop that function

# if we don't give base case then that ends up in infinte loop
# eg
# def hacked():
#     print("Hare Krishna")
#     hacked()
# hacked()


# so we need to terminate that, we uses base cases
def hacked(i):
    if i==6:
        return#this basically gets us out of function
    print("Hare Krishna",i)
    hacked(i+1)
hacked(1)


# recursions are slow and also takes stack memory
def call_me(n):
    if n==5:
        return
    call_me(n+1)
    print(n)#it is like a stack, which will get on adding as we go ahead.

# It is easy to visualize problems of recursion if we make a recursive tree
    
call_me(1)