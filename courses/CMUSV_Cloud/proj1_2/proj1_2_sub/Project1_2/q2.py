file = open("output","r")

max_title = None
max_count = -1

for line in file:
    elements = line.split("\t")
    element_int = int(elements[0])

    if element_int > max_count:
        max_count = element_int
        max_title = elements[1]

print max_title + "\t"+ str(max_count)

