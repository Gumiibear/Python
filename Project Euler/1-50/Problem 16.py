def sum_power(power):
    product = 2 ** power
    result = 0
    for number in str(product):
        result += int(number)
    return result

print sum_power(1000)