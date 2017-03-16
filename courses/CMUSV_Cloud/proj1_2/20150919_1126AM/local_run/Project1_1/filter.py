def merge_sort(data_list):
    if len(data_list) > 1:
        # Determine the pivot point and split
        pivot  = len(data_list) / 2        
        l_list = data_list[0:pivot ]
        r_list = data_list[pivot :]

        # Sort l_list list in-place
        merge_sort(l_list)

        # Sort r_list list in-place           
        merge_sort(r_list)           

        l, r = 0, 0
        # Merging the l_list and r_list list
        for i in range(len(data_list)):     

            l_val = l_list[l] if l < len(l_list) else None
            r_val = r_list[r] if r < len(r_list) else None
            if l_val:
                lcomp = int(l_val.split(" ")[0])
            if r_val:
                rcomp = int(r_val.split(" ")[0])

            if (l_val and r_val and lcomp >= rcomp) or r_val is None:
                data_list[i] = l_val
                l += 1
            elif (l_val and r_val and lcomp < rcomp) or l_val is None:
                data_list[i] = r_val
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')

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

merge_sort(all_lines)

for i in range(0, len(all_lines)):
    component= all_lines[i].split(' ') 
    all_lines[i]=component[1]+"\t"+component[0]

out_file =open('output', 'w')
for myLine in all_lines:
    out_file.write(myLine+'\n')
out_file.close()
