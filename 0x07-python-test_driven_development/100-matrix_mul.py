#!/usr/bin/python3
"""
Module 100-matrix_mul
Define matrix_mul
multipiles two matrixs
"""


def matrix_mul(m_a, m_b):
    """
    returns the multiplication of m_a and m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    L = []
    new = []
    msg_1 = "each row of m_a must be of the same size"
    msg_2 = "each row of m_b must be of the same size"
    msg_3 = "m_a should contain only integers or floats"
    msg_4 = "m_b should contain only integers or floats"
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != len(m_a[0]):
            raise TypeError(msg_1)
        if len(i) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(msg_3)

    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
        if len(i) != len(m_b[0]):
            raise TypeError(msg_2)
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(msg_4)

    _sum = 0
    for row in range(len(m_a)):
        for colom in range(len(m_b[0])):
            for j in range(len(m_a[row])):
                _sum += m_a[row][j] * m_b[j][colom]
            L.append(_sum)
            _sum = 0
        new.append(L.copy())
        L.clear()
    return 
