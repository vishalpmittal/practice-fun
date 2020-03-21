#!/bin/bash

counter=1
file_type='jpg'

getCount() {
    x=$1
    while [ ${#x} -ne 3 ];
    do
       x="0"$x
    done
    echo "$x"
}

if [ $# -eq 2 ]; then
    for entry in "$1"/*
    do
        currCount=$(getCount "$counter")
        newFileName="$2-$currCount.$file_type"
        echo "Renaming $entry to $newFileName"
        mv "$entry" "./$1/$newFileName"
        counter=$((counter+1))
    done
else
    echo "Usage cropWrapper.sh <directory_name> <file_name_prefix>"
fi
