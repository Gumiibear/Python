def radixsort(list):
    maxnumber = max(list)
    placement = 1

    while maxnumber >= placement:
        list_of_lists = [[], [], [], [], [], [], [], [], [], []]

        for number in list:
            tmp = abs(number) // placement
            list_of_lists[(tmp % 10)].append(number)
        a = 0
        for b in range(10):
            buck = list_of_lists[b]
            for number in buck:
                list[a] = number
                a += 1
        placement *= 10
    for number in list[1:]:
        if number < 0:
            list.remove(number)
            list = [number] + list
    return list

import random
a = random.sample(xrange(-999, 999),10)
print(radixsort(a))
