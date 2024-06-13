#!/usr/bin/python3
"""Contains function that rotates 2d matrix"""


def rotate_2d_matrix(matrix):
    """Function to rotate 2d matrix"""
    arr1 = list(zip(*matrix))
    return [list(single[::-1]) for single in arr1]
