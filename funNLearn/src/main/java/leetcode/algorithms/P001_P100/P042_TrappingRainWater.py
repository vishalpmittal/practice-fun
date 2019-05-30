"""
    Tag: array, integer

    Given n non-negative integers representing an elevation map where the 
    width of each bar is 1, compute how much water it is able to trap after 
    raining.

    The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
    In this case, 6 units of rain water (blue section) are being trapped. 
    
    Example:
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""


class Solution(object):

    @staticmethod
    def trap(heights):
        """
        
        """
        total = 0
        l, r = 0, len(heights) - 1
        leftmax, rightmax = l, r
        while l < r:
            print 'l: {}, r: {}, leftmax: {}, rightmax: {}, total: {}'.format(
                l, r, leftmax, rightmax, total
            )
            if heights[l] > heights[leftmax]:
                leftmax = l
            if heights[r] > heights[rightmax]:
                rightmax = r
            if heights[leftmax] > heights[rightmax]:
                total += heights[rightmax] - heights[r]
                r -= 1
            else:
                total += heights[leftmax] - heights[l]
                l += 1                
        return total

def test_code():
    print Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])

test_code()
