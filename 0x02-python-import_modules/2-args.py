#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(" 0 arguments.")
    elif len(sys.argv) >= 2:
        print("{} arguments:".format(len(sys.argv)))
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, arg))
