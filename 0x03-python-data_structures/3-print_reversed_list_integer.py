#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    lent = len(my_list) - 1
    for x in range(len(my_list)):
        print("{}".format(my_list[lent]))
        lent -= 1
