"""
    Tag: array, integer
    
    Given an unsorted integer array, find the smallest missing positive integer.
    Example:
    Input: [1,2,0]    Output: 3
    Input: [3,4,-1,1]  Output: 2
    Input: [7,8,9,11,12]   Output: 1

    Note: Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    @staticmethod
    def firstMissingPositive(nums):
        # traverse through each number n and set it to it's location n-1
        # in the array (nums[n-1]). Skip negative and nums > length of array
        i = 0
        while (i< len(nums)):
            if nums[i] == i+1 or nums[i] <=0 or nums[i] > len(nums):
                i += 1
            elif nums[nums[i]-1] != nums[i]:
                Solution._swap(nums, i, nums[i]-1)
            else:
                i += 1

        # traverse again and find the first mismatch and return
        i=0
        while i<len(nums) and nums[i] == i+1:
            i += 1
        return i+1

    @staticmethod
    def _swap(arr, pos, num):
        temp = arr[pos]
        arr[pos] = arr[num]
        arr[num] = temp

def test_code():
    assert Solution.firstMissingPositive([1,2,0]) == 3
    assert Solution.firstMissingPositive([3,4,-1,1]) == 2
    assert Solution.firstMissingPositive([7,8,9,11,12]) == 1
    print ("Tests Passed!")

test_code()
