file = open("pagecounts-20150801-000000","r")
sum = 0
for line in file:
	line = line.rstrip('\n')
	elements = line.split(' ')
	element_int = int(elements[2])
	sum = sum+element_int
print sum
