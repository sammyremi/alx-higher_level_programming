#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    my_list = sys.argv
    lent = len(my_list)

    if lent == 1:
        print("{} arguments.".format(lent - 1))

    elif lent == 2:
        print("{} argument:".format(lent - 1))

    else:
        print("{} arguments:".format(lent - 1))
        for x in range(1, lent):
            print("{}: {}".format(x, my_list[x]))
