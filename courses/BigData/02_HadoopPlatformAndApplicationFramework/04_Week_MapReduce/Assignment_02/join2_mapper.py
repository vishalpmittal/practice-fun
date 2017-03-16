#!/usr/bin/env python
import sys

# -----------------------------------------------------------------
# join2_mapper:
# 
# read lines, and split lines into key & value
# if value is ABC or if value is a digit print it out
# 
# Note that you can test just the mapper by running something like:
# >cat join2_gen*.txt | ./join2_mapper.py | sort
# -----------------------------------------------------------------

for line in sys.stdin:
    line       = line.strip()
    key_value  = line.split(",")
    
    if key_value[1]=='ABC' or key_value[1].isdigit():
        print( '%s\t%s' % (key_value[0], key_value[1]) )
