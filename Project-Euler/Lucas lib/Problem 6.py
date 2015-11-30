__author__ = 'lucas.glimfjord'

def sum_square_diff(max=100):
    sum_of_square = 0
    for value in range(max+1):
        sum_of_square += value ** 2

    square_of_sum = 0
    for value in range(max+1):
        square_of_sum += value

    square_of_sum **= 2

    return square_of_sum-sum_of_square

print sum_square_diff()


