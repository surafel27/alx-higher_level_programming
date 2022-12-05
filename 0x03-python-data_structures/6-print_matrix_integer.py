#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for y in row:
            if y is not row[len(row) - 1]:
                print("{:d}".format(y), end=" ")
            else:
                print("{:d}".format(y), end="")
        print()
