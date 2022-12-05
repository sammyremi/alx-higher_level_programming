#!/usr/bin/python3

def max_integer(my_list=[]):
    lent = len(my_list)
    if lent == 0:
        return None
    else:
        hig = my_list[0]
        for x in my_list:
            if x > hig:
                hig = x
    return hig
