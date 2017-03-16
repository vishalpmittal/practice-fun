
# Rank the operating systems in the file q7 based on their total wikipedia page views for August 2015
# (In descending order of page views, with the highest one first):
# OS_X,Windows_7,Windows_10,Linux
# Ensure that you print the answers comma separated (As shown in the above line)
# For your convenience, code to read the file q7 is given below. Feel free to modify.
import sys
os_dic = {}

os_file = open(sys.argv[1], "r")
for os in os_file:
    os = os.strip()
    os_dic[os]= 0

file = open("output","r")
for line in file:
    line = line.strip()
    elements = line.split("\t")

    if elements[1] in os_dic:
        os_dic[elements[1]] = int(elements[0])

temp_string = ""
for os in sorted(os_dic, key=os_dic.get, reverse=True):
    temp_string += os +", "
print temp_string[:-2]
