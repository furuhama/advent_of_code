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


if __name__ == '__main__':
    argv = sys.argv
    l = shape_raw_text(argv[1])

    my_sum = 0
    for i in l:
        my_sum += check_difference_min_to_max(i)

    print(my_sum)
