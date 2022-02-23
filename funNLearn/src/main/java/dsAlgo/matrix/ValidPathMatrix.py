"""
    Tag: matrix, recursion

    Problem:  Given a 2-d rectangular array of 1's and 0's, write a routine that will return true if 
    there is a valid path through the maze of 0's going from the top left to the bottom right, moving
    only right or down.

    Examples: 
    0 1 0
    0 0 1
    1 0 0       
    Answer: True     
 
    0 0 1 1 
    1 0 0 0
    0 0 1 0
    Answer: True 
  
    0 1 0 0 0
    0 0 0 1 0     
    Answer: False
    
    This is true only if we allow going left and up as well.
    0 0 0 0 1 0 0 0 0 0 0 
    1 1 1 0 1 0 0 1 0 0 0 
    0 0 0 0 1 0 0 1 0 0 0 
    0 1 1 1 1 0 0 1 0 0 0 
    0 0 0 0 0 0 0 1 0 0 0 
"""
from typing import List

def is_there_a_path(arr: List[List[int]]) -> bool:
    if not arr:
        return False
    
    nr = len(arr)
    nc = len(arr[0])

    def helper(i, j):
        # print(i, j)
        if i >= nr or j >=nc or arr[i][j] == 1:
            return False
        
        if i == nr-1 and j == nc-1:
            return True

        return helper(i, j+1) or helper(i+1, j)
        
    return helper(0, 0)

def is_there_a_path_all_directions(arr: List[List[int]]) -> bool:
    if not arr:
        return False
    
    nr = len(arr)
    nc = len(arr[0])
    visited = set()
    
    def helper(i, j):
        # print(i, j)
        if i >= nr or i < 0 or j >=nc or j < 0 or arr[i][j] == 1 or (i,j) in visited:
            return False
        
        if i == nr-1 and j == nc-1:
            return True
        
        visited.add((i, j))
        # right, down, up, left
        return helper(i, j+1) or helper(i+1, j) or helper(i-1, j) or helper(i, j-1)
    return helper(0, 0)


assert(is_there_a_path([[0, 0, 1, 1], [1, 0, 0, 0], [0, 0, 1, 0]]))
assert(not is_there_a_path([[0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]))
print('Tests Passed!')
