"""
    Tag: dp, array, sliding window

    Given an array A of 0s and 1s, we may change up to K 
    values from 0 to 1.
    Return the length of the longest (contiguous) subarray 
    that contains only 1s. 

    Example 1: Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2; Output: 6
    Explanation: [1,1,1,0,0,_1,_1,_1,_1,_1,_1]
    Bolded numbers were flipped from 0 to 1.  
    The longest subarray is underlined.

    Example 2: Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
    Explanation: [0,0,_1,_1,_1,_1,_1,_1,_1,_1,_1,_1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  
    The longest subarray is underlined.

    Note:
    -  1 <= A.length <= 20000
    -  0 <= K <= A.length
    -  A[i] is 0 or 1 
"""
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips
            # and window has more than allowed zeros, thus increment left
            # pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1

        return right - left + 1


assert Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
assert (
    Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    == 10
)
print("Tests Passed!!")
