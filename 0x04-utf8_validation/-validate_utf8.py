#!/usr/bin/python3
"""
UTF 8 can be from 1 to 4 bytes long , subjected to the following rules:
For a 1 byte character, the first bit is 0,followed by its Unicode code
for an n byte character the first n bits are all one's, the n + 1 bit is 0,
followed by n + 1 bytes with the most significant 2 bits being 10
"""


# [197, 130, 1]
# 197 = 11000110
# 130 = 10000010
# 1 = 0000001

from typing import List


def validUTF8(data: List[int]) -> bool:
    """A function that checks if a set of numbers are all valid UTF 8 values"""
    def check(num):
        """A nested function to check a UTF 8 number"""
        mask = 1 << (8 - 1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1

        return i
    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True
