#!/bin/bash

if [ $# -eq 0 ]; then
    echo "input file and dictionary missing"
    exit 0
fi

if [ ! -f $1 ]; then
    echo "$1 is not a file"
    exit 0
fi

if [ ! -f $2 ]; then
    echo "$2 is not a file"
    exit 0
fi

while read -r line; do
    # Split the line into words using awk
    for word in $(echo $line | awk '{for(i=1;i<=NF;i++) print $i}'); do
        cleaned_line=$(echo "$word" | sed 's/[.,;?!_:-]//g')
        # Check if the word is 5 letters long
        if [ ${#cleaned_line} -eq 5 ]; then
            if ! grep -q $cleaned_line "$2"; then
                echo "$cleaned_line"
            fi
        fi
    done
done < "$1"