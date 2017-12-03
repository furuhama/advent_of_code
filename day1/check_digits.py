""" Advent of Code 2017 Day 1 """


def convert_to_list(input_int):
    """
    convert input integer to list of int
    """
    my_list = list(str(input_int))
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    return my_list


def get_sum_of_same_digits(int_list):
    """
    if list[N] == list[N+1]
    add list[N]
    &&
    if the last element of list equals the first element of the list
    add last element
    """
    my_sum = 0
    for i in range(len(int_list)):
        # check the last element at first
        if i == (len(int_list) - 1):
            if int_list[i] == int_list[0]:
                my_sum += int_list[i]

        # check elements except the last element
        else:
            if int_list[i] == int_list[i + 1]:
                my_sum += int_list[i]

    return my_sum


if __name__ == '__main__':
    n = int(input())
    n = convert_to_list(n)
    print(get_sum_of_same_digits(n))
