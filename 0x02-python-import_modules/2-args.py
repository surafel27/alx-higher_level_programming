#!/usr/bin/python3
import sys
if __name__ == "__main__":
    j = len(sys.argv) - 1
    if j == 0:
        print("{} arguments.".format(j))
    elif j >= 1:
        print("{} arguments:".format(j))
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, arg))
