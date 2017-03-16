#!/usr/bin/python

import os
import sys

viewCountFileName = os.environ["mapreduce_map_input_file"]
data_date = viewCountFileName.split("-")[1]

reserved_list =["Media:","Special:","Talk:","User:","User_talk:","Project:","Project_talk:","File:","File_talk:","MediaWiki:","MediaWiki_talk:","Template:","Template_talk:","Help:","Help_talk:","Category:","Category_talk:","Portal:","Wikipedia:","Wikipedia_talk:"]
extention_list = [".jpg",".gif",".png",".JPG",".GIF",".PNG",".txt",".ico"]
bp_list =["404_error/","Main_Page","Hypertext_Transfer_Protocol","Search"]

## for each line in the file check each condition
for line in sys.stdin:
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

    ## condition 1.2 malformed entries
    if elements[1] == None or elements[1].strip()=="":
        is_proper_string = False

    if is_proper_string:
        print elements[1]+"\t"+elements[2]+"\t"+data_date
