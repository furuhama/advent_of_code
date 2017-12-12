""" this is a code for Advent of Code 2017 Day7 """

#
# Part 1
#


def read_input(file):
    """
    reading input raw file and return program as a list
    """
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()
    data = [x.split(' ') for x in data]

    return data


if __name__ == '__main__':
    print(read_input('test_input'))
