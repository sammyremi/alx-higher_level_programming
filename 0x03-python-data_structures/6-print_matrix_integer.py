#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        new = matrix[x]
        for y in range(len(new)):
            if y == len(new) - 1:
                print("{}".format(new[y]))
            else:
                print("{}{}".format(new[y], " "), end="")
