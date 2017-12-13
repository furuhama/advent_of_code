""" this is a code for Advent of Code 2017 Day8 """

#
# Part 1
#


def read_input(file):
    """
    reading input raw file and return program as a list
    this returns a list like below
    [['b', 'inc', '5', 'if', 'a', '>', '1'], ['a', 'inc', '1', 'if', 'b', '<', '5']]
    """
    f = open(file)
    data = f.read()
    f.close()

    data = [x.split(' ') for x in data.splitlines()]

    return data


def check_variable(var, dic):
    """
    check variables whether it is already exists in my dic or not
    if true, it returns the variable's value
    else, it returns 0
    """
    if not var in dic:
        # update dic as adding '{var: 0}'
        dic[var] = 0


def exec_logic_operator(var, dic, operator, integer):
    """
    read logic operators in each line & exec it
    this allows >, <, >=, <=, ==, !=
    """
    value = dic[var]
    if operator == '>' and value > integer:
        return True
    elif operator == '<' and value < integer:
        return True
    elif operator == '>=' and value >= integer:
        return True
    elif operator == '<=' and value <= integer:
        return True
    elif operator == '==' and value == integer:
        return True
    elif operator == '!=' and value != integer:
        return True
    else:
        return False


def exec_order(var, dic, order, order_value):
    """
    exec order in each line
    this allows 'inc', 'dec'
    """
    if order == 'inc':
        dic[var] += order_value
    elif order == 'dec':
        dic[var] -= order_value
    else:
        print('Error! unexpected order!')


def check_max_value(dic):
    """
    this returns max value in dict object
    (it doesn't consider the time all the variables are negetive number)
    """
    bench = 0
    for k in dic:
        if dic[k] > bench:
            bench = dic[k]
    return bench


def check_highest_value(val, highest):
    if val > highest:
        highest = val
    return highest


if __name__ == '__main__':
    my_dic = {}
    f = read_input('input')
    highest_value = 0

    for e in f:
        check_variable(e[4], my_dic)
        if exec_logic_operator(e[4], my_dic, e[5], int(e[6])):
            check_variable(e[0], my_dic)
            exec_order(e[0], my_dic, e[1], int(e[2]))
            t = e[0]
            highest_value = check_highest_value(my_dic[t], highest_value)

    print(my_dic)

    print(check_max_value(my_dic))

    print(highest_value)
