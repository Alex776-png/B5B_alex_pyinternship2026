# 6. Recursive function to calculate sum from 1 to n

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


print(recursive_sum(10))