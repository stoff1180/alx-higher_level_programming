#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) < 1:
        return None
    div_list = []
    for i in my_list:
        if (i % 2) == 0:
            div_list.append(True)
        else:
            div_list.append(False)
    return div_list
