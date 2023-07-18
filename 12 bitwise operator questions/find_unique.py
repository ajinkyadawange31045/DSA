arr = [2,3,3,4,2,6,4]
def solve(arr):
    a = 0 
    for i in arr:
         a = a^i
    return a




print(solve(arr))