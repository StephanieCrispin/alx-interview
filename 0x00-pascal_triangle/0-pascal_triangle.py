#!/usr/bin/python3
"""Pascals triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """

    # Instantiate a new empty array for triangle
    pascal_tri = []
    # Check edge case
    if n <= 0:
        return []
    for i in range(n):
        if i == 0:
            # If its the first row make it just one element in the list
            pascal_tri.append([1])
        else:
            current_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    current_row.append(1)
                else:
                    current_row.append(pascal_tri
                                       [i-1][j - 1] + pascal_tri[i - 1][j])

            pascal_tri.append(current_row)
    return pascal_tri
