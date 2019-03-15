"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

What is Median
--------------
"if we cut the sorted array to two halves of EQUAL LENGTHS, then
median is the AVERAGE OF Max(lower_half) and Min(upper_half), i.e. the
two numbers immediately next to the cut".

Algorithm
---------
The idea here is to find i1 and i2 in nums1 and nums2 such that 
-  number left to i1 is less than number right to i2, and 
-  number left to i2 is less than number right to i2
Thus we have found the center point of the combined array splitted in 
two parts. Now we get the max of left side and min of right side. 

"""
import sys

class P004_MedianOfTwoSortedArrays(object):
    
    def findMedianSortedArrays_bf(self, nums1, nums2):
        """
        Brute force solution
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = sorted(nums1 + nums2)
        mid = len(a) // 2
        med = (a[mid] + a[~mid]) / 2.0
        return med

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        INT_MIN_VALUE = -sys.maxsize-1
        INT_MAX_VALUE = sys.maxint
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = len1
        while (low <= high):
            part1 = int((low + high)/2)
            part2 = int((len1 + len2 + 1)/2 - part1)

            # if part1 is 0 it means nothing is there on left side. Use -INF for maxLeft1
            # if part1 is length of input then there is nothing on right side. Use +INF for minRight1
            maxLeft1 = INT_MIN_VALUE if part1 == 0 else nums1[part1 - 1]
            minRight1 = INT_MAX_VALUE if part1 == len1 else nums1[part1]

            maxLeft2 = INT_MIN_VALUE if part2 == 0 else nums2[part2 -1]
            minRight2 = INT_MAX_VALUE if part2 == len2 else nums2[part2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median 
                # in case of even length combined array size
                # or get max of left for odd length combined array size.
                if (len1 + len2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2))/2.0
                else:
                    return max(maxLeft1, maxLeft2)

            # if we are too far on right side for partitionX. Go on left side.
            elif maxLeft1 > minRight2:
                high = part1 - 1
            # we are too far on left side for partitionX. Go on right side.
            else:
                low = part1 + 1

def test_code():
    obj = P004_MedianOfTwoSortedArrays()
    assert obj.findMedianSortedArrays_bf([1, 3], [2]) == 2
    assert obj.findMedianSortedArrays_bf([1, 2], [3, 4]) == 2.5
    assert obj.findMedianSortedArrays([1, 3], [2]) == 2
    assert obj.findMedianSortedArrays([1, 2], [3, 4])
    print "Tests Passed!"

test_code()