#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastnum = number % -10
        lastnum *= -1
    else:
        lastnum = int(repr(number)[-1])
    print(lastnum, end="")
    return lastnum
