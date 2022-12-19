#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    my_len = x
    count = 0
    for y in range(my_len):
        try:
            print(my_list[y], end="")
            count += 1
        except:
            break
    print()
    return count
        
        
     
