"""
    tag: binary search, list
    
    Given a sorted array which is increasing first and then decreasing. 
    Find the max value in the array. 
    
    [10 20 30 40 50 45 35 25 15 10 5]
    max is 50
"""


def find_max(A):
    if not A:
        return None
    if len(A) < 3:
        return max(A)

    l, r = 0, len(A) - 1
    while l < r:
        mid = (l + r) // 2
        if mid == 0:
            return A[0]
        elif A[mid - 1] < A[mid] > A[mid + 1]:
            return A[mid]
        elif A[mid - 1] < A[mid] < A[mid + 1]:
            l = mid + 1
        elif A[mid - 1] > A[mid] > A[mid + 1]:
            r = mid - 1

    return max(A[0], A[-1])


assert find_max(None) == None
assert find_max([]) == None
assert find_max([1, 2]) == 2
assert find_max([2]) == 2
assert find_max([10, 20, 30, 40, 50, 45, 35, 25, 15, 10, 7, 6, 5]) == 50
assert find_max([40, 50, 45, 35, 25, 15, 10, 7, 6, 5]) == 50
assert find_max([40, 50, 45]) == 50
assert find_max([50, 45, 35, 25, 15, 10, 7, 6, 5]) == 50
assert find_max([10, 20, 30, 40, 50, 60]) == 60
assert find_max([4, 3, 2, 1, 0]) == 4
assert find_max([0, 1, 2, 3, 4]) == 4
print("Tests Passed!!")
