#!/usr/bin/python

# from operator import itemgetter
import sys

current_title = None
current_date = None
title_view_data = {"total":0}

# input comes from standard input

for line in sys.stdin:
    line = line.strip()
    elements = line.split("\t")

    title = elements[0]
    date = elements[2]
    try:
        views = int(elements[1])
    except valueError:
        continue
    
    if current_title == title:
        if current_date == date:
            title_view_data[date] += views
        else:
            current_date = date
            title_view_data[date] = views
        title_view_data["total"] += views

    else:
        if title_view_data["total"] > 10:
            out_str = str(title_view_data["total"])+ "\t" + current_title 
            for n in range (1, 32):
                current_date = "201508"+'%02d'%n
                out_str += "\t" + current_date + ":"
                if current_date not in title_view_data:
                    out_str += "0"
                else:
                    out_str += str(title_view_data[current_date])
            print out_str

        title_view_data = {}
        title_view_data[date] = views
        title_view_data["total"] = views
        current_title = title
        current_date = date

if title_view_data["total"] > 100:
    out_str = str(title_view_data["total"])+ "\t" + current_title 
    for n in range (1, 32):
        current_date = "201508"+'%02d'%n
        out_str += "\t" + current_date + ":"
        if current_date not in title_view_data:
            out_str += "0"
        else:
            out_str += str(title_view_data[current_date])
    print out_str

