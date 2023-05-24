#!/bin/bash

if [ $# -lt 2 ]; then
    echo "data file or output file not found"
    exit 0
fi

inputfile=$1
if [ ! -f $inputfile ]; then
    echo "$1 not found"
    exit 0
fi

outputfile=$2
if [ ! -f $outputfile ]; then
    touch $outputfile
fi

# Loop through each line in the input file
while read -r line; do
    # Split the line into numbers using ;, :, or , as delimiters
    IFS='\n' read -ra nums <<< "$line"
    nums="${nums[0]}"
    IFS=';:,' read -ra nums <<< "$nums"

    # Loop through the numbers and add them up
    sum=0
    for num in "${nums[@]}"; do
        ((sum+=num))
    done

    # Write the result to the output file
    col_num=$((col_num+1))
    echo "Col $col_num : $sum" 
done < "$inputfile" > "$outputfile"