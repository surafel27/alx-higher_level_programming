#!/usr/bin/python3
"""
   matrix_divided:
      checks for matrix list of int or float
      Return if the matrix list and div is float orn int
"""


def matrix_divided(matrix, div):
    """
    check the matrix for int or float
    and the size of the list must be equal
    """
    result_mx = []
    message1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(message1)
            else:
                inner_list.append(round(j / div, 2))
        result_mx.append(inner_list)
    return result_mx
