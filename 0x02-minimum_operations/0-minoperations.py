#!/usr/bin/python3
"""Function that calculates the minimum number 
of operations needed to print n 'H' in a file"""


def minOperations(n: int) -> int:
    """Calculates the minimum operations to result in n"""
    process = 2
    operations = 0
    while n > 1:

        while n % process == 0:
            operations += process
            n /= process
        process += 1
    return operations
