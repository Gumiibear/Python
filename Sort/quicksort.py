import random

def qsort(list):
    higher = []
    lower = []
    if len(list) > 1:
        current = list[0]
        for number in list[1:]:
            if number >= current:
                higher.append(number)
            else:
                lower.append(number)
        return qsort(list=lower) + [current] + qsort(list=higher)

    else:
        return list

randomlist = random.sample(xrange(-99, 99),10)
print qsort(list=randomlist)
