#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    list_cp = my_list.copy()
    list_cp.sort()
    return list_cp[-1]
