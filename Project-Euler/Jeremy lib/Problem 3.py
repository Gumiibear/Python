def largest_prime(number):
    divide = 2
    while divide * divide < number:
        if number % divide == 0:
            number /= divide
        divide += 1
    return number

print (largest_prime(number=600851475143))
