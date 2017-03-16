file = open("filter_output.txt","r")
count = 0
for line in file:
    line = line.rstrip('\n')
    elements = line.split('\t')
    element_int = int(elements[1])
    if element_int> 2500 :
        count = count+1
print count