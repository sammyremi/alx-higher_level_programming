#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        nums = -(number % -10)
    else:
        nums = number % 10
    print("{:d}".format(nums), end='')
    return (nums)
