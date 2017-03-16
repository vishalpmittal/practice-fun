#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# join2_reducer:
# 
# read lines and split lines into key & value
# if a key has changed (and it's not the first input)
# then check if ABC had been found and print out key and running total,
# 
# if value is ABC then set some variable to mark that ABC was found (like abc_found = True)
# otherwise keep a running total of viewer counts
# 
# --------------------------------------------------------------------------

prev_show = "  "            
op_channel = 'ABC'

curr_show_total_cnt = 0
is_curr_show_on_chnl = False

for line in sys.stdin:
    line = line.strip()       
    curr_show = line.split('\t')[0]
    value_in = line.split('\t')[1]

    if curr_show != prev_show:
        if is_curr_show_on_chnl:
            print('{0} {1}'.format(prev_show,curr_word_total_cnt)) 

        prev_show = curr_show
        curr_word_total_cnt = 0
        is_curr_show_on_chnl = False

    if value_in.isdigit():
        curr_word_total_cnt += int(value_in)
    elif value_in == op_channel:
        is_curr_show_on_chnl = True

if is_curr_show_on_chnl:
    print('{0} {1}'.format(prev_show,curr_word_total_cnt)) 