def palindrome():
    palyn = 0
    for term1 in range(999, 100, -1):
        for term2 in range(999, 100, -1):
            product = term1 * term2

            if str(product) == str(product)[::-1] and palyn < product:
                palyn = product
    return palyn

print palindrome()
