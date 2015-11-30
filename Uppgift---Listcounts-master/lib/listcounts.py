def sum(list):
    output = 0
    for number in list:
        output += number
    return output

def max(list):
    if len(list) > 0:
        output = list[0]
        for number in list:
            if output < number:
                output = number
    else: output = 0
    return output

def min(list):
    if len(list) > 0:
        output = list[0]
        for number in list:
            if output > number:
                output = number
    else: output = 0
    return output

def average(list):
    return sum(list=list) / float(len(list))


def median1(list):
    output_list = []
    current_list = list
    if len(current_list) > 0:
        while len(current_list) > 0:
            current = current_list[0]
            for number in current_list:
                if number < current:
                    current = number

            output_list.append(current_list[0])
            del current_list[0]
        if len(output_list) % 2 == 0:
            firstmed = output_list[len(output_list)/2]
            secondmed = output_list[(len(output_list)-2)/2]
            output = (firstmed + secondmed)/2.0
        else:
            output = output_list[(len(output_list)-1)/2]
    else:
        output = 0
    return output

def median2(list):
    output_list = []
    current_list = list
    if len(current_list) > 0:
        while len(current_list) > 0:
            minnumb = min(list=current_list)
            del current_list[current_list.index(minnumb)]
            output_list.append(minnumb)
        if len(output_list) % 2 == 0:
            firstmed = output_list[(len(output_list)/2)-1]
            secondmed = output_list[len(output_list)/2]
            output = (firstmed + secondmed)/2.0
        else:
            output = output_list[(len(output_list)-1)/2]
    else:
        output = 0
    return output

print median2(list=[2,4,6,4,4,5])