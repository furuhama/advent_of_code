""" this is a code for Advent of Code 2017 Day7 """

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
    """
    if var in dic:
        return dic[var]
    else:
        # update dic as adding '{var: 0}'
        dic[var] = 0
        return dic[var]


def exec_logic_operator(dic, var, operator, integer):
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


if __name__ == '__main__':
    my_dic = {}
    f = read_input('test_input')

    print(my_dic)
