#!/usr/bin/python3
N = 26
for i in range(97, 97 + N):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    else:
        print("{}".format(chr(i)), end="")
    i + 1
