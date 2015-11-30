__author__ = 'lucas.glimfjord'

prime_cache = [2]


def primes_below(max):
    curr = 2
    prime_sum = 2
    while curr <= max:
        if not any(curr % prime == 0 for prime in prime_cache) and curr not in prime_cache:
            prime_cache.append(curr)
            prime_sum += curr
        curr += 1
    return prime_sum


print primes_below(2 * (10 ** 6))

#Answer is 142913828922