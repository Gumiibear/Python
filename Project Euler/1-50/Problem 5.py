def multiple(max):
    result = 1
    divide = 2
    while divide <= max:
        if result % divide != 0:
            for div in xrange(1, divide):
                if divide % div == 0:
                    divide /= div
                    div += 1

            result *= divide


        divide += 1
    return result

print(multiple(max=20))
