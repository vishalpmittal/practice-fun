file = open("output","r")

max_title = None
max_count = -1

for line in file:
    elements = line.split("\t")
    element_int = int(elements[0])
    aug1st_views = elements[2].split(":")[1]
    
    if  int(aug1st_views) == 0 and element_int > max_count :
        max_count = element_int
        max_title = elements[1]

print max_title

