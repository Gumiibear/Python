__author__ = 'lucas.glimfjord'


def sum(max):
    output = 0
    for num in range(max):
            if num % 3 == 0:
                output += num
            elif num % 5 == 0:
                output += num
    return output

print sum(1000)