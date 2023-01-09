#!/usr/bin/python3
"""define a class MyList that inherit List """


class MyList(list):
    """contain list
    """

    def print_sorted(self):
        """Print self in sorted format
        """
        print(sorted(self))
