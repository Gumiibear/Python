prime_cache = [2, 3, 5]


def nth_prime(number):
    curr = 2
    while len(prime_cache)<number:
        if not any(curr%prime == 0 for prime in prime_cache) and curr not in prime_cache:
            prime_cache.append(curr)
        curr += 1
    return prime_cache[number-1]
print nth_prime(number=10001)
