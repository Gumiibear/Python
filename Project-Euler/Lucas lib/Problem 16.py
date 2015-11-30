__author__ = 'lucas.glimfjord'


def power_digit_sum(number, power):
    output = 0
    for value in str(number ** power):
        output += int(value)

    return output

print power_digit_sum(number=2, power=1000)

