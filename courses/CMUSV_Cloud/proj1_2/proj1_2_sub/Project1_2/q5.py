import sys

data_first = None
data_two = None
days_count = 0

file = open("output","r")

for line in file:
    elements = line.split("\t")

    if elements[1] == sys.argv[1]:
        data_first = elements
    elif elements[1]== sys.argv[2]:
        data_two = elements

    if data_first != None and data_two != None:
        break

if data_first != None and data_two != None:
    for i in range (2,33):
        dateCountFirst = int(data_first[i].split(":")[1])
        dataCountTwo = int (data_two[i].split(":")[1])

        if dateCountFirst>dataCountTwo :
            days_count += 1

print days_count





