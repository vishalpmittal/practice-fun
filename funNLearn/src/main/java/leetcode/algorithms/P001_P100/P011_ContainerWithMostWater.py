"""
    Tag: array

    Given n non-negative integers a1, a2, ..., an , where each 
    represents a point at coordinate (i, ai). n vertical lines are 
    drawn such that the two endpoints of line i is at (i, ai) 
    and (i, 0). Find two lines, which together with x-axis forms a 
    container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]
    In this case, the max area of water (blue section) the container 
    can contain is 49.

    Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

class P011_ContainerWithMostWater(object):
    def maxArea(self, height):
        """
        set two pointers initialized at both ends of the array. 
        Every time move the smaller value pointer to inner array. 
        Then after the two pointers meet, all possible max cases have been 
        scanned and the max situation is 100% reached somewhere in the scan
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))

            if (height[left] < height[right]):
                left+1
            else:
                right-1

        return max_area

def test_code():
    obj = P011_ContainerWithMostWater()
    obj.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    print ("Tests Passed!")

test_code()