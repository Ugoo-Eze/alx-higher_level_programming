#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_dup = matrix.copy()

    for i in range(len(matrix)):
        matrix_dup[i] = list(map((lambda x: x ** 2), matrix[i]))
    return matrix_dup
