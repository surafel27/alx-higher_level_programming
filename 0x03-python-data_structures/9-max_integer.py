#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return (None)
    else:
        temp = my_list[0]
        for i in my_list:
            if i > temp:
                temp = i
        return (temp)
