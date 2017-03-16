"""This is a program to merge a list 
according to the rules in a 2024 game
Author: Vishal Mittal""" 

def slide_zeros_to_right(raw_list):
    """ Function to move all the zeros to 
    right most in a list """
    for iter_out in range(0, len(raw_list)-1):
        for iter_in in range(0, len(raw_list)-iter_out-1):
            if(raw_list[iter_in] == 0 and raw_list[iter_in+1]!=0):
                raw_list[iter_in] = raw_list[iter_in+1]
                raw_list[iter_in+1] = 0

def add_left_common_elements(add_list):
    """ Fuction that takes a list and starting from 
    left adds the similar digits"""
    index = 0
    curr_digit = 0
    while (index < len(add_list)-1):
        if (add_list[index] != 0):
            curr_digit = add_list[index]
            # if duplicate numbers found, add and move two places
            if(curr_digit == add_list[index+1]):
                add_list[index] *= 2
                add_list[index+1] = 0
                curr_digit = 0 
                index += 2
            # else move one place
            else:
                index += 1
        # encountered zero move one place
        else:
            index += 1

def merge(line):
    """ Merge fuction for a list
    Logic : move zeros to right most, 
            add duplicate digits starting from left,
            again move zeros to right most """
    merged_line = list(line)
    slide_zeros_to_right(merged_line)
    add_left_common_elements(merged_line)
    slide_zeros_to_right(merged_line)
    return merged_line

print merge([2, 0, 2, 4])
print merge([0, 2, 0, 0])
print merge([0, 0, 2, 2])
print merge([0, 0, 0, 2])
print merge([2, 0, 2, 0])

print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])
