#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
num = str(number)
last = num[-1]

if last == '0':
    print(f"Last digit of {num} is {last} and is 0")
else:
    if number > 0:
        if int(last) > 5:
            print(f"Last digit of {num} is {last} and is greater than 5")
        elif int(last) < 6:
            print(f"Last digit of {num} is {last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is -{last} and is less than 6 and not 0")
