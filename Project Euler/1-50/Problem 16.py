def sum_power(power):
    result = 0
    for number in str(2 ** power):
        result += int(number)
    return result

print sum_power(power=1000)
