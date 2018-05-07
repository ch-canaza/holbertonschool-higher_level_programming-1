#!/usr/bin/python3
"""
This is the module 100-matrix_mul.
It contains one function: matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """
    returns the product of matrices m_a and m_b
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if m_a == [] or len(m_a[0]) == 0:
        raise ValueError('m_a can\'t be empty')
    if m_a == [] or len(m_b[0]) == 0:
        raise ValueError('m_b can\'t be empty')
    len_a = len(m_a[0])
    len_b = len(m_b[0])
    if len_a != len_b:
        raise ValueError('m_a and m_b can\'t be multiplied')
    for row in m_a:
        if len(row) != len_a:
            raise TypeError('each row of m_a must should be of the same size')
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        if len(row) != len_b:
            raise TypeError('each row of m_b must should be of the same size')
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError('m_b should contain only integers or floats')
    new_matrix = []
    for a in range(len(m_a)):
        new_row = []
        for b in range(len_b):
            num = 0
            for c in range(len_a):
                num += m_a[a][c] * m_a[c][b]
            new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix
