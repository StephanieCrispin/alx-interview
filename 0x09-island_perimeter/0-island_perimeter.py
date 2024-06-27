#!/usr/bin/python3
"""Code with solution to Island Perimeter DSA"""


def island_perimeter(grid):
    """A function that solves the problem Island perimeter"""
    ans = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == 1:
                ans += 4
                if row < rows - 1 and grid[row + 1][column] == 1:
                    ans -= 2
                if column < cols - 1 and grid[row][column + 1] == 1:
                    ans -= 2
    return ans
