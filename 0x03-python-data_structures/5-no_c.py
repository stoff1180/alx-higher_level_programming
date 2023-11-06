#!/usr/bin/python3
def no_c(my_string):
    result = ""
    length = len(my_string)
    for i in range(length):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            result += my_string[i]
    return result
