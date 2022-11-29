#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
num = str(number)
lst = num[-1]

if lst == '0':
    print(f"Last digit of {num} is {lst} and is 0")
else:
    if number > 0:
        if int(lst) > 5:
            print(f"Last digit of {num} is {lst} and is greater than 5")
        elif int(lst) < 6:
            print(f"Last digit of {num} is {lst} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is -{lst} and is less than 6 and not 0")
