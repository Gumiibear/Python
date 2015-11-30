def sum_factorial(num):
    result = 1
    output = 0
    for count in range(1, num+1):
        result *= count
    for value in str(result):
        output += int(value)
    return output

print sum_factorial(num=100)