"""
    Tag: math, array

    Given an array nums of n integers and an integer target, 
    find three integers in nums such that the sum is closest to 
    target. Return the sum of the three integers. You may assume that 
    each input would have exactly one solution.

    Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class P016_3Sum_Closest(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return []

        # sort for skipping duplicates
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for curr in range(len(nums) - 2):
            # start two pointers one from curr's immediate right and 
            # one from last element of array
            l, r = curr+1, len(nums) - 1
            while l < r:
                sum = nums[curr] + nums[l] + nums[r]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(closest_sum - target):
                    closest_sum = sum
                
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
        return closest_sum

def test_code():
    obj = P016_3Sum_Closest()
    assert obj.threeSumClosest([-1, 2, 1, -4], 1) == 2
    print "Tests passed!"

test_code()