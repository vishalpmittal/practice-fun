"""
    Tag: sort, binary search, algo

    Given an array of integers nums sorted in ascending order, find 
    the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
"""

"""
    The overall algorithm works fairly similarly to the linear scan approach, 
    except for the subroutine used to find the left and rightmost indices 
    themselves. Here, we use a modified binary search to search a sorted array, 
    with a few minor adjustments. First, because we are locating the leftmost 
    (or rightmost) index containing target (rather than returning true iff we 
    find target), the algorithm does not terminate as soon as we find a match. 
    Instead, we continue to search until lo == hi and they contain some index at 
    which target can be found.

    The other change is the introduction of the left parameter, which is a 
    boolean indicating what to do in the event that target == nums[mid]; if left 
    is true, then we "recurse" on the left subarray on ties. Otherwise, we go 
    right. To see why this is correct, consider the situation where we find target 
    at index i. The leftmost target cannot occur at any index greater than i, so 
    we never need to consider the right subarray. The same argument applies to 
    the rightmost index
"""

class Solution(object):
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

def test_code():
    obj = Solution()
    assert obj.searchRange([5,7,7,8,8,10], 8) == [3, 4]
    assert obj.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
    print "tests passed!!"

test_code()
