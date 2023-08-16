#!/usr/bin/python3

def square_matrix_simple(matrix=[])
    result = []
    for items in matrix:
        new_list = []
        for x in items:
            ans = x * x
            new_list.append(ans)
        result.append(new_list)
    print(result)
    print(matrix)
