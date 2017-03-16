file = open("output","r")
sum = 0
for line in file:
    line = line.rstrip('\n')
    elements = line.split('\t')
    if elements[0].startswith('List_of') and elements[0].endswith('episodes'):
        element_int = int(elements[1])
        sum = sum+element_int
print sum
