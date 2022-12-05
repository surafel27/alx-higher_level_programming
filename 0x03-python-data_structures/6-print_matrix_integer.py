#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    for i in range(x):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j], end=""))
                if j is not (len(matrix[i]) - 1):
                    print(end=" ")
        print()
