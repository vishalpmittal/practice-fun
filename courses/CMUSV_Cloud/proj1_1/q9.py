import sys

file = open("output","r")
count_2014 = 0
count_2015 = 0
for line in file:
    line = line.rstrip('\n')
    elements = line.split('\t')
    if 2014_film in elements[0]:
        count_2014 = count_2014+1
    elif 2015_film in elements[0]:
        count_2015 = count_2015+1

if count_2014 > count_2015:
    sys.stdout.write('2014')
else:
    sys.stdout.write('2015')