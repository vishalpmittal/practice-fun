#!/usr/bin/python

# from operator import itemgetter
import sys

print_month = "201508"
current_title = None
title_view_data = {"total":0}
view_limit=100

def print_title_data(title_dict, print_title):
    out_str = str(title_dict["total"])+ "\t" + print_title
    for n in range (1, 32):
        print_date = print_month + '%02d'%n
        out_str += "\t" + print_date + ":"
        if print_date not in title_dict:
            print "I did not find key " + print_date + "in" + str(title_dict)
            out_str += "0"
        else:
            out_str += str(title_dict[print_date])
    print out_str

# input comes from standard input
for line in sys.stdin:
    line = line.strip()

    elements = line.split("\t")
    stin_title = elements[0]
    stin_date = elements[2]
    try:
        stin_views = int(elements[1])
    except valueError:
        continue

    if current_title != stin_title:
        if title_view_data["total"] > view_limit:
            print "here is the whole dictionary" + str(title_view_data)
            print_title_data(title_view_data, current_title)

        title_view_data = {"total":0}
        title_view_data[stin_date] = stin_views
        title_view_data["total"] += stin_views
        current_title = stin_title

    elif current_title == stin_title:
        title_view_data["total"] += stin_views
        if stin_date not in title_view_data:
            title_view_data[stin_date] = stin_views
        else:
            title_view_data[stin_date] += stin_views

if title_view_data["total"] > view_limit:
    print_title_data(title_view_data, current_title)

