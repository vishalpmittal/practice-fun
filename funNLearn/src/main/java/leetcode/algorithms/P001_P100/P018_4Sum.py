"""
    Tag: array

    Given an array nums of n integers and an integer target, are 
    there elements a, b, c, and d in nums such that a + b + c + d = target? 
    Find all unique quadruplets in the array which gives the sum of target.

    Note: The solution set must not contain duplicate quadruplets.
    Example: Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:  [ [-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2] ]
"""

class Solution(object):

    def fourSum(self, nums, target):
        """
        Calculate 2 sum with O(n^2) and save results
        for each result set find target-set in the results. 
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum2s_list = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 in sum2s_list:
                    sum2s_list[sum2].append((i,j))
                else:
                    sum2s_list[sum2] = [(i,j)]
        
        sum4_set = set()
        for sum2a in sum2s_list:
            sum2b = target - sum2a
            if sum2b in sum2s_list:
                sum2a_list = sum2s_list[sum2a]
                sum2b_list = sum2s_list[sum2b]
                for (i,j) in sum2a_list:
                    for (k,l) in sum2b_list:
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            sum4_set.add(tuple(flist))
        return list(sum4_set)

def test_code():
    obj = Solution()
    print (obj.fourSum([1, 0, -1, 0, -2, 2], 0))

test_code()
