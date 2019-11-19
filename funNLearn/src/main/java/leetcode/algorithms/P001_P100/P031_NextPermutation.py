"""
    Tag: algo, array, integer

    Implement next permutation, which rearranges numbers into the 
    lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest 
    possible order (ie, sorted in ascending order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its 
    corresponding outputs are in the right-hand column.

    1,2,3 -> 1,3,2
    3,2,1 -> 1,2,3
    1,1,5 -> 1,5,1
"""

"""
    Nayuki Algorithm
    Next lexicographical permutation algorithm

    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg

    0. Initial sequence          
        0, 1, 2, 5, 3, 3, 0
    1. Find longest non-increasing suffix
        0, 1, 2, 5, 3, 3, 0
                |----------|
    2. Identify pivot 
        0, 1, 2, 5, 3, 3, 0
              ^
    3. Find rightmost successor to pivot in the suffix 
        0, 1, 2, 5, 3, 3, 0
                       ^
    4. Swap with pivot 
        0, 1, 3, 5, 3, 2, 0
              ^        ^
    5. Reverse the suffix 
        0, 1, 3, 0, 2, 3, 5
                |----------|
    6. Done
        0, 1, 3, 0, 2, 3, 5
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        right = len(nums)-1
        while nums[right] <= nums[right-1] and right-1 >=0:
            right -= 1
        
        # this completely increasing order reverse the list
        # this should cover the case 3,2,1 -> 1,2,3
        if right == 0:
            return self.reverse(nums,0,len(nums)-1)

        # find pivot
        pivot = right-1
        successor = 0

        # find rightmost succesor
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break

        # swap pivot and successor
        nums[pivot],nums[successor] = nums[successor],nums[pivot]

        # reverse suffix
        self.reverse(nums,pivot+1,len(nums)-1)

    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1


def test_code():
    obj = Solution()
    num_list = [1, 2, 3]
    obj.nextPermutation(num_list) 
    assert num_list == [1, 3, 2]

    num_list = [3, 2, 1]
    obj.nextPermutation(num_list)
    assert num_list == [1, 2, 3]
    
    num_list = [1, 1, 5]
    obj.nextPermutation(num_list)
    assert num_list == [1, 5, 1]
    
    print ("Tests Passed!")

test_code()
