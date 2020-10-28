def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += 1
    return square

print(sum_squares(10)) # Should be 285