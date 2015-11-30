def sum():
    sum = 0
    curr = 1
    while curr < 1000:
        if curr % 3 == 0 or curr % 5 == 0:
            sum += curr
        curr += 1
    return sum

print (sum())
