
def pythagorean_triplet_sum(sum):
    for c in range(sum):
        for b in range(sum):
            if c > b:
                for a in range(sum-b):
                    if b > a and a**2 + b**2 == c**2 and a + b +c == sum:
                        return a * b * c

print pythagorean_triplet_sum(1000)

