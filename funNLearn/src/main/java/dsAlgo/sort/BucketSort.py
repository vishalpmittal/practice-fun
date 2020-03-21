"""
    Tag: sort
"""
from typing import List


class Solution:
    def insertionSort(self, B: List[int]) -> List[int]:
        for i in range(1, len(B)):
            up = B[i]
            j = i - 1
            while j >= 0 and B[j] > up:
                B[j + 1] = B[j]
                j -= 1
            B[j + 1] = up
        return B

    def bucket_sort(self, A: List[int]) -> List[int]:
        arr = []
        slot_num = 10  # 10 means 10 slots, each
        # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])

        # Put array elements in different buckets
        for j in A:
            index_b = int(slot_num * j)
            arr[index_b].append(j)

        # Sort individual buckets
        for i in range(slot_num):
            arr[i] = self.insertionSort(arr[i])

        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                A[k] = arr[i][j]
                k += 1
        return A


assert Solution().bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]) == [
    0.1234,
    0.3434,
    0.565,
    0.656,
    0.665,
    0.897,
]
print("Tests Passed!")

