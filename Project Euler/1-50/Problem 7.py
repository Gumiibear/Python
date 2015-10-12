prime_cache = []
def nth_prime(n):
    curr = 2
    while n >= len(prime_cache):
        if not any(curr%prime == 0 for prime in prime_cache) and curr not in prime_cache:
            prime_cache.append(curr)
        curr +=1
    return prime_cache[n-1]

print nth_prime(n=10001)
