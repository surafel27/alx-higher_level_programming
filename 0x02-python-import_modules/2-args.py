#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    if j == 0:
        print("{:d} arguments.".format(j))
    elif j >= 1:
        print("{:d} arguments:".format(j))
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, arg))
