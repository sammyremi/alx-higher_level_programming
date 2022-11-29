#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
n = str(number)
l = n[-1]

if l == '0':
    print(f"Last digit of {n} is {l} and is 0")
else:
    if number > 0:
        if int(l) > 5:
            print(f"Last digit of {n} is {l} and is greater than 5")
        elif int(l) < 6:
            print(f"Last digit of {n} is {l} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n} is -{l} and is less than 6 and not 0")
