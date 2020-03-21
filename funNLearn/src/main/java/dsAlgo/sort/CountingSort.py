"""
    Tag: sort
"""
from typing import List


class Solution:
    def counting_sort(self, arr: List[int]) -> List[int]:
        """
            Sorting technique to use when we know the range of the keys
        """
        output = [0 for i in range(len(arr))]
        count = [0 for i in range(256)]

        for i in arr:
            count[ord(i)] += 1

        for i in range(256):
            count[i] += count[i - 1]

        for i in range(len(arr)):
            output[count[ord(arr[i])] - 1] = arr[i]
            count[ord(arr[i])] -= 1

        return output


assert Solution().counting_sort("vishalmittal") == [
    "a", "a", "h", "i", "i", "l", "l", "m", "s", "t", "t", "v"
]
print("Tests Passed!")
