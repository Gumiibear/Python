def fibonacci():
    sum = 0
    last = 1
    new = 2
    while new < 4*10**6:
        if new % 2 == 0:
            sum += new
        temp = last
        last = new
        new = temp + new
    return sum

print (fibonacci())