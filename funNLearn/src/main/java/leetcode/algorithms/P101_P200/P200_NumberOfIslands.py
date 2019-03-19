"""
    Tag: dfs, matrix

    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands 
    horizontally or vertically. You may assume all four edges of the grid 
    are all surrounded by water.

    Example 1:
    Input:
    11110
    11010
    11000
    00000

    Output: 1

    Example 2:
    Input:
    11000
    11000
    00100
    00011

    Output: 3
"""

class P200_NumberOfIslands:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

def test_code():
    obj = P200_NumberOfIslands()
    
    island = [[] for _ in range (4)]
    island[0]=['1', '1', '1', '1', '0']
    island[1]=['1', '1', '0', '1', '0']
    island[2]=['1', '1', '0', '0', '0']
    island[3]=['0', '0', '0', '0', '0']
    assert obj.numIslands(island) == 1

    m_island = [[] for _ in range (4)]
    m_island[0]=['1', '1', '0', '0', '0']
    m_island[1]=['1', '1', '0', '0', '0']
    m_island[2]=['0', '0', '1', '0', '0']
    m_island[3]=['0', '0', '0', '1', '1']
    assert obj.numIslands(m_island) == 3

    print "Tests Passed!"

test_code()