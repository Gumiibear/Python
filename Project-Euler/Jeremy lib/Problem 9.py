def pythagorean_triplet(sum):
    for c in range(1, sum/2):
        for b in range(1, sum/2):
            if c > b:
                a = sum -(b+c)
                if a**2 + b**2 == c**2 and a+b+c == sum:
                    return a*b*c
            else:
                break
print pythagorean_triplet(1000)
