
import sys

file = open("output","r")

min_title = None
min_count = sys.maxint

for line in file:
    elements = line.split("\t")
    element_int = int(elements[0])

    if element_int < min_count:
        min_count = element_int
        min_title = elements[1]

print min_title + "\t"+ str(min_count)

