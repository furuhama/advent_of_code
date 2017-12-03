""" this is a code for Advent of Code 2017 Day2 """

import sys


def shape_raw_text(filename):
    f = open(filename)
    data = f.read()
    f.close()

    print(data)


if __name__ == '__main__':
    argv = sys.argv
    shape_raw_text(argv[1])
