file = open("pagecounts-20150801-000000","r")
all_lines =[]
reserved_list =["Media:","Special:","Talk:","User:","User_talk:","Project:","Project_talk:","File:","File_talk:","MediaWiki:","MediaWiki_talk:","Template:","Template_talk:","Help:","Help_talk:","Category:","Category_talk:","Portal:","Wikipedia:","Wikipedia_talk:"]
extention_list = [".jpg",".gif",".png",".JPG",".GIF",".PNG",".txt",".ico"]
bp_list =["404_error/","Main_Page","Hypertext_Transfer_Protocol","Search"]

## for each line in the file check each condition
for line in file:
	is_proper_string = True
	line = line.rstrip('\n')
	elements = line.split(' ')

	## condition 1 : should start with "en"
	if 'en' != elements[0]:
		is_proper_string = False

	## condition 2: should not contain reserved_list words 
	for i in range(0,len(reserved_list)):
		if reserved_list[i] in elements[1][0:]:
			is_proper_string = False

	## condition 3: Article must start with upper case and keep special article name
	if elements[1][0:1].islower():
		is_proper_string = False

	## condition4 : remove give image pattern file
	if elements[1][(len(elements[1])-4): ] in extention_list :
		is_proper_string = False

	## Condition 5 : Remove boilerplate pages
	if elements[1] in bp_list:
		is_proper_string = False


	if is_proper_string:
		all_lines.append(elements[2]+" "+elements[1])
		all_lines = sorted(all_lines)


for myLine in all_lines:
	print myLine


# # [project name] [page title] [number of accesses] [total data returned in bytes]
# fr.b Special:Recherche/All_Mixed_Up 1 730

# -  project name starting with en
# - tile should not be key words
# - Article must start with upper case and keep special article name
# -  remove give image pattern file
# -  remove boilerplate page title files
# -  sorting of output in decending order for number of access.
# - [page title]\t[number of accesses]


