""" this is a code for Advent of Code 2017 Day 6 """


def shape_raw_input_to_int_list(file):
    f = open(file)
    data = f.read()
    f.close()

    data = data.split()

    return data


if __name__ == '__main__':
    n = input()
    blocks = shape_raw_input_to_int_list(n)

    print(blocks)
