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

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?