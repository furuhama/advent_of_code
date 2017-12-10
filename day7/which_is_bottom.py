""" this is a code for Advent of Code 2017 Day7 """

#
# Part 1
#

"""
every node, except root node, has their parent node
so, check every node whether it has parent or not
"""


def raw_input_to_list(file):
    """
    format of each line is
    'boko (num) -> hoge, fuga, piyo'
    """
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()

    node_lists = []

    for i in data:
        one_line = []
        # the line below returns list like ['boko', "**) -> 'hoge', 'fuga', 'piyo'"] (2 elements)
        temp = i.split(' (')
        one_line.append(temp[0])

        if '->' in temp[1]:
            # the line below returns list like ['**', "'hoge', 'fuga', 'piyo'"] (2 elements)
            temp = temp[1].split(') -> ')
            # the line below returns list like ['hoge', 'fuga', 'piyo'] (some elements)
            temp = temp[1].split(', ')

            for e in temp:
                one_line.append(e)

        node_lists.append(one_line)

    return node_lists


def search_parent_nodes(node_list):
    """
    root node is definitely in first place of the node
    so, this search every first node of input list

    1. separate every nodes to first-node group and others

    2. search every first-node group's node
       if its name is not in others group, it is root node
    """
    first_node = []
    others = []

    for e in node_list:
        first_node.append(e[0])
        e.pop(0)

        if len(e) > 0:
            for i in range(len(e)):
                if not e[i] in others:
                    others.append(e[i])

    print('first node: {}'.format(len(first_node)))
    print('others: {}'.format(len(others)))

    for e in first_node:
        if not e in others:
            print('the answer is...\n{}'.format(e))


# if __name__ == '__main__':
#     node_list = raw_input_to_list('input')

#     search_parent_nodes(node_list)

#
# Part 2
#


def shape_raw_input_to_list(file):
    """
    format of each line is
    'boko (num) -> hoge, fuga, piyo'
    """
    f = open(file)
    data = f.read()
    f.close()

    data = data.splitlines()

    node_lists = []

    for i in data:
        node_and_weight = []
        one_line = []

        # the line below returns list like ['boko', "**) -> 'hoge', 'fuga', 'piyo'"] (2 elements)
        temp = i.split(' (')
        node_and_weight.append(temp[0])

        # the line below returns list like ['**', " -> 'hoge', 'fuga', 'piyo'"] (2 elements)
        temp = temp[1].split(')')
        node_and_weight.append(temp[0])

        one_line.append(node_and_weight)

        if '->' in temp[1]:
            # the line below returns list like [' ', "'hoge', 'fuga', 'piyo'"] (2 elements)
            temp = temp[1].split('-> ')
            # the line below returns list like ['hoge', 'fuga', 'piyo'] (some elements)
            temp = temp[1].split(', ')

            for e in temp:
                one_line.append(e)

        node_lists.append(one_line)

    return node_lists


def check_weight(branch):
    """
    check branch list & detect wrong wight branch
    """
    return True


if __name__ == '__main__':
    node_list = shape_raw_input_to_list('test_input')

    print(node_list)
