"""
    Tag: math, array

    Given an array nums of n integers, are there elements a, b, c in 
    nums such that a + b + c = 0? Find all unique triplets in the 
    array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.

    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is: [[-1, 0, 1], [-1, -1, 2]]
"""

class P015_3Sum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 2:
            return []

        res = []
        # sort so to skip duplicates
        nums.sort()
        for curr in range(len(nums)-2):
            # Skip for duplicates of curr
            if curr > 0 and nums[curr] == nums[curr-1]:
                continue
            # start two pointers one from curr's immediate right and 
            # one from last element of array
            l, r = curr+1, len(nums)-1
            while l < r:
                s = nums[curr] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[curr], nums[l], nums[r]))
                    # Skip for duplicates of l and r 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

def test_code():
    obj = P015_3Sum()
    obj.threeSum([-1, 0, 1, 2, -1, -4])

test_code()