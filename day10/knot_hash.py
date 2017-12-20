""" this is a code for Advent of Code 2017 Day9 """


def get_input():
    data = input()
    return [i for i in data]


def reverse_and_move_current(input_num, current_position, input_list, skip_size):
    pass


def reverse_list(input_num, c_position, input_list):
    result = [i for i in input_list]
    for i in range(input_num):
        if i + c_position + 1 > len(input_list) - 1:
            c_position -= len(input_list)
        result[i + c_position + 1] = input_list[c_position + input_num - i]

    return result


if __name__ == '__main__':
    # order_list = get_input()
    l = [i for i in range(10)]

    l2 = reverse_list(3, 0, l)
    print(l2)
