"""
    Tag: dp

    There is a fence with n posts, each post can be painted with one of the k colors.
    You have to paint all the posts such that no more than two adjacent fence posts
    have the same color.
    
    Return the total number of ways you can paint the fence.
    
    Note: n and k are non-negative integers.
    
    Example: Input: n = 3, k = 2,  Output: 6
    Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
                post1  post2  post3      
     -----      -----  -----  -----       
       1         c1     c1     c2 
       2         c1     c2     c1 
       3         c1     c2     c2 
       4         c2     c1     c1  
       5         c2     c1     c2
       6         c2     c2     c1
"""

def numWays(p, c):
    """
    p=1: c ways to paint
    p=2: c (when both are same painted) + c * c-1 (when different painted) ways to paint
    so we can take two choices. paint with same color or different color. 
    for any post looking at back posts:
    same = diff*1 = diff 
    diff = same*(c-1) + dif*(c-1)
    """
    if p == 0: return 0
    if p == 1: return c
    
    same, dif = c, c*(c-1)
    for i in range(3, p+1):
        same, dif = dif, (same+dif)*(c-1)
    return same + dif

def test_code():
    assert numWays(3, 2) == 6
    print "Tests Passed!!"

test_code()
