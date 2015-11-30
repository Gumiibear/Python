prime_cache = [2]
def sum_prime(max):
    sum = 0
    curr = 3
    while max >= len(prime_cache):
        if not any(curr%prime == 0 for prime in prime_cache) and curr not in prime_cache:
            prime_cache.append(curr)
            sum += curr
        curr +=2
    return sum

print sum_prime(max=2000000)