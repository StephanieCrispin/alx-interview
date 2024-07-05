#!/usr/bin/python3

"""Practice for Island perimeter"""


def island_perimeter(grid):
    ans = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                ans += 4
                if row < rows - 1 and grid[row + 1][col] == 1:
                    ans -= 2
                if col < cols - 1 and grid[row][col + 1] == 1:
                    ans -= 2
    return ans


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(island_perimeter(grid))
