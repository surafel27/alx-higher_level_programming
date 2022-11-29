#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = int(repr(number)[-1])
if lastnum > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastnum))
elif lastnum == 0:
    print("Last digit of {} is {} and is 0".format(number, lastnum))
elif lastnum < 6:
    print("Last digit of {} is {} and is lessthan than 6 and not 0".format(number, lastnum))

