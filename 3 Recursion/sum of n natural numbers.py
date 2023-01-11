# 10 + 9+8+7+.....
# sum_up_to_n = n + sum_up_to_(n-1)

def sum_of_numbers(n):
    if n==1:
        return 1
    return n + sum_of_numbers(n-1)

print(sum_of_numbers(10))