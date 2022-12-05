#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_llist = list(my_list)
    if idx < 0:
        return (new_llist)
    elif idx > len(my_list) - 1:
        return (new_llist)
    else:
        new_llist[idx] = element
        return (new_llist)
