# When did the article "NASDAQ-100" have the most number of page views?
# Input the answer in yyyymmdd format
# Run your commands/code to process the output and echo the answer 
# in the above format to standard output

import sys
input_title = sys.argv[1]

file = open("output","r")
for line in file:
    line = line.strip()
    elements = line.split("\t")

    if input_title == elements[1]:
        temp_max = -1
        max_date = None

        for i in range(2,33):    
            temp_score = int(elements[i].split(":")[1])

            if temp_score > temp_max:
                temp_max = temp_score
                max_date = elements[i].split(":")[0]

        print max_date
