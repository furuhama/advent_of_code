""" this is a code for Advent of Code 2017 Day9 """


def get_input():
    """
    this returns input string as separated list
    """
    data = input()
    return [i for i in data]


def read_file(file):
    """
    this reads file and returns its text as separated list
    """
    f = open(file)
    data = f.read()
    f.close()

    return [i for i in data]


def make_flag_list(text):
    """
    this makes a list(which has the same length of input text & all the elements are integer 1)
    [example]
    input: 'abcdefg'
    output: [1, 1, 1, 1, 1, 1, 1]
    ( len(input) == len(output) )
    """
    return [1 for i in range(len(text))]


def remove_after_bang(text, flag_list):
    pass


if __name__ == '__main__':
    a = get_input()
    print(make_flag_list(a))
