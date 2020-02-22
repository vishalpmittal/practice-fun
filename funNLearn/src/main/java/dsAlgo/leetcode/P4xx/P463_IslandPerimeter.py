"""
    Tag: matrix

    You are given a map in form of a two-dimensional integer grid where 1 
    represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
    surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes" (water inside that isn't connected to the water 
    around the island). One cell is a square with side length 1. The grid is rectangular, 
    width and height don't exceed 100. Determine the perimeter of the island.

    Example:

    Input:
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

    Output: 16
"""
from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    '''
    Use dictionary to store the values to get around lot of try excepts. 
    '''
    ilnd = {}
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                s = (i, j)
                ilnd[s] = 1
    for i in ilnd.keys():
        m = ilnd.get((i[0]-1, i[1]), -1)
        if m == -1:
            count += 1
        m = ilnd.get((i[0]+1, i[1]), -1)
        if m == -1:
            count += 1
        m = ilnd.get((i[0], i[1]-1), -1)
        if m == -1:
            count += 1
        m = ilnd.get((i[0], i[1]+1), -1)
        if m == -1:
            count += 1
    return count


def test_code():
    assert islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [
                           0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    print("Tests Passed!!")


test_code()
