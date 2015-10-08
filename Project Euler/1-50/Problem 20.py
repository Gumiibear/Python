def sum_factorial(n):
    product = 1
    result = 0
    while n > 1:
        product *= n
        n -= 1
    for number in str(product):
        result += int(number)
    return result

print sum_factorial(100)
