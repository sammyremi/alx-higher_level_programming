#!/usr/bin/python3

for x in range(10):
    for y in range(10):
        if y != 9 or x !=9 :
            print (x, y, end=", ")
        else:
            print (x, y, end="\n")
