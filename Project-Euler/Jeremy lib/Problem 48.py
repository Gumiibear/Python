def self_power(max):
    sum = 0
    number = 1
    while number < max:
        sum += number ** number
        number += 1
    return sum[len(str(sum))-10,len(str(sum))]

print self_power(1000)