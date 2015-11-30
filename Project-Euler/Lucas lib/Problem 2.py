__author__ = 'lucas.glimfjord'


def sum_even_fibonacci():
    output = 0
    last = 1
    curr = 2
    while curr < 4 * (10 ** 6):
        if curr % 2 == 0:
            output += curr

        temp = curr
        curr = last + temp
        last = temp
    return output

cache = {0: 0, 1: 1}

def fib(n):
    print(cache)
    if n in cache:
        return cache[n]
    else:
        result = fib(n - 1) + fib(n-2)
        cache[n] = result
        return result

print(fib(40))
