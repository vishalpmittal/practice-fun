"""
    Tag: recursive

    Given an array of non-negative integers nums, you are initially positioned at the first 
    index of the array. Each element in the array represents your maximum jump length at 
    that position.
    
    Determine if you are able to reach the last index.
    
    INPUT -> list of integers (non-zero) jumps, [2,3,1,1,4], [3,2,1,0,4], [5]
    OUTPUT -> boolean

    DS1
    [2, 3, 1, 1, 4] -> True

    DS2
    [3, 2, 1, 0, 4] -> False

    DS3
    [5] -> False
"""


def reach_last_index(jumps):
    LI = len(jumps)-1
    visited = set()
    
    def helper(curr_indx):
        # print(curr_indx)
        if curr_indx == LI:
            return True
        
        if curr_indx > LI or jumps[curr_indx] == 0 or curr_indx in visited:
            return False
        
        result = False
        for _x in range(1, jumps[curr_indx]+1):
            result = result or helper(curr_indx + _x)
            if result: 
                break
        
        if not result:
            visited.add(curr_indx)
        
        return result
    return helper(0)


assert(reach_last_index(jumps = [2, 3, 1, 1, 4]))
assert(not reach_last_index(jumps = [3, 2, 1, 0, 4]))
assert(reach_last_index(jumps = [3, 2, 2, 0, 4]))
assert(not reach_last_index(jumps = [3, 2, 0, 0, 4]))
assert(reach_last_index(jumps = [5]))
assert(reach_last_index(jumps = [0]))
print("Tests Passed!")
