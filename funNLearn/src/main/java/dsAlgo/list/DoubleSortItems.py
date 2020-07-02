"""
    tag: sort, list

    In a warehouse, a manager would like to sort the items in the stock. 
    Given an array of n item values, sort the array in ascending order, 
    first by the number of items with a certain value, then by the values themselves.

    Example: items = [4, 5, 6, 5, 4, 3]
    There are 2 values that occur twice: [4, 4, 5, 5].
    There are 2 values that occur once: [3, 6].
    The array of items sorted by quantity and then by value in 
    ascending order is [3, 6, 4,  4, 5, 5]
    
    Constraints
    -  1 ≤ n ≤ 2 × 105
    -  1 ≤ items[i] ≤ 106
    
    Eg: [3, 1, 2, 2, 4]
    output: [1, 3, 4, 2, 2]

    Eg: [8, 5, 5, 5, 5, 1, 1, 1, 4, 4]
    output: [ 8, 4, 4, 1, 1, 1, 5, 5, 5, 5]
"""
from collections import Counter
import time


def itemsSort(items):
    if not items or len(items) < 2:
        return items

    itm_cnt = Counter(items)

    count_to_items_dict = dict()
    for num, count in itm_cnt.items():
        count_to_items_dict[count] = count_to_items_dict.get(count, [])
        count_to_items_dict[count].append(num)

    ans_list = []
    for cnt in sorted(count_to_items_dict.keys()):
        nums = sorted(count_to_items_dict[cnt])
        for num in nums:
            ans_list.extend([num] * cnt)

    return ans_list


def itemsSort2(items):
    itm_cnt = Counter(items)
    items.sort()
    items.sort(key=lambda x: itm_cnt[x])
    return items


start_time = time.time()
assert itemsSort([3, 1, 2, 2, 4]) == [1, 3, 4, 2, 2]
assert itemsSort([8, 5, 5, 5, 5, 1, 1, 1, 4, 4]) == [8, 4, 4, 1, 1, 1, 5, 5, 5, 5]
print(time.time() - start_time)

start_time = time.time()
assert itemsSort2([3, 1, 2, 2, 4]) == [1, 3, 4, 2, 2]
assert itemsSort2([8, 5, 5, 5, 5, 1, 1, 1, 4, 4]) == [8, 4, 4, 1, 1, 1, 5, 5, 5, 5]
print(time.time() - start_time)


print("Tests Passed!")
