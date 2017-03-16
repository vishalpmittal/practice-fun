# # a = ["poorva","prashi","vishal","khushboo","Ankit"]
# # a.append("Nilesh")
# # for i in range(len(a)):
# #     print(a[i])
# # 	


# # p="en File:Indacaterol_structure.svg 1 9037"
# # p="vi File:Indacaterol_structure.svg 1 9037"
# # if 'en' in p[0:2]:
# #     print "it has en"
# # else:
# # 	print "no"
# l = "poorva.jpg"
# print l[(len(l)-4):]

# # p = "it is right Media Special"
# # for i in range(0,len(l)):
# # 	if l[i] in p[5:]:
# # 		print "it has wrong name"
# # 	else:
# # 		print "true"


#   >>> def byAge_key(person):
#   ...     return person.age
#   ... 
#   >>> sorted(people, key = byAge_key)
#   [<name: Becky, age: 11>, <name: Jack, age: 19>, <name: Adam, age: 43>]

#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList[2] = 'vishal'
aList.sort();
print "List : ", aList