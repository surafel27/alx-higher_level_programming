#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp = dict(a_dictionary)
    for key, value in tmp.items():
        tmp[key] = value * 2
    return (tmp)
