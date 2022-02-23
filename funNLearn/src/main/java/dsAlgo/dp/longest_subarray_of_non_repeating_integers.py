"""
    Tag: math, dp

    longest non repeating subarray of integer
    
    eg: [10, 8, 4, 6, 3, 2, 1, 4, 7, 11, 12, 4, 1, 2]
    should return [6, 3, 2, 1, 4, 7, 11, 12]

    also print a tree with them
"""
from typing import List

def get_longest_non_repeating_subarray(arr: List[int]) -> [int, int]:
    
    num2indx = dict()
    longest = -1
    longest_start_indx = 0
    longest_end_indx = 0
    curr_start_indx = 0
    
    for i in range(len(arr)):
        n = arr[i]
        if n in num2indx:
            if i - curr_start_indx > longest:
                longest_start_indx = curr_start_indx             # 0               
                longest_end_indx = i-1                           # 6
                longest = i - curr_start_indx                    # 7
                curr_start_indx = num2indx[n] + 1                # 3
            else:
                curr_start_indx = num2indx[n] + 1                # 3
                
        num2indx[n]=i
   
    if i - curr_start_indx > longest:
        longest_start_indx = curr_start_indx                            
        longest_end_indx = len(arr)-1
    
    return arr[longest_start_indx: longest_end_indx+1]
  

print(get_longest_non_repeating_subarray([1, 2, 3, 2, 4]))
print(get_longest_non_repeating_subarray([1, 2, 3, 4, 4]))
print(get_longest_non_repeating_subarray([1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10, 4]))
print(get_longest_non_repeating_subarray([10, 8, 4, 6, 3, 2, 1, 4, 7, 11, 12, 4, 1, 2]))
