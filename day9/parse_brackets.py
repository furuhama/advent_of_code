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


def remove_after_bang(text_list, flag_list):
    flag = True
    for i in range(len(text_list)):
        if flag:
            if text_list[i] == '!':
                flag_list[i] = 0
                flag = False
        else:
            flag_list[i] = 0
            flag = True


def parse_garbages(text_list, flag_list):
    depth_count = 0
    start_point = 0
    for i in range(len(text_list)):
        if i == len(text_list) - 1 and depth_count > 0:
            flag_list[start_point:] = (0,) * (len(text_list) - start_point)
        elif text_list[i] == '<':
            depth_count += 1
            if depth_count == 1:
                start_point = i
        elif text_list[i] == '>':
            depth_count -= 1
            if depth_count == 0:
                flag_list[start_point:(i + 1)] = (0,) * (i - start_point + 1)


# def parse_score(text_list):
#     score = 1
#     sum_score = 0
#     for i in range(len(text_list)):
#         if text_list[i] ==


if __name__ == '__main__':
    a = get_input()
    f_list = make_flag_list(a)

    # remove_after_bang(a, f_list)
    parse_garbages(a, f_list)

    print(a)
    print(f_list)
