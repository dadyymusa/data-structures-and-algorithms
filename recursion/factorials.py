def factorials(n):
    # remove this line if you hate your pc
    if n < 0 or n > 25:  
        return '-1'
    elif n == 1:
        return 1
    return n * factorials(n - 1)

num = 9

print(factorials(num))