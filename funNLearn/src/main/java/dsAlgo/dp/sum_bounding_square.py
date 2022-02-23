"""
    Tag: dp

    Given a 2D array as input, calculate an output array where each element is the sum of the bounding square from [0,0] in the input array.

    For example, given 
           1  2  6
           3  5  2
           7  1  4
            
    it should print
           1   3  9
           4  11 19
           11 19 31
    
    The algorithm should run in O(mn) complexity preferably

    DP key here is: (i-1),j + i,(j-1) - (i-1),(j-1)
    
"""

def sum_bounding_sq(TDA):
    if not TDA:
        return TDA

    nr, nc = len(TDA), len(TDA[0])
    out_tda = [[0 for _i in range(nc)] for _i in range(nr)]
    
    def get_top(i, j):
        return out_tda[i-1][j] if i-1 >= 0 else 0
        
    def get_left(i, j):
        return out_tda[i][j-1] if j-1 >= 0 else 0
        
    def get_diagonal(i, j):
        return out_tda[i-1][j-1] if (i-1 >= 0 and j-1 >= 0) else 0
  
    for i in range(nr):
        for j in range(nc):
            out_tda[i][j] = TDA[i][j] + get_top(i,j) + get_left(i,j) - get_diagonal(i, j)
    
    return(out_tda)
   

assert(sum_bounding_sq([[1, 2, 6], [3, 5, 2], [7, 1, 4]]) == [[1, 3, 9], [4, 11, 19], [11, 19, 31]])
print('Tests Passed!')
