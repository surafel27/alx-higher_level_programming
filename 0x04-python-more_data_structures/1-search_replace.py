#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for item in my_list:
        if item != search:
            return item
        else:
            return replace
