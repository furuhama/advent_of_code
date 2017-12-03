""" this is a code for Advent of Code 2017 Day2 """

import sys


def shape_raw_text(filename):
    """
    get raw text spread sheet
    convert it to integer list
    """
    f = open(filename)
    data = f.read()
    f.close()

    data = data.splitlines()
    for i in range(len(data)):
        data[i] = data[i].split('\t')

    # convert every element to integer
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    return data


def check_difference_min_to_max(l):
    return max(l) - min(l)


def check_divisible_nums(l):
    result = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                next
            if l[j] % l[i] == 0 and l[j] // l[i] > result:
                result = l[j] // l[i]
    return result


if __name__ == '__main__':
    argv = sys.argv
    l = shape_raw_text(argv[1])

    my_sum = 0
    for i in l:
        # this line is for Part 1
        # my_sum += check_difference_min_to_max(i)

        # this line is for Part 2
        my_sum += check_divisible_nums(i)

    print(my_sum)
