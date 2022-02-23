"""
    Tag: Math, list, sort

    The power of an integer x is defined as the number of steps needed to 
    transform x into 1 using the following steps:
    
    - if x is even then x = x / 2
    - if x is odd then x = 3 * x + 1

    For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 
    (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
 
    Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] 
    by the power value in ascending order, if two or more integers have the same power value sort 
    them by ascending order.
    
    Return the k-th integer in the range [lo, hi] sorted by the power value.
    
    Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using 
    these steps and that the power of x is will fit in 32 bit signed integer.

    Input: lo = 12, hi = 15, k = 2;  Output: 13
    Input: lo = 1, hi = 1, k = 1;    Output: 1
    Input: lo = 7, hi = 11, k = 4;    Output: 7
    Input: lo = 10, hi = 20, k = 5;    Output: 13
    Input: lo = 1, hi = 1000, k = 777;    Output: 570
"""

powers = {}
    
def get_power(x: int) -> int:
    if x == 1:
        return 0
    
    if x in powers:
        return powers[x]
    
    curr_power = 1
    if x%2 == 0:
        curr_pow += get_power(x/2)
    else:
        curr_pow += get_power(3*x +1)
        
    powers[x] = curr_pow
    return curr_pow


def getKth(lo: int, hi: int, k: int) -> int:
    if lo <0 or hi <0 or hi < lo or k < hi-lo:
        return None

    all_nums = [c for c in range(lo, hi+1)]
    all_nums.sort(key = lambda x: get_power(x))
    return all_nums[k-1]
   

assert(getKth(lo = 12, hi = 15, k = 2) == 13)
assert(getKth(lo = 1, hi = 1, k = 1) == 1)
assert(getKth(lo = 7, hi = 11, k = 4) == 7)
assert(getKth(lo = 10, hi = 20, k = 5) == 13)
assert(getKth(lo = 1, hi = 1000, k = 777) == 570)
print('tests passed!')

