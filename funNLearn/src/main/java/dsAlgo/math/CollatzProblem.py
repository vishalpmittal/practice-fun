"""
    Tag: math

    The following iterative sequence is defined for the set of positive integers:
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    
    Which starting number, under one million, produces the longest chain?
    
    NOTE: Once the chain starts the terms are allowed to go above one million.
    1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.....
"""


def find_long_chain_number(N: int = 1000000) -> (int, int):
    if not N or N < 0:
        return None
    
    longest_chain_len = 0 
    longest_chain_num = -1
    inc_counter = 1
    
    count_dict = {}
    
    while inc_counter <= N:
        chain_len = 0
        n = inc_counter
        while n >= 1:
            if n in count_dict:
                chain_len += count_dict[n]
                break
            elif n == 1:
                chain_len += 1
                break
            elif n%2 == 0:
                n = n/2
            else: 
                n = (3*n) + 1
            
            chain_len += 1            
            
        count_dict[inc_counter] = chain_len
        
        if chain_len > longest_chain_len:
            longest_chain_len = chain_len 
            longest_chain_num = inc_counter
            
        inc_counter += 1

    return longest_chain_num, longest_chain_len
            
    
print(find_long_chain_number(N=1000000))
