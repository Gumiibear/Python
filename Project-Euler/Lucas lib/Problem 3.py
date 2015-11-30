def highest_factorial(num):
    counter = 2
    while counter < num ** 0.5:
        while num % counter == 0:
            num = num / counter
        counter += 1
    return num

print highest_factorial(num=600851475143)